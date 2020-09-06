from django.db import models

# Create your models here.
class MovieTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    star = models.IntegerField()
    review = models.CharField(max_length=600)
    
    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'movietable'