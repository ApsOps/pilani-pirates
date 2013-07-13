from django.db import models

# Create your models here.


class Common(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    magnet = models.CharField(max_length=100)

    class Meta:
        abstract = True
        verbose_name = ('Common')
        verbose_name_plural = ('Commons')

    def __unicode__(self):
        return self.id

    def get_model_name(self):
        return self._meta.verbose_name


class Movie(Common):
    date_released = models.DateField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    runtime = models.IntegerField()
    cast = models.CharField(max_length=100)
    trailer_link = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Movie')
        verbose_name_plural = ('Movies')

    def __unicode__(self):
        return self.title


class Series(Common):
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    runtime = models.IntegerField()
    cast = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Series')
        verbose_name_plural = ('Series')

    def __unicode__(self):
        return self.title


class Game(Common):
    date_released = models.DateField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    trailer_link = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Game')
        verbose_name_plural = ('Games')

    def __unicode__(self):
        return self.title


class App(Common):
    date_released = models.DateField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)  # os supported

    class Meta:
        verbose_name = ('App')
        verbose_name_plural = ('Apps')

    def __unicode__(self):
        return self.title
