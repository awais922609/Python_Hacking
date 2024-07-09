import urllib.request
import json
import urllib.parse

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
  location = input("Enter location: ")
  if len(location) < 1: break

  # URL encode the location
  encoded_location = urllib.parse.urlencode({'q': location})

  # Build the full URL
  url = serviceurl + encoded_location

  print('Retrieving', url)
  uh = urllib.request.urlopen(url).read()
  data = uh.decode('utf-8')
  print('Retrieved', len(data), 'characters')

  try:
    js = json.loads(data)
    print(data)
    # Extract plus code (assuming 'plus_code' is the key)
    plus_code = js['results'][0]['plus_code']
    print('\n\nPlus code', plus_code)
  except:
    print('==== Failure To Parse JSON ====')

print('Done.')
