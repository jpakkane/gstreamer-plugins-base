xvimage_sources = [
  'xvimagesink.c',
  'xvimage.c',
  'xvimagepool.c',
  'xvimageallocator.c',
]

gstxvimage = library('gstxvimage',
  xvimage_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [gst_dep, glib_dep]
)