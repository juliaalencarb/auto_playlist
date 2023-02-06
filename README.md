# Automatic Top 100 Playlist

Create a playlist automatically on Youtube Music containing the top 100 songs for a chosen date.

---
## Contents

- Requirements
- Functions
- Installation and Usage

---
## Requirements

- Python 3.11 - [read more](https://www.python.org/downloads/release/python-3110/)
- bs4 module - [read more](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- requests module - [read more](https://pypi.org/project/requests/)
- ytmusicapi 0.25.0 - [read more](https://pypi.org/project/ytmusicapi/)

---
## Functions

- Scraps Billboard's "hot 100" webpage for a given date using Beautiful Soup 4,
- Integrates the YTMusic API to search all songs and create automatically a new playlist containing the referred songs.

--- 
## Installation and Usage

All modules previously described must be installed prior using this application.

The user can pick a date of their choice from January 1s 1955 to present.

In order to execute the script, the user must create a json file containing their authorization tokens to be passed as a request header. 

The creation of this json file is done automatically by the YTmusic module, as seen below:

<p align="center">
<img src="https://github.com/juliaalencarb/auto_playlist/blob/master/images/ytmusicapi_setup.png" width=75% height=75%>
</p>

Initialize python on the terminal by typing `python3` command. Then, import the YTMusic class from ytmusicapi module by entering `from ytmusicapi import YTMusic` on terminal.
Next, initiate the setup method from the YTMusic class by typing the `YTMusic.setup(filepath="headers_auth.json")` command. 
The program will ask the user to enter their request headers, which can be obtained using the developer tools. The user must make sure they are logged in.
Navigate to the Library page, on the top menu. Then, under the Network tab, search for an autheticated POST request filtering by `/browse`.
Next, copy and paste the headers onto the terminal (e.g. Authorization, Accept-Language, User-Agent, Cookie, X-Youtube-Client-Version, X-Youtube-Client-Name, X-Goog-AuthUser, X-Goog-Visitor-Id).
For more information, please refer to the ytmusicapi documentation [here](https://ytmusicapi.readthedocs.io/en/latest/setup.html).

A json file containing the user's authorization tokens will be created. 
Before executing the program, the user can also set the playlist title and description by altering the strings 'test' and 'test description', respectivelly, passed as paramaters on line 17.

<p align="center">
<img src="https://github.com/juliaalencarb/auto_playlist/blob/master/images/YTMusic_parameters.png" width=50% height=50%>
</p>

After all the setup is done, the user will be able to execute the script without errors. When the script is executed, the newly created playlist will appear on the user's library.
