#!d:\learningcentre\python\flask\xinaero\aircadianebos_withaero\aircadianebos\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'openmdao==3.16.0','console_scripts','reset_notebook'
__requires__ = 'openmdao==3.16.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('openmdao==3.16.0', 'console_scripts', 'reset_notebook')()
    )
