from django.db import models


class Category(models.Model):
    """
        Модель категории
    """
    name = models.SlugField(primary_key=True, unique=True, max_length=50)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name


class Product(models.Model):  # Родион
    """
        модель продукта
    """
    owner = ...
    category = ...
    title = ...
    price = ...
    image = ...
    created_at = ...