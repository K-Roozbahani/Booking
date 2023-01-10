from carts.models import PlaceOrder
from carts.serializers import PlaceOrderSerializer
from places.models import PlaceDatePrice, Place, Accommodation
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
    # print(pk, user, start_date, end_date, order_type)
    # if order_type == 1:
    #     place = Place.objects.get(pk=pk)
    #     date_prices = HotelRoomDatePrice.objects.filter(Q(palce=place), Q(date__gte=start_date), Q(date__lte=end_date))
    #     serializer = HotelRoomOrderSerializer
    #     order = HotelRoomOrder(place=place, user=user, status=1)

    if order_type == 1:
        # print('-'*10)
        accommodation = Accommodation.objects.get(pk=pk)
        # print('1'*10)
        date_prices = PlaceDatePrice.objects.filter(Q(accommodation=accommodation),
                                                    Q(date__gte=start_date), Q(date__lte=end_date))
        # print('2'*10)
        serializer = PlaceOrderSerializer()
        # print('3'*10)
        order = PlaceOrder(user=user, status=1)
        # print('4'*10)

    order.save()
    # print('5'*10)
    order.date_prices.set(date_prices)
    # print('6'*10)
    serializer.instance = order
    # print('7'*10)
    return {'order': order, 'serializer': serializer}


def reserve_date_price(order):
    date_prices = order.date_prices.all()
    for date in date_prices:
        date.is_reserve = True

    return date_prices.bulk_update(date_prices, ['is_reserve'])


def get_all_or_one_order(request, pk=None):
    # print('-' * 20)
    if pk or 0:
        order_type = int(request.GET.get('type'))
        print(type(order_type))
        if not order_type:
            raise ValueError('\'order_type\' required')

        if order_type == 1:
            hotel_order = PlaceOrder.objects.get(pk=pk)
            hotel_order_serializer = PlaceOrderSerializer(hotel_order)
            return hotel_order_serializer.data

        # elif order_type == 2:
        #     accommodation_order = AccommodationOrder.objects.get(pk=pk)
        #     accommodation_order_serializer = AccommodationOrderSerializer(accommodation_order)
        #     return accommodation_order_serializer.data

    elif not pk:
        # print('*' * 20)
        user = request.user
        accommodation_orders = PlaceOrder.objects.filter(user=user)
        accommodation_order_serializer = PlaceOrderSerializer(accommodation_orders, many=True)
        # hotel_orders = HotelRoomOrder.objects.filter(user=user)
        # hotel_orders_serializer = HotelRoomOrderSerializer(hotel_orders, many=True)

    return {'place_orders': accommodation_order_serializer.data}
    # 'hotel_orders': hotel_orders_serializer.data}


# def redirect_user_for_payed(date_payment):
#     redirect_to_booking(date_payment)


def validate_payment(secure_date):
    return secure_date


def get_object_order(reqeust, pk):
    # print('-'*10)
    if pk:
        order_type = int(reqeust.GET.get('type'))
        # print('1'*10)
        if order_type == 1:
            return PlaceOrder.objects.get(pk=pk)

        # elif order_type == 2:
        #     # print('2'*10)
        #     return AccommodationOrder.objects.get(pk=pk)
        # print('3'*10)
    else:
        order_type = int(reqeust.GET.get('type'))
        if order_type == 1:
            return Place.objects.all()
        # elif order_type == 2:
        #     return HotelRoomOrder.objects.all()
