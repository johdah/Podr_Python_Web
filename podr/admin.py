from django.contrib import admin
from podr.models import Podcast, Episode, UserPodcast, UserEpisode, Category, PodcastCategories, UserProfile, UserFollowing


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General',             {'fields': ['title', 'level', 'parent']}),
    ]
    list_display = ('title', 'level', 'parent')
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)


class PodcastAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General',             {'fields': ['title', 'link', 'copyright', 'description', 'language']}),
        ('iTunes information',  {'fields': ['itunes_author', 'itunes_subtitle', 'itunes_summary', 'itunes_image',
                                            'itunes_owner_name', 'itunes_owner_email', 'itunes_block',
                                            'itunes_complete', 'itunes_explicit'], 'classes': ['collapse']}),
        ('Date information',    {'fields': ['last_updated'], 'classes': ['collapse']}),
    ]
    date_hierarchy = 'last_updated'
    inlines = [EpisodeInline]
    list_display = ('title', 'last_updated')
    search_fields = ['title']

admin.site.register(Podcast, PodcastAdmin)
admin.site.register(PodcastCategories)


class EpisodeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['podcast', 'title', 'guid', 'enclosureUrl', 'enclosureLength', 'enclosureType']}),
        ('iTunes information',  {'fields': ['itunes_author', 'itunes_subtitle', 'itunes_summary', 'itunes_duration',
                                            'itunes_image', 'itunes_block', 'itunes_explicit'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    date_hierarchy = 'pub_date'
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Episode, EpisodeAdmin)

admin.site.register(UserEpisode)
admin.site.register(UserFollowing)
admin.site.register(UserPodcast)
admin.site.register(UserProfile)