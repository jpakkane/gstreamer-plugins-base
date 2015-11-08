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
  'streamvolume.c',
  'gstaudioiec61937.c',
]

audio_headers = [
  'audio-channels.h',
  'audio-format.h',
  'audio.h',
  'audio-info.h',
  'gstaudiobasesink.h',
  'gstaudiobasesrc.h',
  'gstaudiocdsrc.h',
  'gstaudioclock.h',
  'gstaudiodecoder.h',
  'gstaudioencoder.h',
  'gstaudiofilter.h',
  'gstaudioiec61937.h',
  'gstaudiometa.h',
  'gstaudiopack-dist.h',
  'gstaudioringbuffer.h',
  'gstaudiosink.h',
  'gstaudiosrc.h',
  'gstaudioutilsprivate.h',
  'streamvolume.h',
]

gstaudio_h = custom_target('gstaudioenum_h',
  output : 'audio-enumtypes.h',
  input : audio_headers,
  command : [mkenums, '@OUTPUT@', '@INPUT@'])

gstaudio_c = custom_target('gstaudioenum_c',
  output : 'audio-enumtypes.c',
  input : audio_headers,
  command : [mkenums, '@OUTPUT@', '@INPUT@'])


gstaudio = shared_library('gstaudio',
  audio_src, gstaudio_h, gstaudio_c,
  include_directories : gstlib_inc,
  c_args: ['-DGETTEXT_PACKAGE="foobar"',
    '-DPACKAGE="fff"',
    '-DVERSION="fff"',
    '-DGST_PACKAGE_NAME="fff"',
    '-DGST_PACKAGE_ORIGIN="fff"',],
  dependencies : [gst_dep, glib_dep])
