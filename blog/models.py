from django.db import models
from markdownx.models import MarkdownxField
import markdown
from home.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
)
from django.utils import timezone
from markdownx.utils import markdownify
# Create your models here.

class Tag(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    contents = MarkdownxField('Contents', help_text='To Write with Markdown format')
    created_time = models.DateTimeField('Createded Time' , default = timezone.now)
    tags = models.ManyToManyField(Tag, related_name='posts_tags')
    publish = models.BooleanField('flag of publication', default = False)
    published_time =  models.DateTimeField('Pblished Time', blank=True, null=True)

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.contents)
    
    def table_of_contents(self):
        md = markdown.Markdown(
            text=self.contents,
            extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
        )
        html = md.convert(self.contents)
        toc_blog = md.toc
        return toc_blog
    def save(self, *args, **kwargs):
        if self.publish and not self.published_time:
            self.published_time = timezone.now()
        super().save(*args, **kwargs)
