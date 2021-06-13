from celery.decorators import periodic_task, task
from celery.task.schedules import crontab
from celery import shared_task
import requests
from .models import CryptoData

from celery.utils.log import get_task_logger

logger = get_task_logger('__name__')


@shared_task
def get_crypto_data():
    data_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    raw_data = requests.get(data_url).json()

    for item in raw_data:
        p, _ = CryptoData.objects.get_or_create(name=item['name'])
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']
        p.save()


@periodic_task(run_every=(crontab(minute='*/1')))
def create_obj():
    get_crypto_data.delay()
