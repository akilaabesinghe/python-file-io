#! usr/bin/env python3

import re

pattern = r'herit'
re_pattern = re.compile(pattern,re.IGNORECASE)
#print(re_pattern)

print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening output.txt')
    with open('output.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            #all=re_pattern.findall(line)
            #all_lines=re_pattern.finditer(line)
            for finds in re_pattern.findall(line):
                out_stream.write('{0}\n'.format(finds))
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('output.txt is closed?', out_stream.closed)
