configure_file(input : 'gstvideotestsrcorc-dist.h',
  output : 'gstvideotestsrcorc.h',
  configuration : configuration_data())

gstvideotestsrc = library('gstvideotestsrc',
  'gstvideotestsrc.c', 'videotestsrc.c',
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [video_dep, gst_dep, glib_dep]
)
