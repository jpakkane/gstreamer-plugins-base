gio_sources = ['gstgio.c',
  'gstgiobasesink.c',
  'gstgiobasesrc.c',
  'gstgiosink.c',
  'gstgiosrc.c',
  'gstgiostreamsink.c',
  'gstgiostreamsrc.c',
]

gstgio = library('gstgio',
  gio_sources,
  c_args : core_args,
  include_directories : core_inc,
  dependencies : [gst_dep, giounix_dep, glib_dep])
