import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from site_app import models
from django.contrib.auth import get_user_model

User = get_user_model()


def main():
    User.objects.create_superuser('admin1234', 'gazmaket@gmail.com', 'sunday2018')
    realtor = User.objects.create(username='ann', email='gazmaket@gmail.com', password='sunday2018', is_realtor=True)
    user = User.objects.create(username='god', email='gazmaket@gmail.com', password='sunday2018')

    flat = models.Flat.objects.create(
        heading='perfect flat', district='Naukova', cost='1234', description="Magic flat", total_size='1024',
        living_size='1000', kitchen_size='24', rooms_count='10', floor='17', elevator=True, is_approved=True)

    models.Flat.objects.create(
        heading='bad flat', district='Saltovka', cost='1', description="Bad flat", total_size='15',
        living_size='12', kitchen_size='3', rooms_count='1', floor='1')

    models.Flat.objects.create(
        heading='middle flat', district='Alekseevka', cost='170', description="Middle Flat", total_size='130',
        living_size='100', kitchen_size='30', rooms_count='4', floor='2')

    house = models.House.objects.create(
        heading='Big house', district='Kozacha Lopan', cost='1700', description="Big house", house_size='450',
        garage=True, outdoors_size='780', is_approved=True)
    models.House.objects.create(
        heading='Small house', district='HTZ', cost='100', description="Bad house", house_size='45',
        outdoors_size='100')

    room = models.Room.objects.create(
        heading='Normal room', district='Center', cost='20', description="Normal room", size='15', floor='3',
        total_rooms='5', is_approved=True)
    models.Room.objects.create(
        heading='Bad room', district='Holodna Hora', cost='10', description="Bad room", size='3', floor='5',
        total_rooms='2')

    models.RealtorPlacement.objects.create(realtor=realtor, flat=flat)
    placement = models.RealtorPlacement.objects.create(realtor=realtor, house=house)
    models.RealtorPlacement.objects.create(realtor=realtor, room=room)

    models.Contract.objects.create(user=user, placement=placement)


if __name__ == '__main__':
    main()