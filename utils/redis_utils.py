from redis import Redis
from django.conf import settings

redis_cli = Redis()


def get_currency(currency_id):
    hash_name = settings.REDIS_CURRENCY_HASH_NAME
    currency = redis_cli.hget(hash_name, currency_id)
    return currency


def set_currency(currency_key, currency_national_symbol):
    hash_name = settings.REDIS_CURRENCY_HASH_NAME
    exist = get_currency(currency_key)
    if exist and currency_key == exist:
        print('Redis currency already was update')
        return False
    elif exist:
        raise ValueError('duplicate value error')
    else:
        redis_cli.hset(hash_name, currency_key, currency_national_symbol)
        return True


def get_currency_choices():
    hash_name = settings.REDIS_CURRENCY_HASH_NAME
    currencies = redis_cli.hgetall(hash_name)
    list_currency =[]
    for key, value in currencies.items():
        print(key, value)
        new_currency = (key, value)
        list_currency.append(new_currency)
    return tuple(list_currency)