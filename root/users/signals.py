from django.db.models.signals import post_save
from django.dispatch import receiver
from ecommapp.models import Customer

@receiver(post_save, sender = Customer)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user = instance)