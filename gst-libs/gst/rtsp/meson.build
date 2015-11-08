rtsp_sources = [
  'gstrtsptransport.c',
  'gstrtspurl.c',
  'gstrtspmessage.c',
  'gstrtspconnection.c',
  'gstrtspdefs.c',
  'gstrtspextension.c',
  'gstrtsprange.c'
  ]

mkenums = find_program('rtsp_mkenum.py')
genmarshal = find_program('rtsp_marshal.py')

marshal_header = custom_target('rstp_marshal_h',
  output : 'gstrtsp-marshal.h',
  input : 'gstrtsp-marshal.list',
  command : [genmarshal, '@INPUT@', '@OUTPUT@']
)
marshal_src = custom_target('rstp_marshal_c',
  output : 'gstrtsp-marshal.c',
  input : 'gstrtsp-marshal.list',
  command : [genmarshal, '@INPUT@', '@OUTPUT@']
)

gstrtsp_h = custom_target('gstrtspenum_h',
  output : 'gstrtsp-enumtypes.h',
  input : 'gstrtspdefs.h',
  command : [mkenums, '@OUTPUT@', '@INPUT@'])

gstrtsp_c = custom_target('gstrtspenum_c',
  output : 'gstrtsp-enumtypes.c',
  input : 'gstrtspdefs.h',
  command : [mkenums, '@OUTPUT@', '@INPUT@'])


gstsdp = library('gstrtsp',
  rtsp_sources, marshal_src, marshal_header,
  gstrtsp_h, gstrtsp_c,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [gst_dep, glib_dep],
)
