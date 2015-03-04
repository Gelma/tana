from django.db import models

# Create your models here.

class Booking(models.Model):
    '''the booking entity'''
    STUDENT = 'ST'
    TANDEM = 'TM'
    ACTIVITIES = (
            (STUDENT,'Student'),
            (TANDEM,'Tandem')
            )
    PLANE_QUANTITY = (
            (1,'1'),
            (2,'2'),
            (3,'3'),
            (4,'4'),
            (5,'5'),
            )
    booking_date=models.DateTimeField('booking date')
    name = models.CharField(max_length=200)
    activity = models.CharField(max_length=2,choices=ACTIVITIES,default=TANDEM)
    cardinality = models.IntegerField(choices=PLANE_QUANTITY,default=1)

    def __unicode__(self):
        return u''+str(self.name)+" ("+str(self.booking_date)+")"
