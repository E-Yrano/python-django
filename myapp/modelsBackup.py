from django.db import models

# Create your models here.
class FancyLight(models.Model):
    titleText = models.CharField(max_length=200)
    contentText = models.CharField(max_length=200)
    url = models.URLField(verbose_name='url')

class HeadWord(models.Model):
    titleText = models.CharField(max_length=50)

class BodyWord(models.Model):
    Filed1 = models.CharField(max_length=200)
    def __str__(self):
        return self.Filed1
    # Filed2 = models.CharField(max_length=200)
    # Filed3 = models.CharField(max_length=200)
    # Filed4 = models.CharField(max_length=200)
    # Filed5 = models.CharField(max_length=200)
    # Filed6 = models.CharField(max_length=200)
    # Filed7 = models.CharField(max_length=200)
    # Filed8 = models.CharField(max_length=200)
    # Filed9 = models.CharField(max_length=200)
    # Filed10 = models.CharField(max_length=200)
    # Filed11 = models.CharField(max_length=200)
    # Filed12 = models.CharField(max_length=200)
    # Filed13 = models.CharField(max_length=200)
    # Filed14 = models.CharField(max_length=200)
    # Filed15 = models.CharField(max_length=200)