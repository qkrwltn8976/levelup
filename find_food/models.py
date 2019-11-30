from django.db import models

# Create your models here.

class Vendor(models.Model):
    position_x = models.FloatField()
    position_y = models.FloatField()
    open_time = models.TimeField(auto_now=False, auto_now_add=False)
    close_time = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.IntegerField()
    loc = models.ForeignKey('Location', on_delete=models.CASCADE,blank = True)


    def __str__(self):
        return "("+str(self.position_x) +", "+ str(self.position_y)+")"

class Location(models.Model):
    name = models.CharField(max_length=5)
    position_x = models.FloatField()
    position_y = models.FloatField()
    radius = models.IntegerField()

    def __str__(self):
        return self.name