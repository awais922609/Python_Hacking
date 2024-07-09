import urllib.request
import urllib.error
import json

url = 'https://py4e-data.dr-chuck.net/comments_2022583.json'

# Fetch URL content using urllib.request
try:
  with urllib.request.urlopen(url) as response:
    data = response.read().decode('utf-8')  # Decode bytes to string

  # Parse JSON data
  data = json.loads(data)

  # Assuming 'comments' is a key with a list of comments
  if 'comments' in data:
    total_sum = sum(item['count'] for item in data['comments']
                    if 'count' in item)
    print('Total comment count:', total_sum)
  else:
    print("Couldn't find 'comments' key in data")

  # Handle potential errors (optional)
except urllib.error.URLError as e:
  print("Error fetching data:", e)
