from django.db import models
from products.models import Product, Variation
from accounts.models import Account


#___________________________________________________________  Cart
class Cart(models.Model):
    '''
    Stores information about the user's shopping cart, including the cart ID and the date
    when it was added.
    '''
    cart_id     = models.CharField(max_length=250, blank=True)
    date_added  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

#___________________________________________________________  CartItem
class CartItem(models.Model):
    '''
    Stores information about an item added to a shopping cart, including the associated
    user, product, variations, cart, quantity, and whether the item is active.
    '''
    user        = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations  = models.ManyToManyField(Variation, blank=True)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
