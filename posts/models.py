from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Park_number(models.Model):
    p_local_name = models.CharField('공원위치지역', max_length=100)
    p_idx = models.IntegerField('공원번호')

    def __str__(self):
        return self.p_local_name


class Post(models.Model):
    p_idx = models.ForeignKey(Park_number, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    starpoint = models.IntegerField('별점1~5', null=True, blank=True,
                                    validators=[MinValueValidator(0), MaxValueValidator(5)])
    contents = models.TextField('글내용', max_length=500)
    images = models.ImageField(blank=True, upload_to="images", null=True)

    def __str__(self):
        return self.contents