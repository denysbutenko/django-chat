from django.db import models
from django.template.defaultfilters import slugify


class Channel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ("name",)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("channel", (self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Channel, self).save(*args, **kwargs)
