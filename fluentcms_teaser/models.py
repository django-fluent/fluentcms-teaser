# -*- coding: utf-8 -*-

from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import PluginImageField, PluginUrlField
from fluent_contents.models.db import ContentItem

from . import appsettings


@python_2_unicode_compatible
class TeaserItem(ContentItem):

    title = models.CharField(_("title"), max_length=256)
    image = PluginImageField(_("image"), upload_to=appsettings.FLUENTCMS_TEASER_UPLOAD_TO, blank=True, null=True)
    url = PluginUrlField(_("URL"), null=True, blank=True,
        help_text=_("If present image will be clickable."))

    description = models.TextField(_("description"), blank=True, null=True)

    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )))

    class Meta:
        verbose_name = _("Teaser")
        verbose_name_plural = _("Teasers")

    def __str__(self):
        return self.title
