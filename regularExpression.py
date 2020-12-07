import re

patterns=['term1','term2']

text='This is a string with term1,not the other'

for pattern in patterns:
    print("I am searching for:"+pattern)

    if re.search(pattern,text):
        print("Match")
    else:
        print("No match")





text="012 term1"

match=re.search('term1',text)
print("Showing the index where term1 is available at:",match.start())




split_term='@'
email='user@gmail.com'

print(re.split(split_term,email))




print(re.findall('match','test phrase match in middle'))
