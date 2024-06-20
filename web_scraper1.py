import urllib.request, urllib.parse, urllib.error
import re

def get_all_links(url, max_depth=15):
    

    urls = set()  # Use a set to store unique URLs

    def parser(url_val):
  
        try:
            fhand = urllib.request.urlopen(url_val)
        except urllib.error.URLError as e:
            print(f"Error opening URL: {url_val} ({e})")
            return

        for line in fhand:
            line = line.decode().strip()
            match = re.search('<a[^>]+href="([^"]+)"[^>]*>', line)
            if match:
                extracted_url = match.group(1)

                # Check for absolute URLs
                if extracted_url.startswith('http'):
                    if extracted_url not in urls and max_depth > 0:
                        urls.add(extracted_url)
                        parser(extracted_url)  # Recursive call (avoid infinite recursion)
                else:
                    # Handle relative URLs (construct full URL)
                    full_url = urllib.parse.urljoin(url_val, extracted_url)
                    if full_url not in urls and max_depth > 0:
                        urls.add(full_url)
                        parser(full_url)

    parser(url)  # Initiate the recursive link extraction
    return list(urls)  # Convert the set back to a list

if __name__ == "__main__":
    starting_url = 'http://www.dr-chuck.com/page1.htm'
    max_depth = 3  # Adjust the maximum depth as needed
    all_links = get_all_links(starting_url, max_depth)
    print("Extracted links (up to", max_depth, "levels deep):")
    for link in all_links:
        print(link)
