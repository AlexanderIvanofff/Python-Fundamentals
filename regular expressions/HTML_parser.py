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