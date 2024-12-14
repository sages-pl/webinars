from ninja import Router
from .models import Product
from .schemas import ProductSchema


router = Router()

@router.get('/products', response={
    200: list[ProductSchema],
})
def list_products(request):
    return Product.objects.all()
