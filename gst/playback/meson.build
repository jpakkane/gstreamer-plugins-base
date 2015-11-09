playback_sources = [
  'gstdecodebin2.c',
  'gsturidecodebin.c',
  'gstplayback.c',
  'gstplaybin2.c',
  'gstplaysink.c',
  'gstplay-enum.c',
  'gstsubtitleoverlay.c',
  'gstplaysinkvideoconvert.c',
  'gstplaysinkaudioconvert.c',
  'gstplaysinkconvertbin.c',
  'gststreamsynchronizer.c'
]

gstplayback = library('gstplayback',
  playback_sources,
  include_directories : core_inc,
  c_args : core_args + ['-DCOLORSPACE="videoconvert"'],
  dependencies : [audio_dep, video_dep, gst_dep, glib_dep]
)
