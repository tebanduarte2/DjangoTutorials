import factory
from .models import Product, Comment
class ProductFactory(factory.django.DjangoModelFactory): 
    class Meta: 
        model = Product 
    name = factory.Faker('company') 
    price = factory.Faker('random_int', min=200, max=9000)

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment
    product = factory.SubFactory(ProductFactory)
    description = factory.Faker('text')
    