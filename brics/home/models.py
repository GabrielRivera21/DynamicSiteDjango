from django.db import models


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='photos')
    order = models.IntegerField(help_text="Place you want to put this image in the carousel.")
    title = models.CharField(max_length=45, help_text="Image Title")
    description = models.TextField(blank=True, help_text="Image Description")
    header = models.CharField(max_length=45, blank=True, help_text="The title header in home page.")
    sub_header = models.TextField(blank=True,
                                  help_text="Something you want to say in the image in the home page.")
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.title


class Feature(models.Model):
    image = models.ImageField(upload_to='photos', blank=True)
    order = models.IntegerField()
    title = models.CharField(max_length=45)
    description = models.TextField()
    detail_button_link = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.title


class AboutUs(models.Model):
    header = models.CharField(max_length=45)
    description = models.TextField()
    order = models.IntegerField()
    image = models.ImageField(upload_to='photos', blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.header


class Footer(models.Model):
    head_title = models.CharField(max_length=45)
    description = models.TextField()
    order = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.head_title
