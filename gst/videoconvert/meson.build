vconvert_sources = [
  'gstvideoconvert.c',
  'videoconvert.c',
  'gstcms.c'
]

configure_file(input : 'gstvideoconvertorc-dist.h',
  output : 'gstvideoconvertorc.h',
  configuration : configuration_data())

gstvideoconvert = library('gstvideoconvert',
  vconvert_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [video_dep, gst_dep, glib_dep]
)

