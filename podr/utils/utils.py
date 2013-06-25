from datetime import datetime


DATE_FORMAT_CODES = ['%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z']


def to_seconds(timestr):
    seconds= 0
    for part in timestr.split(':'):
        seconds = seconds*60 + int(part)
    return seconds


def getDatetime(datestring):
    result = datetime.now()

    for code in DATE_FORMAT_CODES:
        try:
            result = datetime.strptime(datestring, code)
            return result
        except ValueError:
            continue
    return result
