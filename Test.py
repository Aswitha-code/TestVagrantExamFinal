#test cases are written here

from main import SongStore
def test_SongStore():
    SongStoreObject2 = SongStore(3)
    assert SongStoreObject2.get("Srinu") == None

    SongStoreObject2.put("Srinu", "song1")
    assert SongStoreObject2.get("Srinu") == "song1"

    SongStoreObject2.put("Srinu", "song2")
    assert SongStoreObject2.get("Srinu") == "song2"

    SongStoreObject2.put("Nihan", "song3")
    assert SongStoreObject2.get("Nihan") == "song3"

    SongStoreObject2.put("Srikanth", "song4")
    assert SongStoreObject2.get("Srikanth") == "song4"

    assert SongStoreObject2.get("Srinu") == None # Srinu is least recently used, should be removed from the SongStoreObject2

    SongStoreObject2.put("Srikanth", "song5") # Srikanth is already in the SongStoreObject2, should update song5 for Srikanth
    assert SongStoreObject2.get("Srikanth") == "song5"

    SongStoreObject2.put("Sai", "song6") # SongStoreObject2 is full, Nihan is least recently used, should be removed from the SongStoreObject2
    assert SongStoreObject2.get("Nihan") == None

#Invoking the test cases function
test_SongStore()