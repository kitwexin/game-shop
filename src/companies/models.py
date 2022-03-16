from django.db import models

class Company(models.Model):
    name = models.CharField(
        verbose_name = 'Company name',
        max_length = 50,
    )
    desciption = models.TextField(
        verbose_name = 'Company description',
        null=True,
        blank=True
    )
    logo = models.ImageField(
        verbose_name = 'Company logo',
        upload_to = 'companies-pics',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name