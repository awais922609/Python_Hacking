import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_2022580.html"  # Fixed missing colon (:)

try:
    html = urllib.request.urlopen(url).read().decode()  # Decode to string
except urllib.error.URLError as e:
    print(f"Error opening URL: {e}")
    exit(1)
    
soup = BeautifulSoup(html, 'html.parser')
# Find all anchor tags with class="comments" to target comments specifically
comments = soup('span')
print(comments)
# Initialize sum to 0 before the loop
sum_val = 0

for comment in comments:
    # Extract integer value from comment text
    try:
        comment_text = comment.string.strip()  # Get string content and strip whitespace
        print("In here")
        comment_value = int(comment_text)
        sum_val += comment_value
    except ValueError:
        print(f"Skipping invalid comment: {comment_text}")

print("Sum of comment integers:", sum_val)
