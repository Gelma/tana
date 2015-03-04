# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking_date', models.DateTimeField(verbose_name=b'booking date')),
                ('name', models.CharField(max_length=200)),
                ('activity', models.CharField(default=b'TM', max_length=2, choices=[(b'IS', b'Instructor'), (b'TM', b'Tandem')])),
                ('cardinality', models.IntegerField(default=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
