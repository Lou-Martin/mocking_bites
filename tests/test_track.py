from lib.track import Track
from unittest.mock import Mock

'''

given a track object and search keyword
return bool if objects match keyword string

'''

def test_matches_given_track_partial():
    fake_track = Track('Fake Song', 'Fake Artist')
    assert fake_track.matches('Fake') == True

'''

given a track object and search keyword for artist
return bool if objects match keyword string

'''

def test_matches_given_track_artist():
    fake_track = Track('Fake Song', 'Fake Artist')
    assert fake_track.matches('Artist') == True

'''

given a track object and search keyword
return False if object doesnt match keyword string

'''

def test_matches_false_given_track_artist():
    fake_track = Track('Fake Song', 'Fake Artist')
    assert fake_track.matches('Shiba') == False
