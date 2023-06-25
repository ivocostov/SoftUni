class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property                     # getter
    def username(self):
        return self.__username    # това тук взима username

    @username.setter              # setter
    def username(self, value):         # този ред взима username и го подава на проверката отдолу
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        error_message = "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."

        if len(value) < 8:
            raise ValueError(error_message)

        elif value.lower() == value:           #проверява дали има поне една главна буква в паролата
            raise ValueError(error_message)

        elif not [s for s in value if s.isdigit()]:   # проверява дали има поне една цифра в паролата
            raise ValueError(error_message)

        self.__password = value


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'




# profile_with_invalid_password = Profile('My_username', 'My-password')
# print(profile_with_invalid_password)
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# print(profile_with_invalid_username)
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
