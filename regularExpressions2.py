import re

def multi_re_find(pattern,phrase):
    for pat in pattern:
        f"Searching for pattern,{pat}"
        print(re.findall(pat,phrase))
        print('\n')


test_phrase='sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

# test_pattern=['sd*']
# test_pattern=['sd+']
# test_pattern=['sd?']
test_pattern=['sd{2,3}']
multi_re_find(test_pattern,test_phrase)
