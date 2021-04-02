from django.db import models

# Create your models here.
class TbLine(models.Model):
    tid = models.AutoField(primary_key=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    temp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_line'