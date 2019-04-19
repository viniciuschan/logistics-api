from decimal import Decimal
from localflavor.br import br_states

from django.contrib.postgres.fields import JSONField
from django.db import models


class LogisticsNet(models.Model):
    """ Model to represent logistic networks """

    name = models.CharField(max_length=100, verbose_name='name')
    path_data = JSONField(blank=False, null=False)
    state = models.CharField(
        max_length=2, choices=br_states.STATE_CHOICES,
        verbose_name='state'
    )
    date_added = models.DateField(
        auto_now_add=True, verbose_name='date added'
    )

    def __str__(self):
        return f'ID: {self.pk} - {self.name} - {self.state}'

    class Meta:
        verbose_name = 'Logistic Network'


class UserSearch(models.Model):
    """ Model to represent user searches """

    source = models.CharField(max_length=20, verbose_name='source')
    destination = models.CharField(max_length=20, verbose_name='destination')
    autonomy = models.DecimalField(
        max_digits=4, decimal_places=2, default=Decimal(), verbose_name='autonomy'
    )
    fuel_price = models.DecimalField(
        max_digits=4, decimal_places=2, default=Decimal(), verbose_name='fuel_price'
    )

    def __str__(self):
        return f'{self.pk} - From: {self.source} To {self.destination}'

    class Meta:
        verbose_name = 'User'
