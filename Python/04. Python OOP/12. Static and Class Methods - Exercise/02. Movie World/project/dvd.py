from calendar import month_name


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):  # подава се date format => dd.mm.yy (всичко в числа), а горе в init месеца е str
        day, month, year = [int(x) for x in date.split('.')]

        return cls(name, id_number, year, month_name[month], age_restriction)        # библиотека month_name връща текст ако му подадеш число

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

