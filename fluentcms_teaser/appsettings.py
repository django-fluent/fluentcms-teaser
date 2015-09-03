# -*- coding: utf-8 -*-

from django.conf import settings

FLUENTCMS_TEASER_CLEAN_HTML = getattr(settings, "FLUENTCMS_TEASER_CLEAN_HTML", False)
FLUENTCMS_TEASER_SANITIZE_HTML = getattr(settings, "FLUENTCMS_TEASER_SANITIZE_HTML", False)
FLUENTCMS_TEASER_UPLOAD_TO = getattr(settings, 'FLUENTCMS_TEASER_UPLOAD_TO', '.')
