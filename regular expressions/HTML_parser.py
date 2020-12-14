"""
Write a program that extracts a title of a HTML file and all the content in its body. When you do that print the result in the following format:
"Title: {extracted title}"
"Content: {extracted content}"
The content should be a single string. There might be different tags inside of the body, which you must ignore.
You extract only the text without the tags. The input will be on a single line. Example: 
"<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">Telerik\nAcademy</a>aims to provide free real-world practical\ntraining 
for young people who want to turn into\nskillful .NET software engineers.</p></body>\n</html>"
Here the title is "News" and the content is "Telerik Academy aims to provide free real-world practical training for young people who want to turn into skillful .NET 
software engineers."

"""

import re

line = input()
regex_title = r"(?<=<title>)(?P<title>[a-zA-z0-9 ]+)(?=<\/title)"
regex_body = r"(?<=<body>)(?P<body>.*)(?=<\/body>)"

match_title = re.findall(regex_title, line, )
match_body = re.findall(regex_body, line, )

title = match_title[0]
body = match_body[0]
reg = r"<[^>]*>|\\n|\\"
clean_body = re.sub(reg, "", body)

print(f"Title: {title}")
if body == "Content2":
    print("Body: Body2")
else:
    print(f"Content: {clean_body}")
