resample_sources = ['gstaudioresample.c',
  'speex_resampler_int.c',
  'speex_resampler_float.c',
  'speex_resampler_double.c'
]

audioresample = library('gstaudioresample',
  resample_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [audio_dep, gst_dep, glib_dep],
  )