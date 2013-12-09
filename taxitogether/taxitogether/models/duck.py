from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class Duck(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = "taxitogether"

    REQUIRED_FIELDS = ['email', 'gender']  # Only for 'manage.py createsuperuser'
    USERNAME_FIELD = 'username'
    GENDER_CHOICE = (
            ('M', 'Male'),
            ('F', 'Female'),
            )

    objects = UserManager()

    # Comes from django.contrib.auth.models.AbstractUser
    username = models.CharField(max_length=50, db_index=True, unique=True, primary_key=True)
    email = models.EmailField("@kaist.ac.kr", blank=False, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # TaxiTogether specific
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    key = models.CharField(max_length=25)
    verified = models.BooleanField(default=False)

    # Meta
    date_joined = models.DateTimeField(auto_now_add=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


class Settings(models.Model):
    class Meta:
        app_label = "taxitogether"

    user = models.OneToOneField(Duck, related_name='setting', primary_key=True)
    photo = models.ImageField(upload_to='photo', blank=True, null=True, default='photo/default/default.png')
    pushtime = models.IntegerField(default=5)


class Device(models.Model):
    class Meta:
        app_label = "taxitogether"

    DEVICE_CHOICE = (
            ('iPhone', 'iPhone'),
            ('Android', 'Android'),
            )

    owner = models.ForeignKey(Duck, related_name="devices", db_index=True)
    phone = models.CharField(max_length=11, db_index=True)
    token = models.CharField(max_length=200)
    device_type = models.CharField(max_length=10, choices=DEVICE_CHOICE)

    registertime = models.DateTimeField(auto_now_add=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.owner.username + "'s " + idself.device_type


@receiver(post_save, sender=Duck)
def create_setting(sender, instance, created, raw, **kwargs):
    """ Create Settings instance when new Duck has been created. """
    if raw or not created:
        return
    Settings(user=instance).save()
