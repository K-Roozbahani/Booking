from carts.models import HotelRoomOrder, AccommodationOrder
from carts.serializers import HotelRoomOrderSerializer, AccommodationOrderSerializer
from places.models import HotelRoomDatePrice, AccommodationDatePrice, Place, Accommodation
from django.db.models import Q
from django.utils import timezone



def get_date(str_time, format_time="%Y-%m-%d"):
    new_datetime = timezone.datetime.strptime(str_time, format_time)
    return new_datetime.date()


def taking_order(request):
    user = request.user
    start_date = request.data.get('start_date')
    end_date = request.data.get('end_date')
    start_date = get_date(start_date)
    end_date = get_date(end_date)
    order_type = int(request.data.get('order_type'))
    pk = request.data.get('pk')
    date_prices = None
    order = None
    serializer = None
    if order_type == 1:
        place = Place.objects.get(pk=pk)
        date_prices = HotelRoomDatePrice.objects.filter(Q(palce=place), Q(date__gte=start_date), Q(date__lte=end_date))
        serializer = HotelRoomOrderSerializer
        order = HotelRoomOrder(place=place, user=user, status=1)

    elif order_type == 2:
        accommodation = Accommodation.objects.get(pk=pk)
        date_prices = AccommodationDatePrice.objects.filter(Q(accommodation=accommodation),
                                                            Q(date__gte=start_date), Q(date__lte=end_date))
        serializer = AccommodationOrderSerializer()
        order = AccommodationOrder(accommodation=accommodation, user=user, status=1)

    order.save()
    order.date_prices.set(date_prices)
    serializer.instance = order
    return {'order': order, 'serializer': serializer}


def reserve_date_price(order):
    date_prices = order.date_prices.all()
    for date in date_prices:
        date.is_reserve = True

    return date_prices.objects.bulk_update(date_prices, ['is_reserve'])
