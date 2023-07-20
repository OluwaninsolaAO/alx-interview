#!/usr/bin/python3
"""0. Log parsing"""
from sys import stdin, stdout
import re


class TrackLog:
    """Keep tracks of log size and status codes"""

    def __init__(self) -> None:
        """Initializes TrackLog"""
        self._size = 0
        self._status = {}

    def add(self, status: str, size: str) -> None:
        """Updates log metrics"""
        if not self._status.get(status, None):
            self._status.update({status: 1})
        else:
            self._status.update({status: self._status.get(status) + 1})
        self._size += int(size)

    def print(self) -> None:
        """Prints Log metrics"""
        # stdout.write('File size: {}\n'.format(self._size))
        print('File size: {}'.format(self._size))

        arr = list(self._status.items())
        arr.sort()

        for status, counts in arr:
            # stdout.write('{}: {}\n'.format(status, counts))
            print('{}: {}'.format(status, counts))


log = TrackLog()
DEFAULT_COUNT = 10
log_interval = DEFAULT_COUNT
log_pattern = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r' - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]'
    r' "(GET|POST|PUT|DELETE) (.+)" (\d{3}) (\d+)$'
)


try:
    for line in stdin:
        if re.match(log_pattern, line):
            log.add(*(line.split()[-2:]))
            if log_interval == 1:
                log_interval = DEFAULT_COUNT
                log.print()
            else:
                log_interval -= 1
except KeyboardInterrupt:
    log.print()
    raise
