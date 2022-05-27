
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
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    countries=models.ForeignKey(Countries,on_delete=models.CASCADE)
    price_for_one_TON=models.IntegerField()

    class Meta:
        unique_together = ('category','countries')

    def get_countries(self):
        return ",".join ([str(p) for p in self.countries.all()])


class Order(models.Model):
    ORDER_CHOICES = (('ACCEPTED','ACCEPTED'),('ORDER PROCESSING','ORDER PROCESSING'),('SHIPMENT PENDING','SHIPMENT PENDING'),('ESTIMATED DELIVERY','ESTIMATED DELIVERY'))
    track_number = models.CharField(max_length=128)
    customer_name = models.CharField(max_length=128)
    email = models.EmailField('customer email',blank=True, null=True)
    phone = models.CharField(max_length=128)
    from_address = models.TextField()
    to_address = models.TextField()
    status = models.CharField(max_length=128,default=True)


    def get_order_update(self):
        if OrderUpdate.objects.filter(order=self).exists():
            return OrderUpdate.objects.filter(order=self)
        else:
            return None

            
    def str(self):
        return str(self.track_number)
   


class Icon(models.Model):
    title=models.CharField(max_length=128)
    icon=VersatileImageField('Image',upload_to='icon/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return str(self.title)
        


class OrderUpdate(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    location = models.CharField(max_length=128) 
    comments = models.CharField(max_length=128)
    timestamp = models.DateTimeField()
    order_icon = models.ForeignKey(Icon,on_delete = models.CASCADE,blank=True,null=True)

    def str(self):
        return str(self.order)