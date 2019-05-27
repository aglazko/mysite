def get_placement_query(request):
    filter_set = {}
    if request.user.is_authenticated:
        if request.user.is_realtor or request.user.is_admin:
            print("Yeah")
            filter_set['is_approved'] = request.GET.get('is_approved', True)
        else:
            filter_set['is_approved'] = True
    else:
        filter_set['is_approved'] = True

    if request.GET.get('is_free'):
        filter_set['is_free'] = request.GET.get('is_free')

    if request.GET.get('cost_more'):
        filter_set['cost__gte'] = request.GET.get('cost_more')

    if request.GET.get('cost_less'):
        filter_set['cost__lte'] = request.GET.get('cost_less')
    return filter_set


def get_room_query(request):
    filter_set = get_placement_query(request)
    if request.GET.get('size_more'):
        filter_set['size__gte'] = request.GET.get('size_more')

    if request.GET.get('size_less'):
        filter_set['size__lte'] = request.GET.get('size_less')

    if request.GET.get('floor_more'):
        filter_set['floor__gte'] = request.GET.get('floor_more')

    if request.GET.get('floor_less'):
        filter_set['floor__lte'] = request.GET.get('floor_less')

    if request.GET.get('total_rooms_more'):
        filter_set['total_rooms__gte'] = request.GET.get('total_rooms_more')

    if request.GET.get('total_rooms_less'):
        filter_set['total_rooms__lte'] = request.GET.get('total_rooms_less')

    if request.GET.get('elevator'):
        filter_set['elevator'] = request.GET.get('elevator')

    return filter_set


def get_house_query(request):
    filter_set = get_placement_query(request)
    if request.GET.get('house_size_more'):
        filter_set['house_size__gte'] = request.GET.get('house_size_more')

    if request.GET.get('house_size_less'):
        filter_set['house_size__lte'] = request.GET.get('house_size_less')

    if request.GET.get('garage'):
        filter_set['garage'] = request.GET.get('garage')

    if request.GET.get('outdoors_size_more'):
        filter_set['outdoors_size__gte'] = request.GET.get('outdoors_size_more')

    if request.GET.get('outdoors_size_less'):
        filter_set['outdoors_size__lte'] = request.GET.get('outdoors_size_less')

    return filter_set


def get_flat_query(request):
    filter_set = get_placement_query(request)
    if request.GET.get('floor_more'):
        filter_set['floor__gte'] = request.GET.get('floor_more')

    if request.GET.get('floor_less'):
        filter_set['floor__lte'] = request.GET.get('floor_less')

    if request.GET.get('elevator'):
        filter_set['elevator'] = request.GET.get('elevator')

    if request.GET.get('rooms_count _more'):
        filter_set['rooms_count __gte'] = request.GET.get('rooms_count _more')

    if request.GET.get('rooms_count _less'):
        filter_set['rooms_count __lte'] = request.GET.get('rooms_count _less')

    if request.GET.get('total_size_more'):
        filter_set['total_size__gte'] = request.GET.get('total_size_more')

    if request.GET.get('total_size_less'):
        filter_set['total_size__lte'] = request.GET.get('total_size_less')

    if request.GET.get('kitchen_size_more'):
        filter_set['kitchen_size__gte'] = request.GET.get('kitchen_size_more')

    if request.GET.get('kitchen_size_less'):
        filter_set['kitchen_size__lte'] = request.GET.get('kitchen_size_less')

    if request.GET.get('living_size_more'):
        filter_set['living_size__gte'] = request.GET.get('living_size_more')

    if request.GET.get('living_size_less'):
        filter_set['living_size__lte'] = request.GET.get('living_size_less')

    return filter_set


def is_realtor(user):
    return user.is_authenticated and (user.is_admin or user.is_realtor)