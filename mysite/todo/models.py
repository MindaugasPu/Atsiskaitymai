from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Uzduotis(models.Model):
    uzduotis = models.CharField('Užduotis', max_length=200)
    vartotojas = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return f"{self.vartotojas} \nužduotis: {self.uzduotis} \n({self.data})"

    class Meta:
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'