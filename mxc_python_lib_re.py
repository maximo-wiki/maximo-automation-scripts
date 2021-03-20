# Maximo Python/Jython script example to import re Python library
# and use re to replace square brackets with a number between e.g. [1] in a string with an empty string
# https://maximo.wiki @MaximoWiki March 2020

from java.lang import System
import sys

service.log(scriptName + '  ' + str(sys.path))

# Required : Appending to sys.path to refer to python libraries 
if sys.path.count('__pyclasspath__/Lib') == 1:
 service.log('\nPath to /Lib already exists\n')
else :
 service.log('\nExtend path to /Lib \n')
 sys.path.append('__pyclasspath__/Lib')

import re

service.log(scriptName + ' [START]')

find = r'\[\d\]'
replace = ''
text = 'text [1]'
service.log(scriptName + ' ' + text)

text = re.sub(find, replace, text)

service.log(scriptName + ' ' + text)

service.log(scriptName + ' [END]')
