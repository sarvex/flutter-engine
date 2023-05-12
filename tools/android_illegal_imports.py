#!/usr/bin/env python
# Copyright 2013 The Flutter Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import os
import subprocess
import sys

ANDROID_LOG_CLASS = 'android.util.Log'
FLUTTER_LOG_CLASS = 'io.flutter.Log'

def main():
  parser = argparse.ArgumentParser(description='Checks Flutter Android library for forbidden imports')
  parser.add_argument('--stamp', type=str, required=True)
  parser.add_argument('--files', type=str, required=True, nargs='+')
  args = parser.parse_args()

  open(args.stamp, 'a').close()

  bad_files = []

  for file in args.files:
    if file.endswith(os.path.join('io', 'flutter', 'Log.java')):
      continue
    with open(file) as f:
      if ANDROID_LOG_CLASS in f.read():
        bad_files.append(file)

  if bad_files:
    print('')
    print(f'Illegal import {ANDROID_LOG_CLASS} detected in the following files:')
    for bad_file in bad_files:
      print(f'  - {bad_file}')
    print(f'Use {FLUTTER_LOG_CLASS} instead.')
    print('')
    return 1

  return 0


if __name__ == '__main__':
  sys.exit(main())
