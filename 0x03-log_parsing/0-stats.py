#!/usr/bin/python3
"""0. Log parsing"""
import sys

status_codes = {}
total_size = 0


def add(status: str, size: str) -> int:
    """Updates log metrics"""
    try:
        status = int(status)
        size = int(size)
    except:
        return 0
    arr = [200, 301, 400, 401, 403, 404, 405, 500]
    if status not in arr:
        return
    if not status_codes.get(status, None):
        status_codes.update({status: 1})
    else:
        status_codes.update({status: status_codes.get(status) + 1})
    return size


def print_log() -> None:
    """Prints Log metrics"""
    print('File size: {}'.format(total_size))
    arr = list(status_codes.items())
    arr.sort()
    for status, counts in arr:
        print('{}: {}'.format(status, counts))


DEFAULT_COUNT = 10
log_interval = DEFAULT_COUNT

try:
    for line in sys.stdin:
        total_size += add(*(line.split()[-2:]))
        if log_interval == 1:
            log_interval = DEFAULT_COUNT
            print_log()
        else:
            log_interval -= 1
except KeyboardInterrupt:
    print_log()
    raise
