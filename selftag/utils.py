"""Utils library for data pull"""
import csv
import unicodedata
import sys


tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                    if unicodedata.category(unichr(i)).startswith('P'))


def normalize_word(text):
    """
    strip input string of any punctuations, make it lowercase and
    return a sha1 hash of the stripped text.
    """
    if text:
        stripped = "".join(unicode(text).translate(tbl).lower().split())
        return stripped


def list_to_csv(filename, list_data):
    with open(filename, 'wb') as fobj:
        writer = csv.writer(fobj, delimiter=',')
        for item in list_data:
            writer.writerow(item)


def csv_to_list(filename):
    with open(filename, 'rb') as fobj:
        reader = csv.reader(fobj, delimiter=',')
        result = []
        for field in reader:
            items = [field[0], field[1]]
            result.append([item.strip() for item in items])
        return result
        # return [[item.strip() for item in field] for field in reader
        #         if field]
