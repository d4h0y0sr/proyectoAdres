from django.db import models

class CSVData(models.Model):
    col1 = models.IntegerField()
    col2 = models.EmailField()
    col3 = models.CharField(max_length=2)
    col4 = models.IntegerField()
    col5 = models.CharField(max_length=255)