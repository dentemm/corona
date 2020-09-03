from django.db import models
from django.utils import timezone
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page


class HomePage(Page):

    subtitle = models.CharField(max_length=128, blank=False, default='Preparing for the next pandemic and beyond')
    info = models.CharField(max_length=128, blank=False, default='A Health House scientific learning experience created by Norvell Jefferson')
    date = models.DateTimeField(default=timezone.now)
    discover = models.CharField(max_length=128, blank=False, default='Be one of the first to discover this unique learning experience')

        # Intro
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

HomePage.content_panels = [
    MultiFieldPanel([
        FieldPanel('title', classname='col8'),
        FieldPanel('subtitle', classname='col8'),
        FieldPanel('info', classname='col8'),
        FieldPanel('date', classname='col8'),
        FieldPanel('discover', classname='col8'),
        # FieldRowPanel([
        #     ImageChooserPanel('background_image')
        # ])
    ],  heading='Data',
        classname='collapsible'
    ),
]