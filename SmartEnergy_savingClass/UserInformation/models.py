from django.db import models

# Create your models here.
class TbUser(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_user'