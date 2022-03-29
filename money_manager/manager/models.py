from django.db import models

# Create your models here.
'''MODEL CATEGORY
    id
    title
'''

class Category(models.Model):
    title = models.CharField(max_length=75, verbose_name="Category")


'''MODEL TRANSACTION
    id
    amount
    datatime
    user
    category
'''

class Transaction(models.Model):
    amount = models.IntegerField(verbose_name='Amount')
    datetime = models.DateTimeField
    user = models.CharField(max_length=50, verbose_name="UserID")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
