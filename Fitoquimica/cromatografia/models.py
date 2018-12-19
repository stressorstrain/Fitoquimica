from django.db import models
from django.utils import timezone
import datetime


class Gas(models.Model):
    ars = models.IntegerField(default=0)
    ars_p = models.IntegerField(default=0)
    h2 = models.IntegerField(default=0)
    h2_p = models.IntegerField(default=0)
    he = models.IntegerField(default=0)
    he_p = models.IntegerField(default=0)
    ver_name = models.CharField(default="None", max_length=100)
    ver_date = models.CharField(default="None", max_length=12)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.ver_date

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Gas, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Gases"
        get_latest_by = 'created_at'
# Create your models here.
