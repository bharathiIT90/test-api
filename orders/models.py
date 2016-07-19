from django.db import models
from django.conf import settings
# Create your models here.

class UserCheckout(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, blank=True)
	email = models.EmailField()


	def __unicode__(self):
		return self.email

# class Order(models.model):
# 	#cart
# 	#user
# 	#shipping address
# 	#billing address
# 	#shipping total
# 	#order total
# 	#order_id
