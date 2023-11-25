from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineObject

@receiver(post_save, sender=OrderLineObject)
def edit_OrderLineObject_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineObject)
def edit_OrderLineObject_on_remove(sender, instance, **kwargs):
    instance.order.update_total()