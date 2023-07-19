#!/usr/bin/python3
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
        stdout.write('File size: {}\n'.format(self._size))
        for status, counts in self._status.items():
            stdout.write('{}: {}\n'.format(status, counts))


log = TrackLog()
DEFAULT_COUNT = 10
log_interval = DEFAULT_COUNT


try:
    for line in stdin:
        if re.match(r'^(\d+\.)+\d+ - \[.+] \".+\" \d{3} \d+$', line):
            log.add(*(line.split()[-2:]))
            if log_interval == 1:
                log_interval = DEFAULT_COUNT
                log.print()
            else:
                log_interval -= 1
except KeyboardInterrupt:
    log_interval = DEFAULT_COUNT
    log.print()
