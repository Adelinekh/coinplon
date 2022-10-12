from email.policy import default
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
import lorem

class FlexPage(Page):
    class Meta :
        verbose_name = "Page divers"
        verbose_name_plural = "Pages divers"


    text = models.TextField(
        blank = True,
        null=True,
        max_length = 500,
        default = lorem.paragraph()
    )

    content_panels = Page.content_panels + [
        FieldPanel("text")
    ]
    
