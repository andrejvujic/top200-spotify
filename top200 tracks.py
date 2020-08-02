from bs4 import BeautifulSoup
import requests

URL = "https://spotifycharts.com/regional/global/weekly/latest"
KEY = "Ariana"

def find_singer(KEY):
	response = requests.get(URL)
	soup = BeautifulSoup(response.text, "lxml")

	positions = soup.findAll("td", class_ = "chart-table-position")
	songs_and_singers = soup.findAll("td", class_ = "chart-table-track")
	streams = soup.findAll("td", class_ = "chart-table-streams")

	songs_and_singers = [song_and_singer.text.strip().replace("\n", " ") for song_and_singer in songs_and_singers]
	for index, song_and_singer in enumerate(songs_and_singers):
		if KEY in song_and_singer:
			print(f"{positions[index].text}. {song_and_singer}\n{streams[index].text} streams\n")


find_singer(KEY)