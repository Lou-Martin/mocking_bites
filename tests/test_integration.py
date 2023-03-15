from lib.music_library import MusicLibrary
from lib.track import Track

'''

given an instance of "Track"
add track to music_library

'''

def test_add_one_track():
    todays_music = MusicLibrary()
    track_one = Track("Moth Grinder", "Grim Salvo")
    todays_music.add(track_one)
    assert todays_music.library == {"Moth Grinder" : "Grim Salvo"}

'''

given two instances of track
add tracks to music_library

'''

def test_add_two_tracks():
    todays_music = MusicLibrary()
    track_one = Track("Moth Grinder", "Grim Salvo")
    track_two = Track("OBLITERATION", "Killstation")
    todays_music.add(track_one)
    todays_music.add(track_two)
    assert todays_music.library == {"Moth Grinder" : "Grim Salvo", "OBLITERATION" : "Killstation"}

'''

given several tracks and a search keyword
return tracks that have keyword in title or artist (search by partial title)

'''

def test_search_with_two_tracks():
    todays_music = MusicLibrary()
    track_one = Track("Moth Grinder", "Grim Salvo")
    track_two = Track("OBLITERATION", "Killstation")
    todays_music.add(track_one)
    todays_music.add(track_two)
    assert todays_music.search('Moth Grinder') == {"Moth Grinder": "Grim Salvo"}


'''

given several tracks and a search keyword
return tracks that have keyword in title or artist (search by partial artist)

'''


def test_search_with_two_tracks_by_partial_artist():
    todays_music = MusicLibrary()
    track_one = Track("Moth Grinder", "Grim Salvo")
    track_two = Track("OBLITERATION", "Killstation")
    todays_music.add(track_one)
    todays_music.add(track_two)
    assert todays_music.search('Kills') == {"OBLITERATION": "Killstation"}

'''

given multiple tracks that meet search criteria
return list of matching tracks and artist

'''

def test_search_with_three_tracks_with_two_matches():
    todays_music = MusicLibrary()
    track_one = Track("Moth Grinder", "Grim Salvo")
    track_two = Track("OBLITERATION", "Killstation")
    track_three = Track("Moth Kills", "David Bowie")
    todays_music.add(track_one)
    todays_music.add(track_two)
    todays_music.add(track_three)
    assert todays_music.search('Kills') == {"OBLITERATION": "Killstation", "Moth Kills": "David Bowie"}