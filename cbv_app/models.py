from django.db import models
from django.urls import reverse
#from django.core.urlresolvers import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        #return "cbv_app/%i/" % self.pk
        print ("in get_absolute_url")
        print(reverse("cbv_app:detail", kwargs = {'pk':self.pk}))
        return reverse("cbv_app:detail", kwargs = {'pk':self.pk})


class Student(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name = 'students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
