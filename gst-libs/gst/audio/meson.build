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
  'streamvolume.h',
]

audio_mkenum_headers = [
  'audio-format.h',
  'audio-channels.h',
  'audio-info.h',
  'gstaudioringbuffer.h',
]

mkenums = find_program('audio_mkenum.py')
gstaudio_h = custom_target('gstaudioenum_h',
  output : 'audio-enumtypes.h',
  input : audio_mkenum_headers,
  command : [mkenums, '@OUTPUT@', '@INPUT@'])

gstaudio_c = custom_target('gstaudioenum_c',
  output : 'audio-enumtypes.c',
  input : audio_mkenum_headers,
  command : [mkenums, '@OUTPUT@', '@INPUT@'])

cdata = configuration_data()
configure_file(input : 'gstaudiopack-dist.h',
  output : 'gstaudiopack.h',
  configuration : cdata)

gstaudio = library('gstaudio-@0@'.format(api_version),
  audio_src, gstaudio_h, gstaudio_c,
  include_directories : core_inc,
  c_args: core_args,
  dependencies : [gst_dep, glib_dep])
