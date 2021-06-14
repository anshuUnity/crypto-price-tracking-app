from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from django.dispatch import receiver
import json
from asgiref.sync import async_to_sync
from .models import CryptoData


@receiver(post_save, sender=CryptoData)
def price_update(sender, created, instance, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        data = {}
        data['price'] = instance.price
        data['coin_name'] = instance.name

        print(instance.price)

        async_to_sync(channel_layer.group_send)(
            'price', {
                'type': 'update_price',
                'price': json.dumps(data)
            }
        )
