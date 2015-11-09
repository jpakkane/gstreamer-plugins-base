riff_sources = [
  'riff.c',
  'riff-media.c',
  'riff-read.c',
]

gstriff = library('gstriff',
  riff_sources,
  c_args : core_args,
  include_directories : core_inc,
  dependencies : [audio_dep, gst_dep, glib_dep],
)
