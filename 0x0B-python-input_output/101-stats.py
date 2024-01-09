#!/usr/bin/python3
import signal
import sys


def print_metrics(signum, frame):
    """Prints the metrics when interrupted by CTRL+C"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))


signal.signal(signal.SIGINT, print_metrics)

total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) >= 7:
            total_size += int(parts[-1])
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

        if i % 10 == 0:
            print_metrics(None, None)
except KeyboardInterrupt:
    pass
finally:
    print_metrics(None, None)
