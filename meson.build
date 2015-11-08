project('gst-plugins-base', 'c', 'cpp', version : '1.4.5',
  default_options : ['warning_level=1', 'c_std=gnu99'])



cdata = configuration_data()
cdata.set('GETTEXT_PACKAGE', '"foobar"')
cdata.set('PACKAGE', '"fff"')
cdata.set('VERSION', '"fff"')
cdata.set('GST_PACKAGE_NAME', '"fff"')
cdata.set('GST_PACKAGE_ORIGIN', '"fff"')
cdata.set('GST_API_VERSION', '"@0@"'.format(meson.project_version()))

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)

core_args = ['-DHAVE_CONFIG_H']

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

core_inc = include_directories('gst-libs', '.')

mkenums = find_program('build_mkenum.py')

# To use the subproject make subprojects directory
# and put gstreamer meson git there (symlinking is fine)
gst_dep = dependency('gstreamer-1.0')
#gst_proj = subproject('gstreamer')
#gst_dep = gst_proj.get_variable('gst_dep')

subdir('gst-libs')
subdir('gst')
