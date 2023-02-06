from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic


URL = "https://www.billboard.com/charts/hot-100/"
DATE = "2012-06-12"

response = requests.get(url=f"{URL}{DATE}/")
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
song_titles = [song.getText().strip('\n\n\t\n\t\n\t\t\n\t\t\t\t\t').strip('\t\t\n\t\n') for song in soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
song_artists = [song_artist.getText().strip('\n\t\n\t').strip('\n') for song_artist in soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]

yt = YTMusic("headers_auth.json")
playlistId = yt.create_playlist('test', 'test description')

for i in range(len(song_titles) - 1):
    search_results = yt.search(f'{song_titles[i]} {song_artists[i]}')
    if 'videoId' in search_results[0]:
        yt.add_playlist_items(playlistId, [search_results[0]['videoId']])
    else:
        continue
