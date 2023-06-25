<<<<<<< HEAD
import re

valid_urls = []
pattern = r'(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*\.[a-z]+(\.[a-z]+)*)'

text = input()
while text:
    match = re.search(pattern, text)

    if match:
        url = match.groups()
        valid_urls.append(url[0])

    text = input()

for valid_url in valid_urls:
    print(valid_url)

=======
import re

valid_urls = []
pattern = r'(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*\.[a-z]+(\.[a-z]+)*)'

text = input()
while text:
    match = re.search(pattern, text)

    if match:
        url = match.groups()
        valid_urls.append(url[0])

    text = input()

for valid_url in valid_urls:
    print(valid_url)

>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
