from django.db import models
from django.db.models.fields import TextField

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=200, default='Pakistan Cricket')
    date_of_creation = models.CharField(max_length=50, default='DD/MM/YY')
    para1 = models.TextField(blank=False)
    para2 = models.TextField(blank=True)
    para3 = models.TextField(blank=True)
    para4 = models.TextField(blank=True)
    para5 = models.TextField(blank=True)
    card_image = models.TextField(
        default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')
    img1 = models.TextField(
        blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')
    img2 = models.TextField(
        blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')
    img3 = models.TextField(
        blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')
