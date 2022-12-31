from redis import Redis
from django.conf import settings

redis_cli = Redis()
hash_name = settings.REDIS_CURRENCY_HASH_NAME


def get_currency(currency_id):
    currency = redis_cli.hget(hash_name, currency_id)
    return currency


def set_currency(currency_key, currency_national_symbol):
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


def currency_choices():
    currencies = redis_cli.hgetall(hash_name)
    list_currencies = []
    for key, value in currencies.items():
        currency = (key, value)
        list_currencies.append(currency)
    return tuple(list_currencies)
