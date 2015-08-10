from django.contrib import admin

from .models import (CarouselImage, Feature,
                     AboutUs, Footer)


class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'title',
        'description',
        'is_active',
    )

    list_filter = ('is_active',)
    search_fields = ('title', 'description',)


class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'title',
        'description',
        'is_active',
    )

    list_filter = ('is_active',)
    search_fields = ('title', 'description',)


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'header',
        'description',
        'is_active',
    )

    list_filter = ('is_active',)
    search_fields = ('header', 'description',)


class FooterAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'head_title',
        'description',
        'is_active',
    )
    list_filter = ('is_active',)
    search_fields = ('head_title', 'description',)

admin.site.register(CarouselImage, CarouselAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(AboutUs, AboutAdmin)
admin.site.register(Footer, FooterAdmin)
