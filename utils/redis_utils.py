from redis import Redis
from django.conf import settings

redis_cli = Redis(decode_responses=True)
hash_currency_name = settings.REDIS_CURRENCY_HASH_NAME
hash_exchange_currency_name = settings.REDIS_CURRENCY_EXCHANGE_HASH_NAME


def get_currency(currency_id):
    currency = redis_cli.hget(hash_currency_name, currency_id)
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
        redis_cli.hset(hash_currency_name, currency_key, currency_national_symbol)
        return True

def currency_choices():
    currencies = redis_cli.hgetall(hash_currency_name)
    list_currencies = []
    for key, value in currencies.items():
        currency = (int(key), str(value))
        list_currencies.append(currency)
    return tuple(list_currencies)


def set_rate_currency_exchange(currency_from, currency_to, rate):
    currency_from = str(get_currency(currency_from))
    currency_to = str(get_currency(currency_to))
    key = currency_from + "/" + currency_to
    redis_cli.hset(hash_exchange_currency_name, key, rate)
    print('currency exchange rate updated')
    return True


def get_rate_currency_exchange(currency_from, currency_to):
    key = currency_from + "/" + currency_to
    rate = redis_cli.hget(hash_exchange_currency_name, key)
    if rate:
        return float(rate)
    else:
        print('currency exchange rate not exist')
        return False
