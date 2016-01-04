# -*- coding: utf-8 -*-

from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import (
    PluginHtmlField, PluginImageField, PluginUrlField)
from fluent_contents.models.db import ContentItem

from django_wysiwyg.utils import clean_html, sanitize_html

from . import appsettings


@python_2_unicode_compatible
class TeaserItem(ContentItem):

    title = models.CharField(_("title"), max_length=256)
    image = PluginImageField(_("image"), upload_to=appsettings.FLUENTCMS_TEASER_UPLOAD_TO, blank=True, null=True)
    url = PluginUrlField(_("URL"), null=True, blank=True,
        help_text=_("If present image will be clickable."))
    url_title = models.CharField(_("URL title"), max_length=200, blank=True, null=True)

    description = PluginHtmlField(_("description"), blank=True, null=True)

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

    def save(self, *args, **kwargs):
        if appsettings.FLUENTCMS_TEASER_CLEAN_HTML:
            self.description = clean_html(self.description)

        # Remove unwanted tags if requested
        if appsettings.FLUENTCMS_TEASER_SANITIZE_HTML:
            self.description = sanitize_html(self.description)

        super(TeaserItem, self).save(*args, **kwargs)
