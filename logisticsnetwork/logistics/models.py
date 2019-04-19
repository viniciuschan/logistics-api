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
