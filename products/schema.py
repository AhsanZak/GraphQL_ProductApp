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
    all_product_types = graphene.List(ProductTypes)
    all_categories = graphene.List(ProductCategory)
    all_brands = graphene.List(ProductBrand)

    @login_required
    def resolve_all_products(root, info):
        return Product.objects.all()
    
    @login_required
    def resolve_all_product_types(root, info):
        return ProductType.objects.all()
    
    @login_required
    def resolve_all_categories(root, info):
        return Category.objects.all()
    
    @login_required
    def resolve_all_brands(root, info):
        return Brand.objects.all()
    
    
class ProductMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        category = graphene.String(required=True)
        type = graphene.String(required=True)
        brand = graphene.String(required=True)

    product = graphene.Field(ProductDetails)

    @classmethod
    @login_required
    def mutate(cls, root, info, name, price, category, type, brand):
        category = Category.objects.get(name=category)
        product_type = ProductType.objects.get(name=type)
        brand = Brand.objects.get(name=brand)
        product = Product(name=name, category=category, product_type=product_type, brand=brand, price=price)
        product.save()
        return ProductMutation(product=product)

class BrandMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        
    brand = graphene.Field(ProductBrand)

    @classmethod
    @login_required
    def mutate(cls, root, info, name):
        brand = Brand(name=name)
        brand.save()
        return BrandMutation(brand=brand)

class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        
    category = graphene.Field(ProductCategory)

    @classmethod
    @login_required
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    create_product = ProductMutation.Field()
    create_brand = BrandMutation.Field()
    create_category = CategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)