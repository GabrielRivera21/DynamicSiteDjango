from django.db import models


class Service(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='photos', blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.title
