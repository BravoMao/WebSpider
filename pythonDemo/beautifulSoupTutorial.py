from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser")
#print(soup.prettify())
print(soup.title.string)

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match

html = """<div class="feeditemcontent cxfeeditemcontent">
<div class="feeditembodyandfooter">
<div class="feeditembody">
<span>The actual data is some where here</span>
</div>
</div>
</div>"""

soup = BeautifulSoup(html)

print soup.find_all(match_class(["feeditemcontent", "cxfeeditemcontent"]))

