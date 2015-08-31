# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import TeaserItem


@plugin_pool.register
class TeaserPlugin(ContentPlugin):
    model = TeaserItem
    category = _('Media')
    render_template = "fluentcms_teaser/teaser.html"
