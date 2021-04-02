from django.db import models

# Create your models here.
class Search(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    time = models.CharField(max_length=10)
    pnum = models.IntegerField()
    temp = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tb_search'


