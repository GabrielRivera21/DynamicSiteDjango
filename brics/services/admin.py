from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'title',
        'description',
    )

    list_filter = ('is_active',)
    search_fields = ('title', 'description',)

admin.site.register(Service, ServiceAdmin)
