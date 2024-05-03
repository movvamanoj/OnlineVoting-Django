# settings.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Other settings...

STATIC_URL = '/static/'

# Set the STATIC_ROOT to a directory where you want to collect static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Change 'staticfiles' to the desired directory name
