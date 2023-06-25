class Category:
    def __init__(self, category_id: int, name: str):
        self.id = category_id
        self.name = name

    def edit(self, new_name: str) -> str:
        self.name = new_name

        return self.name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
