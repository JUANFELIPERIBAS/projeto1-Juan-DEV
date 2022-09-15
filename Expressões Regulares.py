# Expressões Regulares
# Dev: Juan Felipe Ribas
# Data: 04.09.22

import re

result = re.match('AV', 'AV Analytics Video AT')
print(result)

result = re.match('AV', 'AV Analytics Video AV')
print(result.group(0))

result = re.match('Analytics', 'AV Analytics Video AV')
print(result)

result = re.search('StackX', 'AV Analytics StackX AV')
print(result.group(0))

result = re.findall('AV', 'AV Analytics Video AV')
print(result)

result = re.split('i', 'Analytics Video')
print(result)

result = re.split('i', 'Analytics video é muito legal', maxsplit=1)
print(result)

result=re.sub('da India','do Mundo','AV é a maior comunidade de Analytics da India')
print(result)

pattern = re.compile('AV')
result = pattern.findall('AV Analytics Video AV')
print(result)
result2 = pattern.findall('AV é a maior comunidade de Analytics da India')
print(result2)

result=re.findall('.', 'AV é a maior comunidade de Analytics da India')
print(result)

result=re.findall('\w', 'AV é a maior comunidade de Analytics da India')
print(result)

li=['9999999999','999999-999','99999x9999']
for val in li:
    if re.match(r"[8-9]{1}[0-9]{9}", val) and len(val) == 10:
        print('sim')
    else:
        print('não')