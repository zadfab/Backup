, %r528; bra.uni 	BB4_362;  BB4_364: div.u64 	%rd1066, %rd325, %rd2; rem.u64 	%rd1067, %rd325, %rd2;  BB4_366:  mul.lo.s64 	%rd830, %rd12, %rd1066; add.s64 	%rd831, %rd830, %rd13; mul.lo.s64 	%rd832, %rd831, %rd2; add.s64 	%rd833, %rd832, %rd1067; cvt.u32.u64	%r730, %rd833; bra.uni 	BB4_368;  BB4_360: div.u64 	%rd1064, %rd13, %rd2; rem.u64 	%rd1065, %rd13, %rd2;  BB4_362:  cvt.u64.u32	%rd824, %r647; mul.lo.s64 	%rd825, %rd17, %rd1064; add.s64 	%rd826, %rd825, %rd824; mul.lo.s64 	%rd827, %rd826, %rd2; add.s64 	%rd828, %rd827, %rd1065; cvt.u32.u64	%r730, %rd828;  BB4_368:  mul.wide.u32 	%rd837, %r730, 2; add.s64 	%rd838, %rd19, %rd837; st.global.u16 	[%rd838], %rs107;  add.s32 	%r647, %r647, 1;  BB4_369:  setp.lt.u32	%p242, %r644, %r5; and.pred  	%p244, %p242, %p9; mov.u16 	%rs44, 0;  @!%p244 bra 	BB4_383; bra.uni 	BB4_370;  BB4_370: setp.eq.s32	%p245, %r4, -1;  @%p245 bra 	BB4_381; bra.uni 	BB4_371;  BB4_381:  cvt.u64.u32	%rd850, %r644; mul.lo.s64 	%rd851, %rd11, %rd850; add.s64 	%rd852, %rd15, %r