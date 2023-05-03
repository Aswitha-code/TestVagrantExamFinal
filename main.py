#python code to play the songs based on the user
# and eliminate the least recently played songs when the store becomes full.


class SongStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.head = None
        self.tail = None

    def get(self, user):
        if user not in self.store:
            return None

        node = self.store[user]
        if node != self.head:
            self._remove(node)
            self._set_head(node)
        return node.song

    def put(self, user, song):
        if user in self.store:
            node = self.store[user]
            node.song = song
            if node != self.head:
                self._remove(node)
                self._set_head(node)
        else:
            node = Node(user, song)
            self.store[user] = node
            if len(self.store) > self.capacity:
                del self.store[self.tail.user]
                self._remove(self.tail)
            self._set_head(node)

    def _remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def _set_head(self, node):
        node.prev = None
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node


class Node:
    def __init__(self, user, song):
        self.user = user
        self.song = song
        self.prev = None
        self.next = None

#created an object SongStoreObject for different users and songs they are playing
SongStoreObject = SongStore(3)

SongStoreObject.put("Ashwi","s1")
SongStoreObject.put("Ashwi","s2")
SongStoreObject.put("Ashwi","s3")
SongStoreObject.put("Ashwi","Faded")

SongStoreObject.put("Nani","s1")
SongStoreObject.put("Nani","s2")
SongStoreObject.put("Nani","s3")
SongStoreObject.put("Nani","Perfect")

recent_song_for_user1 = SongStoreObject.get("Ashwi")
recent_song_for_user2 = SongStoreObject.get("Nani")
print("Recent Songs for user1: ",recent_song_for_user1)
print("Recent Songs for user2: ",recent_song_for_user2)
