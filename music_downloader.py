"""
This module automatically searches for music on YouTube, downloads it and adds it to the Library
"""

import youtube_dl

from library import Library
from api_key import api_key as API_KEY

MUSIC_CATEGORIES = ['Entertainment', 'Music']


class Downloader:
    def __init__(self, library):
        self.library = library

    def download_songs(self, song_urls):
        def check_if_music(categories):
            for category in categories:
                if category in MUSIC_CATEGORIES:
                    return True
            return False  # Should probably see if this will be a problem before fixing it

        if not isinstance(song_urls, list):
            song_urls = [song_urls]

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filenames = []
            for url in song_urls:
                info = ydl.extract_info(url, download=True)

                filenames.append(
                    "{TITLE}.{EXTENSION}".format(
                        TITLE=info['title'],
                        EXTENSION="mp3",
                    )
                )

        return filenames

    def find_new_song(self):
        # TODO: Implement a pseudo-random way of getting new songs
        return "https://www.youtube.com/watch?v=PUTctm9j3ZE"

if __name__ == '__main__':
    library = Library()
    downloader = Downloader(library)

    songs = [
        "https://www.youtube.com/watch?v=tzwJGOx8EYA",
        "https://www.youtube.com/watch?v=BGlTZp_mbRQ",
    ]
    print(downloader.download_songs(songs))
