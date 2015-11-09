tcp_sources = [
  'gsttcpplugin.c',
  'gsttcpclientsrc.c',
  'gsttcpclientsink.c',
  'gstmultihandlesink.c',
  'gstmultisocketsink.c',
  'gsttcpserversrc.c',
  'gsttcpserversink.c'
]

if core_conf.has('HAVE_SYS_SOCKET_H')
   tcp_sources += 'gstmultifdsink.c'
endif

gsttcp = library('gsttcp',
  tcp_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [giounix_dep, gst_dep, glib_dep]
)
