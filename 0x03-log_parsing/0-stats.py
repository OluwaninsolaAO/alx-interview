#!/usr/bin/python3
"""0. Log parsing"""
import sys


class TrackLog:
    """Keep tracks of log size and status codes"""

    def __init__(self) -> None:
        """Initializes TrackLog"""
        self._size = 0
        self._status = {}

    def add(self, status: str, size: str) -> None:
        """Updates log metrics"""
        try:
            status = int(status)
            size = int(size)
        except:
            return
        arr = [200, 301, 400, 401, 403, 404, 405, 500]
        if status not in arr:
            return
        if not self._status.get(status, None):
            self._status.update({status: 1})
        else:
            self._status.update({status: self._status.get(status) + 1})
        self._size += int(size)

    def print(self) -> None:
        """Prints Log metrics"""
        print('File size: {}'.format(self._size))

        arr = list(self._status.items())
        arr.sort()

        for status, counts in arr:
            print('{}: {}'.format(status, counts))


log = TrackLog()
DEFAULT_COUNT = 10
log_interval = DEFAULT_COUNT

try:
    for line in sys.stdin:
        log.add(*(line.split()[-2:]))
        if log_interval == 1:
            log_interval = DEFAULT_COUNT
            log.print()
        else:
            log_interval -= 1
except KeyboardInterrupt:
    log.print()
    raise
