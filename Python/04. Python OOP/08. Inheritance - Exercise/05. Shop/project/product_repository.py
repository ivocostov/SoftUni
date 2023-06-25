from typing import List
from MainProblem.project import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for current_product in self.products:
            if current_product.name == product_name:
                return current_product

    def remove(self, product_name):
        self.products.remove(product_name)

    def __repr__(self):
        return '\n'.join([f"{p}: {p.quantity}" for p in self.products])