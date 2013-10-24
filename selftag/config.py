"""
You can store your app's configuration settings here.

"""
# SECRET_KEY = '\xfb\xd3\xc1$\xa1^\xfa\xa8\xac4\xed\x02s>\xa6\xe2M\x85\xd9\xee\x85p\xb9\xdd'
# DEBUG=True
# CSRF_ENABLED=True
# CSRF_SESSION_LKEY='dev_key_h8asSNJ9s9=+'

from os.path import dirname, realpath, join


DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

tagger_root = dirname(dirname(realpath(__file__)))

csv_read_file = join(tagger_root, 'test_read.txt')
csv_write_file = join(tagger_root, 'test_write.txt')