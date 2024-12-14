from ninja import Router
from ninja.pagination import paginate
from .models import Product
from .schemas import NotFound, ProductSchema


router = Router()

@router.get('/products', response={
    200: list[ProductSchema]})
@paginate
def list_products(request):
    return Product.objects.all()


@router.get('/products/{product_id}', response={
    200: ProductSchema,
    404: NotFound})
def get_product(request, product_id: int):
    try:
        product = Product.objects.get(id=product_id)
        return 200, product
    except Product.DoesNotExist:
        return 404, {'details': 'Product not found'}
