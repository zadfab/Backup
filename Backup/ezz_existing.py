
def save(self, *args, **kwargs):
    #self.full_clean() # This function internally call clean() method.

    if self.ezz_id is  None and  self._state.adding :
        obj = CustomerDetails.objects.order_by('id').last()
        try:
            numeric = int(obj.ezz_id[-5:])
        except:
            numeric = 0
        self.ezz_id = f"EZ{self.country.fedex_code}{numeric+1:05}"
    return super(CustomerDetails, self).save(*args, **kwargs)