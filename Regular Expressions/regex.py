import urllib.request, urllib.parse, urllib.error
import re

def get_allLinks(url):
  try:  
    fhand=urllib.request.urlopen(url)
  except urllib.error.URLError as e:
    print("Error Opening Url {url} ({e})")
    return
  for line in fhand:
    line=line.decode().strip()
    match = re.search('href="([^"]+)"',line)
    if match:
      extracted_url=match.group(1)
      if extracted_url.startswith('http'):
        if extracted_url not in urls:
          urls.append(extracted_url)
        
        
        
fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

  