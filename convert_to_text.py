import urllib.request
import html2text





url = 'https://www.cbc.ca/radiointeractives/thecurrent/death-of-a-hostage-taker'

response = urllib.request.urlopen(url)

webContent = str(response.read(), 'utf-8')

f = open('article.html', 'w')
f.write(webContent)
f.close()

r = open('article.html', 'r')

print(html2text.html2text(r.read()))


