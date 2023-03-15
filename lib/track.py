# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        # title and artist are both strings

    def matches(self, keyword):
        if keyword in self.title:
            return True
        elif keyword in self.artist:
            return True
        else:
            return False
        # keyword is a string
        # Returns true if the keyword matches either the title or artist