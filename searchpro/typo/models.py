from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "companies"

    def __str__(self):
        return '%s' %(self.name)