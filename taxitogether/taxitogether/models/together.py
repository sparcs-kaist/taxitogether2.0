from django.db import models


class Together(models.Model):
    class Meta:
        app_label = "taxitogether"

    departure = models.CharField(max_length=100, db_index=True)
    destination= models.CharField(max_length=100, db_index=True)
    departtime = models.DateTimeField(db_index=True)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    maketime = models.DateTimeField(auto_now_add=True, db_index=True)
    departure_long = models.DecimalField(max_digits=9, decimal_places=6,
                                         db_index=True, blank=True, null=True)
    departure_lat = models.DecimalField(max_digits=8, decimal_places=6,
                                        db_index=True, blank=True, null=True)
    destination_long = models.DecimalField(max_digits=9, decimal_places=6,
                                           db_index=True, blank=True, null=True)
    destination_lat = models.DecimalField(max_digits=8, decimal_places=6,
                                          db_index=True, blank=True, null=True)
    def __unicode__(self):
        return 'id = ' + str(self.id)+' maketime = '+str(self.maketime)


class Participants(models.Model):
    class Meta:
        app_label = "taxitogether"

    together = models.ForeignKey('Together', db_index=True)
    member = models.ForeignKey('taxitogether.Duck', db_index=True)
    jointime = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    class Meta:
        app_label = "taxitogether"

    together = models.ForeignKey('Together', db_index=True)
    writer = models.ForeignKey('taxitogether.Duck')
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
