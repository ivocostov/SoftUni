<<<<<<< HEAD
article_title = input()
article_content = input()
temporary = ''
html_list = ''

while True:
    comment = input()
    if comment == 'end of comments':
        break
    current_comment = comment

    for letter in current_comment:
        temporary += letter

    temp = f'<div>\n    {temporary}\n</div>\n'
    html_list += temp
    temporary = ''


print(f"<h1>\n"
      f"    {article_title}\n"
      f"</h1>\n"
      f"<article>\n"
      f"    {article_content}\n"
      f"</article>\n"
      f"{html_list}")
=======
article_title = input()
article_content = input()
temporary = ''
html_list = ''

while True:
    comment = input()
    if comment == 'end of comments':
        break
    current_comment = comment

    for letter in current_comment:
        temporary += letter

    temp = f'<div>\n    {temporary}\n</div>\n'
    html_list += temp
    temporary = ''


print(f"<h1>\n"
      f"    {article_title}\n"
      f"</h1>\n"
      f"<article>\n"
      f"    {article_content}\n"
      f"</article>\n"
      f"{html_list}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
