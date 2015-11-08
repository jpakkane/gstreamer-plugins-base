pbutils_sources = [
  'gstpluginsbaseversion.c',
  'pbutils.c',
  'codec-utils.c',
  'descriptions.c',
  'encoding-profile.c',
  'encoding-target.c',
  'install-plugins.c',
  'missing-plugins.c',
  'gstdiscoverer.c',
  'gstdiscoverer-types.c'
  ]

pbconf = configuration_data()
pbconf.set('PACKAGE_VERSION_MAJOR', version_major)
pbconf.set('PACKAGE_VERSION_MINOR', version_minor)
pbconf.set('PACKAGE_VERSION_MICRO', version_micro)
pbconf.set('PACKAGE_VERSION_NANO', version_nano)
configure_file(input : 'gstpluginsbaseversion.h.in',
  output: 'gstpluginsbaseversion.h',
  configuration: pbconf)

pbutils_mkenum_headers = ['pbutils.h', 'codec-utils.h', 'descriptions.h', 'encoding-profile.h', 'encoding-target.h', 'install-plugins.h', 'missing-plugins.h', 'gstdiscoverer.h']

mkenums = find_program('pbutils_mkenum.py')
gstpbutils_h = custom_target('gstpbutilsenum_h',
  output : 'pbutils-enumtypes.h',
  input : pbutils_mkenum_headers,
  command : [mkenums, '@OUTPUT@', '@INPUT@'])

gstpbutils_c = custom_target('gstpbutilsenum_c',
  output : 'pbutils-enumtypes.c',
  input : pbutils_mkenum_headers,
  command : [mkenums, '@OUTPUT@', '@INPUT@'])



pbutils = library('gstpbutils',
  pbutils_sources, gstpbutils_c, gstpbutils_h,
  c_args : core_args,
  include_directories : core_inc,
  dependencies : [gst_dep, glib_dep]
)

