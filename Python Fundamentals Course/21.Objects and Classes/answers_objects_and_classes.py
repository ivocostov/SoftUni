# Party
class Person:
    def __init__(self, name):
        self.name = name


class Party:

    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def name_of_attendees(self):
        return ', '.join([person.name for person in self.people])

    def number_of_guests(self):
        return len(self.people)


party = Party()

while True:
    command = input()

    if command == 'End':
        break

    name = command
    person = Person(name)
    party.invite(person)

print(f"Going: {party.name_of_attendees()}")
print(f"Total: {party.number_of_guests()}")


# Comment
class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


# Emails
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()

    if command == 'Stop':
        break

    sender, receiver, content = command.split(' ')
    email = Email(sender, receiver, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(', ')]

for email in emails:
    print(email.get_info())


# 5
class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.radius

    def calculate_area(self):
        return Circle.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle):
        return Circle.__pi * self.radius * self.radius * (angle / 360)


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")