from django.db import models

# Create your models here.
NULLBALE = {'null': True, 'blank':True}
class Category(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание',**NULLBALE)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['first_name']


class Product(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='products/',**NULLBALE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.category}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['first_name']