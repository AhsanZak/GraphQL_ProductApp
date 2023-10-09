import graphene
from graphql_jwt.decorators import login_required
from graphene_django import DjangoObjectType
from .models import Product, Category, Brand, ProductType

    
class ProductDetails(DjangoObjectType):
    class Meta:
        model = Product
        field = ("name", "price")

class ProductTypes(DjangoObjectType):
    class Meta:
        model = ProductType
        field = ("name")

class ProductCategory(DjangoObjectType):
    class Meta:
        model = Category
        field = ("name")

class ProductBrand(DjangoObjectType):
    class Meta:
        model = Brand
        field = ("name")

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductDetails)

    @login_required
    def resolve_all_products(root, info):
        return Product.objects.all()
    

schema = graphene.Schema(query=Query)