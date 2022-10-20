# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdsOwner(models.Model):
    id_ads_owner = models.AutoField(db_column='ID_ADS_OWNER', primary_key=True)  # Field name made lowercase.
    id_owner = models.ForeignKey('Owner', models.DO_NOTHING, db_column='ID_OWNER', blank=True, null=True)  # Field name made lowercase.
    link_ad_owner = models.CharField(db_column='LINK_AD_OWNER', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type_ad_owner = models.IntegerField(db_column='TYPE_AD_OWNER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ads_owner'


class Area(models.Model):
    id_area = models.AutoField(db_column='ID_AREA', primary_key=True)  # Field name made lowercase.
    name_area = models.CharField(db_column='NAME_AREA', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'area'


class Balcony(models.Model):
    id_balcony = models.AutoField(db_column='ID_BALCONY', primary_key=True)  # Field name made lowercase.
    name_balcony = models.CharField(db_column='NAME_BALCONY', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'balcony'


class Bathroom(models.Model):
    id_bathroom = models.AutoField(db_column='ID_BATHROOM', primary_key=True)  # Field name made lowercase.
    name_bathroom = models.CharField(db_column='NAME_BATHROOM', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bathroom'


class City(models.Model):
    id_city = models.AutoField(db_column='ID_CITY', primary_key=True)  # Field name made lowercase.
    name_city = models.CharField(db_column='NAME_CITY', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'city'


class ConditionObject(models.Model):
    id_condition_object = models.AutoField(db_column='ID_CONDITION_OBJECT', primary_key=True)  # Field name made lowercase.
    name_condition_object = models.CharField(db_column='NAME_CONDITION_OBJECT', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'condition_object'


class Deposite(models.Model):
    id_deposite = models.AutoField(db_column='ID_DEPOSITE', primary_key=True)  # Field name made lowercase.
    name_deposite = models.CharField(db_column='NAME_DEPOSITE', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'deposite'


class Estate(models.Model):
    id_estate = models.AutoField(db_column='ID_ESTATE', primary_key=True)  # Field name made lowercase.
    name_estate = models.CharField(db_column='NAME_ESTATE', unique=True, max_length=500)  # Field name made lowercase.
    link_estate = models.CharField(db_column='LINK_ESTATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_site = models.ForeignKey('Site', models.DO_NOTHING, db_column='ID_SITE', blank=True, null=True)  # Field name made lowercase.
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='ID_REGION', blank=True, null=True)  # Field name made lowercase.
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='ID_CITY', blank=True, null=True)  # Field name made lowercase.
    id_street = models.ForeignKey('Street', models.DO_NOTHING, db_column='ID_STREET', blank=True, null=True)  # Field name made lowercase.
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='ID_AREA', blank=True, null=True)  # Field name made lowercase.
    id_type_house = models.ForeignKey('TypeHouse', models.DO_NOTHING, db_column='ID_TYPE_HOUSE', blank=True, null=True)  # Field name made lowercase.
    id_balcony = models.ForeignKey(Balcony, models.DO_NOTHING, db_column='ID_BALCONY', blank=True, null=True)  # Field name made lowercase.
    id_type_room = models.ForeignKey('TypeRoom', models.DO_NOTHING, db_column='ID_TYPE_ROOM', blank=True, null=True)  # Field name made lowercase.
    id_bathroom = models.ForeignKey(Bathroom, models.DO_NOTHING, db_column='ID_BATHROOM', blank=True, null=True)  # Field name made lowercase.
    id_repair_status = models.ForeignKey('RepairStatus', models.DO_NOTHING, db_column='ID_REPAIR_STATUS', blank=True, null=True)  # Field name made lowercase.
    id_heating = models.ForeignKey('Heating', models.DO_NOTHING, db_column='ID_HEATING', blank=True, null=True)  # Field name made lowercase.
    id_window_view = models.ForeignKey('WindowView', models.DO_NOTHING, db_column='ID_WINDOW_VIEW', blank=True, null=True)  # Field name made lowercase.
    id_type_parking = models.ForeignKey('TypeParking', models.DO_NOTHING, db_column='ID_TYPE_PARKING', blank=True, null=True)  # Field name made lowercase.
    id_owner = models.ForeignKey('Owner', models.DO_NOTHING, db_column='ID_OWNER', blank=True, null=True)  # Field name made lowercase.
    num_of_estate = models.CharField(db_column='NUM_OF_ESTATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    year_build = models.CharField(db_column='YEAR_BUILD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    floor_estate = models.IntegerField(db_column='FLOOR_ESTATE', blank=True, null=True)  # Field name made lowercase.
    floor_flat = models.IntegerField(db_column='FLOOR_FLAT', blank=True, null=True)  # Field name made lowercase.
    count_room = models.CharField(db_column='COUNT_ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    full_space = models.DecimalField(db_column='FULL_SPACE', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    live_space = models.DecimalField(db_column='LIVE_SPACE', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    kitchen_space = models.DecimalField(db_column='KITCHEN_SPACE', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    price_estate = models.CharField(db_column='PRICE_ESTATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    internet = models.IntegerField(db_column='INTERNET', blank=True, null=True)  # Field name made lowercase.
    tv = models.IntegerField(db_column='TV', blank=True, null=True)  # Field name made lowercase.
    children = models.IntegerField(db_column='CHILDREN', blank=True, null=True)  # Field name made lowercase.
    animal = models.IntegerField(db_column='ANIMAL', blank=True, null=True)  # Field name made lowercase.
    smoking = models.IntegerField(db_column='SMOKING', blank=True, null=True)  # Field name made lowercase.
    passenger_lift = models.IntegerField(db_column='PASSENGER_LIFT', blank=True, null=True)  # Field name made lowercase.
    service_lift = models.IntegerField(db_column='SERVICE_LIFT', blank=True, null=True)  # Field name made lowercase.
    garbage_chute = models.IntegerField(db_column='GARBAGE_CHUTE', blank=True, null=True)  # Field name made lowercase.
    date_add = models.DateTimeField(db_column='DATE_ADD', blank=True, null=True)  # Field name made lowercase.
    archive = models.IntegerField(db_column='ARCHIVE', blank=True, null=True)  # Field name made lowercase.
    upd_archive_date = models.DateTimeField(db_column='UPD_ARCHIVE_DATE', blank=True, null=True)  # Field name made lowercase.
    payment_by_bills_on = models.IntegerField(db_column='PAYMENT_BY_BILLS_ON', blank=True, null=True)  # Field name made lowercase.
    count_renters = models.CharField(db_column='COUNT_RENTERS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deposit = models.CharField(db_column='DEPOSIT', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estate'


class Heating(models.Model):
    id_heating = models.AutoField(db_column='ID_HEATING', primary_key=True)  # Field name made lowercase.
    name_heating = models.CharField(db_column='NAME_HEATING', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'heating'


class ImgEstate(models.Model):
    id_img_estate = models.AutoField(db_column='ID_IMG_ESTATE', primary_key=True)  # Field name made lowercase.
    link_img_estate = models.CharField(db_column='LINK_IMG_ESTATE', max_length=500)  # Field name made lowercase.
    id_estate = models.ForeignKey(Estate, models.DO_NOTHING, db_column='ID_ESTATE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'img_estate'


class Objects(models.Model):
    id_objects = models.AutoField(db_column='ID_OBJECTS', primary_key=True)  # Field name made lowercase.
    name_objects = models.CharField(db_column='NAME_OBJECTS', unique=True, max_length=50)  # Field name made lowercase.
    id_type_object = models.ForeignKey('TypeObject', models.DO_NOTHING, db_column='ID_TYPE_OBJECT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'objects'


class ObjectsInEstate(models.Model):
    id_objects_in_estate = models.AutoField(db_column='ID_OBJECTS_IN_ESTATE', primary_key=True)  # Field name made lowercase.
    id_estate = models.ForeignKey(Estate, models.DO_NOTHING, db_column='ID_ESTATE', blank=True, null=True)  # Field name made lowercase.
    id_objects = models.ForeignKey(Objects, models.DO_NOTHING, db_column='ID_OBJECTS', blank=True, null=True)  # Field name made lowercase.
    id_condition = models.ForeignKey(ConditionObject, models.DO_NOTHING, db_column='ID_CONDITION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'objects_in_estate'


class Owner(models.Model):
    id_owner = models.AutoField(db_column='ID_OWNER', primary_key=True)  # Field name made lowercase.
    id_type_owner = models.ForeignKey('TypeOwner', models.DO_NOTHING, db_column='ID_TYPE_OWNER', blank=True, null=True)  # Field name made lowercase.
    name_owner = models.CharField(db_column='NAME_OWNER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_registered = models.DateField(db_column='DATE_REGISTERED', blank=True, null=True)  # Field name made lowercase.
    rating_owner = models.DecimalField(db_column='RATING_OWNER', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    feedback_owner = models.TextField(db_column='FEEDBACK_OWNER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'owner'


class ParkingInEstate(models.Model):
    id_parking_in_estate = models.AutoField(db_column='ID_PARKING_IN_ESTATE', primary_key=True)  # Field name made lowercase.
    id_type_parking = models.ForeignKey('TypeParking', models.DO_NOTHING, db_column='ID_TYPE_PARKING', blank=True, null=True)  # Field name made lowercase.
    id_estate = models.ForeignKey(Estate, models.DO_NOTHING, db_column='ID_ESTATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'parking_in_estate'


class ParserProcess(models.Model):
    id_process = models.CharField(db_column='ID_PROCESS', primary_key=True, max_length=20)  # Field name made lowercase.
    id_site = models.ForeignKey('Site', models.DO_NOTHING, db_column='ID_SITE', blank=True, null=True)  # Field name made lowercase.
    date_begin = models.DateTimeField(db_column='DATE_BEGIN', blank=True, null=True)  # Field name made lowercase.
    date_end = models.DateTimeField(db_column='DATE_END', blank=True, null=True)  # Field name made lowercase.
    logs = models.TextField(db_column='LOGS', blank=True, null=True)  # Field name made lowercase.
    success = models.IntegerField(db_column='SUCCESS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'parser_process'


class Region(models.Model):
    id_region = models.AutoField(db_column='ID_REGION', primary_key=True)  # Field name made lowercase.
    name_region = models.CharField(db_column='NAME_REGION', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'region'


class RepairStatus(models.Model):
    id_repair_status = models.AutoField(db_column='ID_REPAIR_STATUS', primary_key=True)  # Field name made lowercase.
    name_repair_status = models.CharField(db_column='NAME_REPAIR_STATUS', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'repair_status'


class Site(models.Model):
    id_site = models.AutoField(db_column='ID_SITE', primary_key=True)  # Field name made lowercase.
    name_site = models.CharField(db_column='NAME_SITE', unique=True, max_length=100)  # Field name made lowercase.
    link_site = models.CharField(db_column='LINK_SITE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'site'


class Street(models.Model):
    id_street = models.AutoField(db_column='ID_STREET', primary_key=True)  # Field name made lowercase.
    name_street = models.CharField(db_column='NAME_STREET', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'street'


class TypeHouse(models.Model):
    id_type_house = models.AutoField(db_column='ID_TYPE_HOUSE', primary_key=True)  # Field name made lowercase.
    name_type_house = models.CharField(db_column='NAME_TYPE_HOUSE', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'type_house'


class TypeObject(models.Model):
    id_type_object = models.AutoField(db_column='ID_TYPE_OBJECT', primary_key=True)  # Field name made lowercase.
    name_type_object = models.CharField(db_column='NAME_TYPE_OBJECT', unique=True, max_length=150)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'type_object'


class TypeOwner(models.Model):
    id_type_owner = models.IntegerField(db_column='ID_TYPE_OWNER', primary_key=True)  # Field name made lowercase.
    name_type_owner = models.CharField(db_column='NAME_TYPE_OWNER', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'type_owner'


class TypeParking(models.Model):
    id_type_parking = models.AutoField(db_column='ID_TYPE_PARKING', primary_key=True)  # Field name made lowercase.
    name_type_parking = models.CharField(db_column='NAME_TYPE_PARKING', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'type_parking'


class TypeRoom(models.Model):
    id_type_room = models.AutoField(db_column='ID_TYPE_ROOM', primary_key=True)  # Field name made lowercase.
    name_type_room = models.CharField(db_column='NAME_TYPE_ROOM', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'type_room'


class WindowView(models.Model):
    id_window_view = models.AutoField(db_column='ID_WINDOW_VIEW', primary_key=True)  # Field name made lowercase.
    name_window_view = models.CharField(db_column='NAME_WINDOW_VIEW', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'window_view'


class Xpath(models.Model):
    id_xpath = models.AutoField(db_column='ID_XPATH', primary_key=True)  # Field name made lowercase.
    xpath = models.CharField(db_column='XPATH', max_length=150, blank=True, null=True)  # Field name made lowercase.
    name_xpath = models.CharField(db_column='NAME_XPATH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_site = models.ForeignKey(Site, models.DO_NOTHING, db_column='ID_SITE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'xpath'
