import vlc
import time

from library import Library


class Player:
    def __init__(self, library):
        self.media = None

        self.library = library

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play(self, song):
        self.media = self.instance.media_new(song)
        self.player.set_media(self.media)

        if self.player.play() == -1:
            raise ValueError("Couldn't play song!")
        else:
            print("Playing {SONG}".format(SONG=song))

        while self.player.get_state() != vlc.State.Ended:
            pass

        return True


if __name__ == '__main__':
    library = Library()
    player = Player(library)
    player.play("18V_Cordless_Drill_High_Pitch.mp3")
