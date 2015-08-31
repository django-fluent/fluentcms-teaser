# -*- coding: utf-8 -*-

from django.conf import settings

FLUENTCMS_TEASER_UPLOAD_TO = getattr(settings, 'FLUENTCMS_TEASER_UPLOAD_TO', '.')
