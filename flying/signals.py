from django.db.models.signals import post_save
from django.dispatch import receiver
from redis import Redis
from django.conf import settings
redis_cli = Redis()
def set_redis_currency():
