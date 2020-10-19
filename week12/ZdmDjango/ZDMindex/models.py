from django.db import models

# Create your models here.
class ZdmTable(models.Model):
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=4000)
    comment_date = models.CharField(max_length=255)
    score = models.CharField(max_length=10)
    
    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'zdm_comment_score'