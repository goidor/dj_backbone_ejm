from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib import admin

class Entry(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    slug = models.SlugField(max_length=50, blank=True)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)


# Admin Site
admin.site.register(Entry)
