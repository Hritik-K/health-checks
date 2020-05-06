#!/usr/bin/env python3

import os
import sys

def check_reboot_required():
  return os.path.exists('/run/reboot-required')

def main():
  if check_reboot_required():
    print('pending reboot')
    sys.exit(1)
  print('everything ok')
  sys.exit(0)

main()
