import vlc
import time


class Player:
    def __init__(self):
        self.media = None
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play(self, song):
        self.media = self.instance.media_new(song)
        self.player.set_media(self.media)
        if self.player.play() == -1:
            raise ValueError("Couldn't play song!")
        else:
            print("Playing {SONG}".format(SONG=song))


if __name__ == '__main__':
    player = Player()
    player.play("Beautiful Scarlet Rare Bird 1970.mp3")

    while True:
        pass
