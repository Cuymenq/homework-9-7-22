import re

with open("names.txt") as text: #names.txt should be in your project folder for your homework
    data = text.readlines()

# for item in data:
#     print(item)

# Generate the desired output. Hint: use an asterisk * in your re.compile()

title_pattern = re.compile('([\w]+)([A-Z][a-z]+)|([C][A-Z]+)|([A-Z][a-z]+ [A-Z][a-z]+ ,)')
find_titles = title_pattern.findall(str(data))
# print(find_names)


for title in find_titles:
    print(title[1]+title[2])

email_pattern = re.compile('([\w]+)@([a-z]+)(.com|.gov|.co.se|.co.uk)') # email validator

found_emails = email_pattern.findall(data[0])
# print(found_emails)

for i in range(11):
    found_emails = email_pattern.findall(data[i])
    print(found_emails[0][0] + '@' + found_emails[0][1] + found_emails[0][2])


