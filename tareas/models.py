from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tarea(models.Model):
	descripcion=models.CharField(max_length=128)
	tarea_done=models.BooleanField(default=False)

# done
