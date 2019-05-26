from django.db import models


# Create your models here.
class Placement(models.Model):
    class Meta:
        abstract = True
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    elevator = models.BooleanField()
    cost_of_place = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __repr__(self):
        return self.heading


class Room(Placement):
    class Meta:
        db_table = "rooms"
    size = models.IntegerField()
    floor = models.IntegerField()
    count_of_roommate = models.IntegerField()


    # def adds(self):
    #     super(self).save()
    #     self.save()


class Flat(Placement):
    total_size = models.IntegerField()
    living_size = models.IntegerField()
    rooms_count = models.IntegerField()
    floor = models.IntegerField()

    # def adds(self):
    #     # super(self).save()
    #     self.save()
    def __repr__(self):
        super().__repr__()



class House(Placement):
    house_size = models.IntegerField()
    garage = models.BooleanField()
    outdoors_size = models.IntegerField()

    # def adds(self):
    #     super(self).save()
    #     self.save()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=100)
    is_admin = models.BooleanField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    # def adds(self):
    #     # super(self).save()
    #     self.save()

