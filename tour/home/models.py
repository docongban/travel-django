from django.db import models

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key = 'true')
    cat_name = models.CharField(max_length=50, null= False)
    cat_image = models.CharField(max_length=255)
    cat_description = models.TextField()
    class Meta:
        db_table = 'category'


class Product(models.Model):
    list_category = Category.objects.all()

    result = []
    for i in list_category:
        result.append(
            (i.cat_id, i.cat_name)
        )

    pro_id = models.AutoField(primary_key = 'true')
    pro_name = models.CharField(max_length=255, null=False)
    cat_id = models.IntegerField(null=False)
    pro_image = models.CharField(max_length=255, null=False)
    pro_price = models.FloatField(null=False)
    description = models.TextField(null=False)
    class Meta:
        db_table = 'product'
