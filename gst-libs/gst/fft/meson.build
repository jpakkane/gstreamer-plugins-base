fft_sources = [
  'gstfft.c',
  'gstffts16.c',
  'gstffts32.c',
  'gstfftf32.c',
  'gstfftf64.c',
  'kiss_fft_s16.c',
  'kiss_fft_s32.c',
  'kiss_fft_f32.c',
  'kiss_fft_f64.c',
  'kiss_fftr_s16.c',
  'kiss_fftr_s32.c',
  'kiss_fftr_f32.c',
  'kiss_fftr_f64.c'
]

gstfft = library('gstfft',
  fft_sources,
  c_args : core_args,
  include_directories : core_inc,
  dependencies : [gst_dep, glib_dep],
  )
