link

        canonical_package_name = canonicalize_name(package_name)
        for wheel_name, wheel_dir in self._get_candidates(
            link, canonical_package_name
        ):
            try:
                wheel = Wheel(wheel_name)
            except InvalidWheelFilename:
                continue
            if canonicalize_name(wheel.name) != canonical_package_name:
                logger.debug(
                    "Ignoring cached wheel %s for %s as it "
                    "does not match the expected distribution name %s.",
                    wheel_name, link, package_name,
                )
                continue
            if not wheel.supported(supported_tags):
                # Built for a different python/arch/etc
                continue
            candidates.append(
                (
                    wheel.support_index_min(supported_tags),
                    wheel_name,
                    wheel_dir,
                )
            )

        if not candidates:
            return link

        _, wheel_name, wheel_dir = min(candidates)
        return Link(path_to_url(os.path.join(wheel_dir, wheel_name)))


class EphemWheelCache(SimpleWheelCache):
    """A SimpleWheelCache that creates it's own temporary cache directory
    """

    def __init__(self, format_control):
        # type: (FormatControl) -> None
        self._temp_dir = TempDirectory(
            kind=tempdir_kinds.EPHEM_WHEEL_CACHE,
            globally_managed=True,
        )

        super(EphemWheelCache, self).__init__(
            self._temp_dir.path, format_control
        )


class CacheEntry(object):
    def __init__(
        self,
        link,  # type: Link
        persistent,  # type: bool
    ):
        self.link = link
        self.persistent = persistent


class WheelCache(Cache):
    """Wraps EphemWheelCache and SimpleWheelCache into a single Cache

    This Cache allows for gracefully degradation, using the ephem wheel cache
    when a certain link is not found in the simple wheel cache first.
    """

    def __init__(self, cache_dir, format_control):
        # type: (str, FormatControl) -> None
        super(WheelCache, self).__init__(
            cache_dir, format_control, {'binary'}
        )
        self._wheel_cache = SimpleWheelCache(cache_dir, format_control)
        self._ephem_cache = EphemWheelCache(format_control)

    def get_path_for_link_legacy(self, link):
        # type: (Link) -> str
        return self._wheel_cache.get_path_for_link_legacy(link)

    def get_path_for_link(self, link):
        # type: (Link) -> str
        return self._wheel_cache.get_path_for_link(link)

    def get_ephem_path_for_link(self, link):
        # type: (Link) -> str
        return self._ephem_cache.get_path_for_link(link)

    def get(
        