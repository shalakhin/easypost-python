#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import tempfile
import time
import urllib2

import easypost

easypost.api_key = 'cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'
easypost.api_base = 'http://localhost:5000/v2'

def process_job(job):

    with tempfile.NamedTemporaryFile() as f:
        try:
            response = urllib2.urlopen(job['url'])
        except urllib2.URLError:
            return False

        f.write(response.read())
        f.flush()

        return print_zpl(f.name)

    #if success:


def print_zpl(file_path):
    print 'calling lpr...'

    exit_code = subprocess.call(
        [
            'lpr',
            '-o',
            'raw',
            file_path,
        ]
    )

    print 'got exit code %d!' % exit_code

    success = exit_code == 0

    return success
    #return exit_code == 0


if __name__ == '__main__':
    printer = easypost.Printer.retrieve("printer_pPmkSEU3")

    try:
        while True:
            print 'getting jobs'
            response = printer.get_jobs()
            print response

            # print 'saw %d jobs...' % len(response['print_jobs'])

            # for job in response['print_jobs']:
            result = process_job(response[0])
            print 'job finished with %s' % result

            print 'sleeping 1 second...'
            time.sleep(5)

    except KeyboardInterrupt:
        print 'bye bye!'

