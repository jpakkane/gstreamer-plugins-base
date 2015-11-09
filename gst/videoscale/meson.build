videoscale_sources = [
  'gstvideoscale.c',
  'vs_image.c',
  'vs_scanline.c',
  'vs_4tap.c',
  'vs_fill_borders.c',
  'vs_lanczos.c'
]

configure_file(input : 'gstvideoscaleorc-dist.h',
  output : 'gstvideoscaleorc.h',
  configuration : configuration_data())

gstvideoscale = library('gstvideoscale',
  videoscale_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [video_dep, gst_dep, glib_dep]
)