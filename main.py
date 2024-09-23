
from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth


user_input = input("Which year will you like to travel to? Type the date in this format YYYY-MM-DD:\n")
CLIENT_ID = "67e70f01c4f443c98455190290524c88"
CLIENT_SECRET = "b6eeddce3c834268b8cf0c9537cbb76b"
user_id = "Kobby24"


# user_input = "2020-02-11"

url = f"https://www.billboard.com/charts/hot-100/{user_input}"
response = requests.get(url=url)
response_text = response.text
print(response_text)

# soup = BeautifulSoup(response_text, "lxml")
#
# top_100_ = soup.select("li ul li h3")
# top_100_list = [i.getText().strip() for i in top_100_]
# print(top_100_list)
#
# scope = "user-library-read playlist-modify-public playlist-modify-private playlist-read-private"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username="Kobby24",scope=scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri="http://example.com",))
#
# results = sp.current_user()["id"]
# print(results)
#
# song_urls = [sp.search(q=track)["tracks"]["items"][0]["external_urls"]["spotify"] for track in top_100_list]
#
# print(song_urls)
# creat_pl = sp.user_playlist_create(user=results,name=f"{user_input}Billboard 100",public=True,collaborative=False,
#                                    description="Top 100")
# creat_pl_id = creat_pl["id"]
# add_trcks = sp.playlist_add_items(playlist_id=creat_pl_id,items=song_urls,position=None)
#
# print(creat_pl)
# print(creat_pl_id)
# print(add_trcks)