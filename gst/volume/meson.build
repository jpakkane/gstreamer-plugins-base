configure_file(input : 'gstvolumeorc-dist.h',
  output : 'gstvolumeorc.h',
  configuration : configuration_data())

gstvolume = library('gstvolume', 'gstvolume.c',
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [audio_dep, gst_dep, glib_dep]
)
