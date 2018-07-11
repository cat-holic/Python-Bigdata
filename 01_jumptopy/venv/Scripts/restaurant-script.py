#!C:\Python_Workspace\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'restaurant==0.1.0','console_scripts','restaurant'
__requires__ = 'restaurant==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('restaurant==0.1.0', 'console_scripts', 'restaurant')()
    )
