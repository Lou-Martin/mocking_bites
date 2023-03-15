from lib.music_library import MusicLibrary
from unittest.mock import Mock

'''

using mocks as track objects (3)
return a list of objects that match keyword string
this test also encapsulates the add method

'''

def test_search_given_three_mock_tracks():
    library = MusicLibrary()

    fake_track = Mock()
    fake_track.artist = 'Fake Artist'
    fake_track.title = 'Fake Song'

    fake_track_two = Mock()
    fake_track_two.artist = 'Second Fake Artist'
    fake_track_two.title = 'Second Fake Song'

    fake_track_three = Mock()
    fake_track_three.artist = 'Third Fake Artist'
    fake_track_three.title = 'Third Fake Song'

    library.add(fake_track)
    library.add(fake_track_two)
    library.add(fake_track_three)

    assert library.search("Third") == {'Third Fake Song': 'Third Fake Artist'}

'''

using mocks as track objects (2)
add track to library
return library

'''

def test_add_given_two_mock_tracks():
    library = MusicLibrary()

    fake_track = Mock()
    fake_track.artist = 'Fake Artist'
    fake_track.title = 'Fake Song'

    fake_track_two = Mock()
    fake_track_two.artist = 'Second Fake Artist'
    fake_track_two.title = 'Second Fake Song'

    library.add(fake_track)
    library.add(fake_track_two)

    assert library.library == {'Fake Song': 'Fake Artist', 'Second Fake Song': 'Second Fake Artist'}
