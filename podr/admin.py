from django.contrib import admin
from podr.models import Subscription, Episode


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 3


class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'link']}),
        ('Date information', {'fields': ['last_updated'], 'classes': ['collapse']}),
    ]
    date_hierarchy = 'last_updated'
    inlines = [EpisodeInline]
    list_display = ('title', 'last_updated')
    search_fields = ['title']

admin.site.register(Subscription, SubscriptionAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'subscription']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    date_hierarchy = 'pub_date'
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Episode, EpisodeAdmin)