from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineObject

@receiver(post_save, sender=OrderLineObject)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.edit_total()

@receiver(post_delete, sender=OrderLineObject)
def update_on_save(sender, instance, **kwargs):

    instance.order.edit_total()