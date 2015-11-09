encoding_sources = ['gstencodebin.c',
  'gstsmartencoder.c',
  'gststreamcombiner.c',
  'gststreamsplitter.c',
  ]

gstencoding = library('gstencodebin',
  encoding_sources,
  c_args : core_args,
  include_directories : core_inc,
  dependencies : [pbutils_dep, gst_dep, glib_dep]
)
