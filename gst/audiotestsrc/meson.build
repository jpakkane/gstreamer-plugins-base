audiotest = shared_library('gstaudiotestsrc',
  'gstaudiotestsrc.c', gstaudio_h,
  include_directories : gstlib_inc,

  c_args: ['-DGETTEXT_PACKAGE="foobar"',
    '-DPACKAGE="fff"',
    '-DVERSION="fff"',
    '-DGST_PACKAGE_NAME="fff"',
    '-DGST_PACKAGE_ORIGIN="fff"',],
  dependencies : [gst_dep, glib_dep],
)
