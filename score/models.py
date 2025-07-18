from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Score(models.Model):
    name = models.CharField(_("name"),max_length=255)
    points = models.IntegerField(_("points"))

    def __str__(self):
        return self.name