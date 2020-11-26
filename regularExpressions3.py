import re

def multi_re_find(pattern,phrase):
    for pat in pattern:
        f"Searching for pattern,{pat}"
        print(re.findall(pat,phrase))
        print('\n')


test_phrase='This is a string!But it has a punctuation.How can we remove it?'

test_patterns=['[^!.?]+']

multi_re_find(test_patterns,test_phrase)
