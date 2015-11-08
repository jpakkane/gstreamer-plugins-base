#configure_file(input : 'gstadderorc-dist.h',
#  output : 'gstadderorc.h',
#  configuration : configuration_data())

adder = library('gstapp',
  'gstapp.c',
  include_directories : core_inc,
  c_args: core_args,
  link_with : gstaudio,
  dependencies : [gst_dep, glib_dep],
)
