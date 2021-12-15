from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        

    def __str__(self):
        return 'f{self.title}-{self.created_at}-{self.updated_at}'
    


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table  ='products'

    def __str__(self):
        return 'f{self.category}-{self.title}-{self.price}-{self.created_at}-{self.updated_at}'
    
