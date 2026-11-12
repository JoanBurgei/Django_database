from django.db import models

CATEGORIES =[
    ('politics', 'Political categories'),
    ('technology', 'Technological categories'),
    ('sports', 'Sports categories'),
    ('Education', 'Educational categories'),
]
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORIES, max_length=100, null=True)
    year = models.IntegerField()
    cost = models.IntegerField()
    isbn = models.CharField(unique=True, max_length=15, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'books'

# python manage.py makemigrations
# python manage.py migrate