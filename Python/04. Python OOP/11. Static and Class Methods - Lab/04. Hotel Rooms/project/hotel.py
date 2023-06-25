from typing import List
from MainProblem.project import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> str or None:
        room = next(filter(lambda r: r.number == room_number, self.rooms))  # преизползваме метода в Room, за да се опитаме да ги настаним в свободна стая, ако е такава
        result = room.take_room(people)                                     # метода в Room връща или str или None, ако върне None, значи стаята е заета и не може да се заеме
                                                                            # ако върне str, значи стаята е свободна и може да бъде заета
        if result:
            return result

        self.guests += people

    def free_room(self, room_number: int) -> str or None:
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        guests = room.guests
        result = room.free_room()

        if result:
            return result

        self.guests -= guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"

