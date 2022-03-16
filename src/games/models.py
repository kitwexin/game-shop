from django.db import models
from companies.models import Company
from genres.models import Genre


class Game(models.Model):
    name = models.CharField(
        verbose_name='Game name',
        max_length=50,
    )
    price = models.IntegerField(
        verbose_name='Game price USD',
        default=0,
    )
    release_date = models.DateField(
        verbose_name='Release date',
        null=True,
        blank=True
    )
    development_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Development company',
        default='Unknown',
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Game genre',
        default='No genre'
    )
    image = models.ImageField(
        verbose_name='Game cover',
        upload_to='games-pics',
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Game description',
    )
    age_limit = models.IntegerField(
        verbose_name='Age limit',
        default=0
    )

    def __str__(self):
        return self.name
