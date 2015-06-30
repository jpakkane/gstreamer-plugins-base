audio_src= [
  'audio.c',
  'audio-format.c',
  'audio-channels.c',
  'audio-info.c',
  'gstaudioringbuffer.c',
  'gstaudioclock.c',
  'gstaudiocdsrc.c',
  'gstaudiodecoder.c',
  'gstaudioencoder.c',
  'gstaudiobasesink.c',
  'gstaudiobasesrc.c',
  'gstaudiofilter.c',
  'gstaudiometa.c',
  'gstaudiosink.c',
  'gstaudiosrc.c',
  'gstaudioutilsprivate.c',
  'streamvolume.c',
  'gstaudioiec61937.c',
]

# generate audio h and c files with
# glib-mkenums here

gstaudio = shared_library('gstaudio',
  audio_src,
  include_directories : gstlib_inc,
  dependencies : [gst_dep, glib_dep])
