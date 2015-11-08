rtp_sources = [
  'gstrtpbuffer.c',
  'gstrtcpbuffer.c',
  'gstrtppayloads.c',
  'gstrtphdrext.c',
  'gstrtpbaseaudiopayload.c',
  'gstrtpbasepayload.c',
  'gstrtpbasedepayload.c'
  ]

gst_rtp = library('gstrtp',
  rtp_sources,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : [gst_dep, glib_dep]
)
