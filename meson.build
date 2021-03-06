project('gst-plugins-base', 'c', 'cpp', version : '1.4.5',
  default_options : ['warning_level=1', 'c_std=gnu99'])

varr = meson.project_version().split('.')
version_major = varr[0]
version_minor = varr[1]
version_micro = varr[2]
version_nano = 1
api_version = '1.0'

cc = meson.get_compiler('c')

core_conf = configuration_data()
check_headers = [
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_EMMINTRIN_H', 'emmintrin.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_PROCESS_H', 'process.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_SOCKET_H', 'sys/socket.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_SYS_WAIT_H', 'sys/wait.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
  ['HAVE_WINSOCK2_H', 'winsock2.h'],
  ['HAVE_XMMINTRIN_H', 'xmmintrin.h'],
]
foreach h : check_headers
  if cc.has_header(h.get(1))
    core_conf.set(h.get(0), 1)
  endif
endforeach

check_functions = [
  ['HAVE_DCGETTEXT', 'dcgettext', '#include<libintl.h>'],
  ['HAVE_GMTIME_R', 'gmtime_r', '#include<time.h>'],
  ['HAVE_LRINTF', 'lrintf', '#include<math.h>'],
  ['HAVE_MMAP', 'mmap', '#include<sys/mman.h>'],
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    core_conf.set(f.get(0), 1)
  endif
endforeach

core_conf.set('SIZEOF_CHAR', cc.sizeof('char'))
core_conf.set('SIZEOF_INT', cc.sizeof('int'))
core_conf.set('SIZEOF_LONG', cc.sizeof('long'))
core_conf.set('SIZEOF_SHORT', cc.sizeof('short'))
core_conf.set('SIZEOF_VOIDP', cc.sizeof('void*'))

core_conf.set('GETTEXT_PACKAGE', '"foobar"')
core_conf.set('PACKAGE', '"fff"')
core_conf.set('VERSION', '"fff"')
core_conf.set('PACKAGE_VERSION', '"fff"')
core_conf.set('GST_PACKAGE_NAME', '"fff"')
core_conf.set('GST_PACKAGE_ORIGIN', '"fff"')
core_conf.set('GST_API_VERSION', '"@0@"'.format(meson.project_version()))
core_conf.set('GST_INSTALL_PLUGINS_HELPER', '"/FIXME"')
core_conf.set('GST_DATADIR', '"/FIXME"')
core_conf.set('GST_LICENSE', '"FIXME"')
core_conf.set('DISABLE_ORC', 1)
core_conf.set('GIO_MODULE_DIR', '"FIXME"')
core_conf.set('GIO_LIBDIR', '"FIXME"')
core_conf.set('DEFAULT_VIDEOSINK', '"FIXME"')
core_conf.set('DEFAULT_AUDIOSINK', '"FIXME"')

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

core_conf.set('HAVE_GIO_UNIX_2_0', giounix_dep.found())
core_conf.set('HAVE_OGG', ogg_dep.found())
core_conf.set('HAVE_THEORA', theora_dep.found())

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : core_conf)

core_inc = include_directories('gst-libs', '.')

# To use the subproject make subprojects directory
# and put gstreamer meson git there (symlinking is fine)
gst_dep = dependency('gstreamer-1.0')
gst_base_dep = dependency('gstreamer-base-1.0')
#gst_proj = subproject('gstreamer')
#gst_dep = gst_proj.get_variable('gst_dep')

subdir('gst-libs')
subdir('gst')
subdir('sys')
subdir('tools')
