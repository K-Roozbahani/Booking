from redis import Redis
from django.conf import settings

redis_cli = Redis(decode_responses=True)
currency_hash_name = settings.REDIS_CURRENCY_HASH_NAME
exchange_rate_hash_name = settings.REDIS_EXCHANGE_RATE_HASH_NAME


# holidays_hash_name = settings.REDIS_HOLIDAYS_HASH_NAME


def get_currency(currency_id):
    currency = redis_cli.hget(currency_hash_name, currency_id)
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
        redis_cli.hset(currency_hash_name, currency_key, currency_national_symbol)
        return True


def currency_choices():
    currencies = redis_cli.hgetall(currency_hash_name)
    list_currencies = []
    for key, value in currencies.items():
        currency = (int(key), str(value))
        list_currencies.append(currency)
    return tuple(list_currencies)


def set_exchange_rate(currency_from, currency_to, rate):
    currency_from = str(get_currency(currency_from))
    currency_to = str(get_currency(currency_to))
    key = currency_from + "/" + currency_to
    redis_cli.hset(exchange_rate_hash_name, key, rate)
    print('Exchange rate updated')
    return True


def get_exchange_rate(currency_from, currency_to):
    key = currency_from + "/" + currency_to
    rate = redis_cli.hget(exchange_rate_hash_name, key)
    if rate:
        return float(rate)
    else:
        key = currency_to + "/" + currency_from
        rate = redis_cli.hget(exchange_rate_hash_name, key)
        if rate:
            rate = 1 / float(rate)
            return rate
        else:
            return False

# def update_holiday(date, description):
#     previous_holidays =
#     redis_cli.hset(holidays_hash_name, date, description)
