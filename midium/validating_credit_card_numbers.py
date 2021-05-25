import re

for i in range(int(input())):
    input_str = input()
    if(re.match(r'^[456](\d{15}|\d{3}(-\d{4}){3})$', input_str) and not re.search(r'(\d)\1\1\1', re.sub('-', '', input_str))):
        print('Valid')
    else:
        print('Invalid')
