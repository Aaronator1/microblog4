import os, sys

PROJECT_DIR = '/www/html/microblog4'

activate_this = os.path.join(PROJECT_DIR, 'venv/bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from microblog4 import app as application

