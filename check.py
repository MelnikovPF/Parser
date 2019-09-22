import urllib.request
response = urllib.request.urlopen('http://operline.ru')
print(response.read())

