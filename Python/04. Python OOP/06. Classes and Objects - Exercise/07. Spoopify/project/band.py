from typing import List
from MainProblem.project import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.attribute_albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.attribute_albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.attribute_albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."


    def remove_album(self, album_name: str):
        try:
            current_album = next(filter(lambda a: a.name == album_name, self.attribute_albums))

        except StopIteration:
            return f"Album {album_name} is not found."

        if current_album.published:
            return f"Album has been published. It cannot be removed."

        self.attribute_albums.remove(current_album)
        return f"Album {album_name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        [result.append(f"{b.details()}") for b in self.attribute_albums]

        return "\n".join(result)
