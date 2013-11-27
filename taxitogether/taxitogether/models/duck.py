from django.db import models


class Duck(models.Model):
    class Meta:
        app_label = "taxitogether"

    GENDER_CHOICE = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    DEVICE_CHOICE = (
            ('iPhone', 'iPhone'),
            ('Android', 'Android'),
            )
    userid = models.CharField(max_length=50, db_index=True)  # index
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    key = models.CharField(max_length=25)
    phone = models.CharField(max_length=11, db_index=True)
    token = models.CharField(max_length=200)
    device_type = models.CharField(max_length=10, choices=DEVICE_CHOICE)
    verified = models.BooleanField(default=False)
    registertime = models.DateTimeField(auto_now_add=True)
    lastmodified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.userid + " " + self.device_type


class Tmp_Duck(models.Model):
    class Meta:
        app_label = "taxitogether"

    GENDER_CHOICE = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    DEVICE_CHOICE = (
            ('iPhone', 'iPhone'),
            ('Android', 'Android'),
            )
    userid = models.ForeignKey(Duck, db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    key = models.CharField(max_length=25)
    phone = models.CharField(max_length=11, db_index=True)
    token = models.CharField(max_length=200)
    device_type = models.CharField(max_length=10, choices=DEVICE_CHOICE)
    requesttime = models.DateTimeField(auto_now=True)


class Settings(models.Model):
    class Meta:
        app_label = "taxitogether"

    userid = models.ForeignKey(Duck, db_index=True) #index
    photo = models.ImageField(upload_to='photo', blank=True, null=True, default='photo/default/default.png')
    pushtime = models.IntegerField(default=5)
