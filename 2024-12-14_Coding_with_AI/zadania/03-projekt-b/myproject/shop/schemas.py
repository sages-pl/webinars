from ninja import Schema


class ProductSchema(Schema):
    id: int
    ean13: str
    name: str
    price: float


class NotFound(Schema):
    code: int = 404
    status: str = 'Not Found'
    details: str
