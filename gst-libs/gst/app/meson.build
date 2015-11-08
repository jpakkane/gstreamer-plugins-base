app_sources = ['gstappsrc.c', 'gstappsink.c']

genmarshal = find_program('app_marshal.py')

marshal_header = custom_target('app_marshal_h',
  output : 'gstapp-marshal.h',
  input : 'gstapp-marshal.list',
  command : [genmarshal, '@INPUT@', '@OUTPUT@']
)
marshal_src = custom_target('app_marshal_c',
  output : 'gstapp-marshal.c',
  input : 'gstapp-marshal.list',
  command : [genmarshal, '@INPUT@', '@OUTPUT@']
)


gstapp = library('gstapp',
  app_sources, marshal_src, marshal_header,
  c_args : core_args,
  include_directories : core_inc,
  dependencies : [gst_dep, glib_dep]
  )
