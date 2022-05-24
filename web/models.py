
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify




class Update(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=500)
    date=models.DateField()
    image=VersatileImageField('Image',upload_to='updates/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    content=HTMLField(blank=True, null=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
        


class Countries(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = ("Countries")

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.OneToOneField(Category,on_delete=models.CASCADE)
    countries=models.ManyToManyField(Countries)
    quantity_in_TON=models.IntegerField()
    price=models.IntegerField()

    def get_countries(self):
        return ",".join ([str(p) for p in self.countries.all()])

    def __str__(self):
        return f"category = {self.category}, countries = {self.Countries.all()}"
   
