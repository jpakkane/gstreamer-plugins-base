tool_deps = [pbutils_dep, audio_dep, video_dep, gst_dep]

executable('gst-device-monitor-@0@'.format(api_version),
  'gst-device-monitor.c',
  link_with : gsttag,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : tool_deps,
)

executable('gst-discoverer-@0@'.format(api_version),
  'gst-discoverer.c',
  link_with : gsttag,
  include_directories : core_inc,
  c_args : core_args,
  dependencies : tool_deps,
)

executable('gst-play-@0@'.format(api_version),
  'gst-play.c', 'gst-play-kb.c',
  link_with : gsttag,
  include_directories : core_inc,
  c_args : core_args,
  link_args : ['-lm'], # FIXME, device a better way to do lm.
  dependencies : tool_deps,
)
