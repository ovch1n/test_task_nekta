from django.contrib import admin
from contents.models import *

class RequestMessageInline(admin.TabularInline):
    model = RequestMessage
    fields = ('user', 'created_at', 'content',)
    readonly_fields = ('created_at',)
    list_display = ['user', 'created_at', 'content',]
    extra = 0

class RequestAdmin(admin.ModelAdmin):
    model = Request
    fields = ('title', 'user', 'created_at',)
    readonly_fields = ('created_at',)
    list_display = ['title', 'user', 'created_at',]
    search_fields = ('title', 'user', 'created_at',)
    inlines = [
        RequestMessageInline,
    ]

admin.site.register(Request, RequestAdmin)
