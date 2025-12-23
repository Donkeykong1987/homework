from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(
        upload_to='photos/',
        null=True,
        blank=True
    )
    owner_website = models.URLField(null=True, blank=True)
    is_available = models.BooleanField(null=True, blank=True)

    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand



    