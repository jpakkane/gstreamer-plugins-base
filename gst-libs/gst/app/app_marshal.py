#!/usr/bin/env python3

import sys, subprocess

assert(len(sys.argv) == 3)

_, listname, outname = sys.argv

if outname.endswith('.h'):
    arg = '--header'
else:
    arg = '--body'

output = subprocess.check_output(['glib-genmarshal', '--prefix=__gst_app_marshal', arg, listname])
open(outname, 'wb').write(output)
