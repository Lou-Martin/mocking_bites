# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.library = {}

    def add(self, track):
        self.library.update({track.title:track.artist})
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing


    def search(self, keyword):
        matching_tracks = {}

        for key, value in self.library.items():
                
                if keyword in key:
                    matching_tracks[key] = value
            
                elif keyword in value:
                    matching_tracks[key] = value

        return matching_tracks