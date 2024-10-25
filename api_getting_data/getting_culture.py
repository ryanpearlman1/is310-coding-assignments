import requests
import json
from googleapiclient.discovery import build
import apikey

youtube_api_key = apikey.load("youtube_api_key")
europeana_api_key = apikey.load("europeana_api_key")

def get_youtube_video_titles(search_term, api_key, max_results=10):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(q=search_term, part='snippet', maxResults=max_results, type='video')
    response = request.execute()
    return [item['snippet']['title'] for item in response['items']]

def get_europeana_titles(search_term, api_key, max_results=10):
    url = 'https://api.europeana.eu/record/v2/search.json'
    params = {'query': search_term, 'wskey': api_key, 'start': 1, 'rows': max_results}
    response = requests.get(url, params=params)
    return [item['title'][0] for item in response.json().get('items', []) if 'title' in item]

if __name__ == "__main__":
    search_term = input("Enter a search term: ")
    
    youtube_titles = get_youtube_video_titles(search_term, youtube_api_key)
    europeana_titles = get_europeana_titles(search_term, europeana_api_key)
    
    print("YouTube Video Titles:")
    for title in youtube_titles:
        print(title)

    print("\nEuropeana Titles:")
    for title in europeana_titles:
        print(title)

    combined_data = {'YouTube': youtube_titles,'Europeana': europeana_titles}

    with open('youtube_europeana.json', 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)
    print("Data saved to youtube_europeana.json")