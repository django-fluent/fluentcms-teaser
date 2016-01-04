# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluentcms_teaser', '0002_auto_20150903_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaseritem',
            name='url_title',
            field=models.CharField(max_length=200, null=True, verbose_name='URL title', blank=True),
        ),
    ]
