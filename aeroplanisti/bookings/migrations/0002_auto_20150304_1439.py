# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='activity',
            field=models.CharField(default=b'TM', max_length=2, choices=[(b'ST', b'Student'), (b'TM', b'Tandem')]),
            preserve_default=True,
        ),
    ]
