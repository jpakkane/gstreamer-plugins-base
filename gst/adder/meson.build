configure_file(input : 'gstadderorc-dist.h',
  output : 'gstadderorc.h',
  configuration : configuration_data())

adder = library('gstadder',
  'gstadder.c',
  include_directories : core_inc,
  c_args: core_args,
  dependencies : [gst_dep, glib_dep],
)
