from django.core.management.base import BaseCommand 
from pages.factories import ProductFactory 
from pages.factories import CommentFactory
class Command(BaseCommand): 
    help = 'Seed the database with products' 
    help = 'Seed the database with comments'
    def handle(self, *args, **kwargs): 
        ProductFactory.create_batch(8) 
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))

        CommentFactory.create_batch(4)
        self.stdout.write(self.style.SUCCESS('Successfully seeded comments'))