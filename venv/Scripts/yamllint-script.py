#!c:\users\yraji\desktop\chatbotv2\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'yamllint==1.26.1','console_scripts','yamllint'
__requires__ = 'yamllint==1.26.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('yamllint==1.26.1', 'console_scripts', 'yamllint')()
    )
