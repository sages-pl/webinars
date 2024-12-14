from ninja import Schema


class ProductSchema(Schema):
    id: int
    ean13: str
    name: str
    price: float