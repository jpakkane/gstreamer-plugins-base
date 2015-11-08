aconv_sources = [
  'gstaudioconvert.c',
  'audioconvert.c',
  'gstchannelmix.c',
  'gstaudioquantize.c',
  'plugin.c'
  ]

configure_file(input : 'gstaudioconvertorc-dist.h',
  output : 'gstaudioconvertorc.h',
  configuration : configuration_data())

gstaudioconvert = library('gstaudioconvert',
  aconv_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [audio_dep, gst_dep, glib_dep],
)
