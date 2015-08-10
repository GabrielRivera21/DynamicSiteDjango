from django.contrib import admin

from .models import CarouselImage, Feature, AboutUs


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

admin.site.register(CarouselImage, CarouselAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(AboutUs, AboutAdmin)
