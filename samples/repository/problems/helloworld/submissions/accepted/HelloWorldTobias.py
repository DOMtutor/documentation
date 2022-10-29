#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case_number in range(1, case_count + 1):
        name = sys.stdin.readline().strip()
        print("Case #{0}: Hello {1}!".format(case_number, name))
