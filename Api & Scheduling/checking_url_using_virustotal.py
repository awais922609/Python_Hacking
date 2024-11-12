import requests
import base64
import pandas as pd

def check_url(url):
    # Base64 encode the URL and decode it to a string, removing any padding "=" characters
    url_encoded = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    api_key = "<virustotal_key>"  # Replace with your actual VirusTotal API key
    endpoint = f"https://www.virustotal.com/api/v3/urls/{url_encoded}"
    headers = {"x-apikey": api_key}

    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()

        # Extract 'last_analysis_stats' and display as a pandas Series
        stats = data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})
        print("Analysis Summary:")
        print(pd.Series(stats))
        print("\n")

        # Extract 'last_analysis_results' and display as a pandas DataFrame
        analysis_results = data.get('data', {}).get('attributes', {}).get('last_analysis_results', {})
        if analysis_results:
            df = pd.DataFrame.from_dict(analysis_results, orient='index')
            print("Per Engine Analysis Results:")
            print(df[['category', 'result']])
        else:
            print("No analysis results found.")
    else:
        print("Error:", response.status_code, response.text)

# Example usage
check_url("https://eicar.com")
