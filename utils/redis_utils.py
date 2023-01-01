from redis import Redis
from django.conf import settings

redis_cli = Redis(decode_responses=True)
hash_currency_name = settings.REDIS_CURRENCY_HASH_NAME
hash_exchange_rate_name = settings.REDIS_EXCHANGE_RATE_HASH_NAME


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


def set_exchange_rate(currency_from, currency_to, rate):
    currency_from = str(get_currency(currency_from))
    currency_to = str(get_currency(currency_to))
    key = currency_from + "/" + currency_to
    redis_cli.hset(hash_exchange_rate_name, key, rate)
    print('Exchange rate updated')
    return True


def get_exchange_rate(currency_from, currency_to):
    key = currency_from + "/" + currency_to
    rate = redis_cli.hget(hash_exchange_rate_name, key)
    if rate:
        return float(rate)
    else:
        key = currency_to + "/" + currency_from
        rate = redis_cli.hget(hash_exchange_rate_name, key)
        if rate:
            return 1/float(rate)
        else:
            return False
