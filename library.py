from collections import deque

QUEUE_MIN_LENGTH = 5


class Library:
    """The Library gets songs from Music Downloader and gives them to the Player
    """
    def __init__(self):
        # TODO: Pickle history periodically... maybe by making it a property...
        self.history = list()
        self.queue = deque()  # There should always be about 5 songs in the queue at a time

    def add_song(self, filename):
        if not self.is_repeat(filename):
            self.queue.append(filename)
        else:
            raise ValueError("This song has been played before!")

    def get_next_song(self):
        filename = self.queue.popleft()
        self.history.append(filename)  # I never forget a song

        return filename

    def is_repeat(self, filename):
        return filename in self.history

    @property
    def needs_more_songs(self):
        return len(self.queue) < QUEUE_MIN_LENGTH
