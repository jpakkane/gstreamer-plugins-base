subparse_sources = [
  'gstssaparse.c',
  'gstsubparse.c',
  'samiparse.c',
  'tmplayerparse.c',
  'mpl2parse.c',
  'qttextparse.c',
]

gstsubparse = library('gstsubparse',
  subparse_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [gst_dep, glib_dep]
)
