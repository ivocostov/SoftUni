from math import ceil



class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]   # прави матрица в обхвата на pages

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))             # получаваме броя на страниците според снимките и ги закръгляме
                                                                         # нагоре, защото ако се получи примерно 10 / 4 = 2.5, а знаем че
    def add_photo(self, label: str) -> str:                              # на страница са 4 снимки, то тогава ще ни трябват 3 страници
        for page in range(self.pages):                                   # 2 стр. * 4 снимки и на третата ще сложим 2
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_PER_PAGE:                 # сравнява се дължината на всеки списък който сме създали
                self.photos[page].append(label)                                     # с максимума снимки които могат да се съберат

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"  #  page + 1 защото страниците започват от 1
        return "No more free slots"                                                                          #  len(self.photos[page]) или дължината на текущия лист
                                                                                                             #  показва на коя позиция(slot) се намира снимката

    def display(self) -> str:
        result = ["-" * 11]                                             #  за първия ред от принта се създават 11 тирета в списък
                                                                        #  след това за всяка страница се създават толкова []
        for page in self.photos:                                        #  колкото снимки има на страницата (def add_photo())
            result.append(("[] " * len(page)).rstrip())                 #  и след това отново 11 тирета
            result.append("-" * 11)                                     # rstrip се слага за да махне празното място след последната кутийка

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
