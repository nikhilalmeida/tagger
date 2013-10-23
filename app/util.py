"""Utils library for data pull"""
import hashlib
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