# Maximo Python/Jython script example to import re Python library
# and use re to replace square brackets with a number between e.g. [1] in a string with an empty string
# https://maximo.wiki @MaximoWiki March 2020 - Oct-2021

from java.lang import System
import sys

service.log(scriptName + '  ' + str(sys.path))

# Required : Appending to sys.path to refer to python libraries 
if sys.path.count('__pyclasspath__/Lib') == 1:
    service.log(scriptName + '> Path to /Lib already exists')
else :
    service.log('Extend path to /Lib ')
    sys.path.append(scriptName + '> __pyclasspath__/Lib')

import re

service.log(scriptName + '> [START]')

find = r'\[\d\]'
replace = ''
text = 'text [1]'
service.log(scriptName + '> text=' + text)
service.log(scriptName + '> replace=' + replace)

text = re.sub(find, replace, text)

service.log(scriptName + '> replaced text=' + text)

service.log(scriptName + '> [END]')
