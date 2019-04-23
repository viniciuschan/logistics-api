from django.contrib.postgres.fields import JSONField
from django.db import models


class LogisticsNet(models.Model):
    """ Model to represent logistic networks """

    name = models.CharField(
        'name', max_length=100, db_index=True, unique=True
        )
    path_data = JSONField('path_data', blank=False, null=False)
    date_added = models.DateField('date added', auto_now_add=True)

    def __str__(self):
        return f'ID: {self.pk} - Name: {self.name}'

    class Meta:
        verbose_name = 'Logistic Network'

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(LogisticsNet, self).save(*args, **kwargs)
