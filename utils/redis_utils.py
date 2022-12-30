from redis import Redis
from django.conf import settings

redis_cli = Redis()


def get_currency(currency_id):
    hash_name = settings.REDIS_CURRENCY_HASH_NAME
    currency = redis_cli.hget(redis_cli, currency_id)
    return currency


def set_currency(currency_key, currency_national_symbol):
    hash_name = settings.REDIS_CURRENCY_HASH_NAME
    exist = get_currency(currency_key)
    if exist and currency_key == exist:
        print('Redis currency already was update')
        return True
    elif exist:
        print('duplicate value error')
        return False
    else:
        print('add new currency to redis')
        redis_cli.hset(hash_name, currency_key, currency_national_symbol)
        return True
