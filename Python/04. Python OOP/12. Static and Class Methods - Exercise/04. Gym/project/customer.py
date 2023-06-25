class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()                                # викаме def get_next_id()

        Customer.id += 1                                            # увеличаваме клас атрибута с едно за всяка инстанция, която се създава.
                                                                    # При първото инициализиране id ще стане 2 и следващия
                                                                    # обект ще бъде с id 2 и т.н.

    @staticmethod
    def get_next_id():
        return Customer.id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
