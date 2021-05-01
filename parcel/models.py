from django.db import models
from django.utils.translation import gettext_lazy as _


class Merchant(models.Model):
    name = models.CharField(max_length=20, unique=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'Merchants'

    def __str__(self):
        return self.name


class Order(models.Model):
    class Location(models.TextChoices):
        IN_DHAKA = 'in_dhaka', _('Inside of Dhaka')
        OUT_DHAKA = 'out_dhaka', _('Outside of Dhaka')
        DIV_DHAKA = 'div_dhaka', _('Division of Dhaka')

    class ProductType(models.TextChoices):
        FRAGILE = 'fra', _('Fragile')
        LIQUID = 'liq', _('Liquid')

    class Quantity(models.TextChoices):
        TWO_KG = '2_kg', _('500 gm to 2 Kg')
        THREE_KG = '3_kg', _('3 Kg')
        FOUR_KG = '4_kg', _('4 Kg')
        FIVE_KG = '5_kg', _('5 Kg')

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant_order')
    product_type = models.CharField(max_length=10, choices=ProductType.choices, default=ProductType.FRAGILE)
    invoice_id = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=30, choices=Location.choices, default=Location.IN_DHAKA)
    quantity = models.CharField(max_length=50, choices=Quantity.choices, default=Quantity.TWO_KG)
    cost = models.PositiveIntegerField()
    order_datetime = models.DateField(auto_now_add=True, editable=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.invoice_id

    @property
    def calculated_charge(self):
        if self.location == 'div_dhaka':
            total = self.cost + (self.cost * 0.01) + (self.cost * 0.5)
            return total
        elif self.location == 'out_dhaka':
            total = self.cost + (self.cost * 0.01) + (self.cost * 0.5)
            return total
        else:
            return 'No Cod & Return Charge'
