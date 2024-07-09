import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error


def count_elements_in_xml(url):
  """
    Fetches an XML document from a URL, counts the occurrences of the element named "count",
    and returns the total count.

    Args:
        url (str): The URL of the XML document.

    Returns:
        int: The total number of elements named "count" in the XML document, or 0 if an error occurs.
    """

  try:
    # Fetch the XML data from the URL
    data = urllib.request.urlopen(url).read().decode()

    # Parse the XML data using ElementTree
    tree = ET.fromstring(data)

    # Find all elements named "count" using XPath
    counts = tree.findall(".//count")

    # Calculate the total count (handle potential exceptions)
    total_count = 0
    for item in counts:
      try:
        total_count += int(item.text)  # Directly access text content for efficiency
      except ValueError:
        print(
            f"Error: Encountered non-numeric value in 'count' element at '{item.attrib.get('path', '<unknown path>')}'"
        )

    return total_count

  except (urllib.error.URLError, ET.ParseError) as e:
    print(
        f"Error: An error occurred while processing the URL or XML data: {e}")
    return 0


if __name__ == "__main__":
  input_url = input("Enter URL of the XML document: ")
  total_count = count_elements_in_xml(input_url)

  if total_count > 0:
    print(
        f"The XML document contains a total of {total_count} 'count' elements."
    )
  else:
    print("No 'count' elements found in the XML document.")
