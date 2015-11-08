tag_sources = [
  'gstvorbistag.c',
  'gstid3tag.c',
  'gstxmptag.c',
  'gstexiftag.c',
  'lang.c',
  'licenses.c',
  'tags.c',
  'gsttagdemux.c',
  'gsttagmux.c',
  'gsttageditingprivate.c',
  'id3v2.c',
  'id3v2frames.c',
  'xmpwriter.c',
]

gsttag = library('gsttag',
  tag_sources,
  c_args : core_args,
  include_directories: core_inc,
  dependencies : [gst_dep, glib_dep])
