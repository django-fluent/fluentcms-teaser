# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import TeaserItem


@plugin_pool.register
class TeaserPlugin(ContentPlugin):
    model = TeaserItem
    category = _('Media')
    render_template = "fluentcms_teaser/teaser.html"
    admin_init_template = "admin/fluentcms_teaser/admin_init.html" # TODO: remove the need for this.

    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description'),
        }),
        (_("read more link"), {
            'fields': ('url', 'url_title','target'),
        }),
    )
