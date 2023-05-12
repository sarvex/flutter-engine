#!/usr/bin/env python
# Copyright 2013 The Flutter Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import subprocess
import os
import sys


def main():
  parser = argparse.ArgumentParser(description='Package a Flutter application')

  parser.add_argument('--flutter-root', type=str, required=True,
                      help='The root of the Flutter SDK')
  parser.add_argument('--flutter-tools', type=str, required=True,
                      help='The executable for the Flutter tool')
  parser.add_argument('--asset-dir', type=str, required=True,
                      help='The directory where to put intermediate files')
  parser.add_argument('--app-dir', type=str, required=True,
                      help='The root of the app')
  parser.add_argument('--packages', type=str, required=True,
                      help='The package map to use')
  parser.add_argument('--manifest', type=str, help='The application manifest')
  parser.add_argument('--component-name', type=str, help='The name of the component')
  parser.add_argument('--asset-manifest-out', type=str,
                      help='Output path for the asset manifest used by the fuchsia packaging tool')

  args = parser.parse_args()

  env = os.environ.copy()
  env['FLUTTER_ROOT'] = args.flutter_root

  call_args = [
      args.flutter_tools,
      f'--asset-dir={args.asset_dir}',
      f'--packages={args.packages}',
  ]
  if 'manifest' in args:
    call_args.append(f'--manifest={args.manifest}')

  if args.asset_manifest_out:
    call_args.append(f'--asset-manifest-out={args.asset_manifest_out}')

  if args.component_name:
    call_args.append(f'--component-name={args.component_name}')

  return subprocess.call(call_args, env=env, cwd=args.app_dir)

if __name__ == '__main__':
  sys.exit(main())
