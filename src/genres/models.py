from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name = 'Genre name',
        max_length = 20,
    )
    desciption = models.TextField(
        verbose_name = 'Genre description',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name