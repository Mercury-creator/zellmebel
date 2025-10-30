from django.db import models

class Category(models.Model):
    #Categories
    name = models.CharField("Категория", max_length=150)
    poster = models.ImageField("Постер", upload_to="category_poster/")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Furniture(models.Model):
    name = models.CharField("Имя", max_length=150)
    poster = models.ImageField("Постер", upload_to="furni_poster/")
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебели"
        
class AdditionalImages(models.Model):
    title = models.CharField("", max_length=160)
    description = models.TextField("")
    image = models.ImageField("", upload_to="additional_furni/")
    furniture = models.ForeignKey(Furniture, verbose_name="", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Даполнительный изображение"
        verbose_name_plural = "Даполнительный изображении"