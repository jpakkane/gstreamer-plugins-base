project('gst-plugins-base', 'c', 'cpp',
  default_options : ['warning_level=1', 'c_std=gnu99'])

libm = find_library('m', required : false)
alsa_dep = dependency('alsa', version : '>=0.9.1')
cdpara_dep = dependency('cdparanoia-3', version : '>=10.2', required : false)
vorbisidec_dep = dependency('vorbisidec', required : false)
ogg_dep = dependency('ogg', version : '>=1.0', required : false)
pango_dep = dependency('pango', version : '>=1.22.0', required : false)
pangocairo_dep = dependency('pangocairo', version : '>=1.22.0', required : false)
theora_dep = dependency('theora', version : '>=1.1')
theoraenc_dep = dependency('theoraenc', version : '>=1.1')
vorbis_dep = dependency('vorbis', version : '>=1.0')
giounix_dep = dependency('gio-unix-2.0', version : '>=2.24')
ft2_dep = dependency('freetype2', version : '>=2.0.9', required : false)
glib_dep = dependency('glib-2.0')

gstlib_inc = include_directories('gst-libs')

mkenums = find_program('build_mkenum.py')

# To use the subproject make subprojects directory
# and put gstreamer meson git there (symlinking is fine)
gst_dep = dependency('gstreamer-1.0')
#gst_proj = subproject('gstreamer')
#gst_dep = gst_proj.get_variable('gst_dep')

subdir('gst-libs')
subdir('gst')
