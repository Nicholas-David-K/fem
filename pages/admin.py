from django.contrib import admin
from .models import Chapter, Sermon, Verse, Event, About, AboutFounder, Book, Giving, ImageSlider, ServiceSchedule, Belief, Testimony
# Register your models here.





class ChapterModelAdmin(admin.ModelAdmin):
    list_display = ('chapter_name', 'url')
    list_display_links = ('chapter_name', 'url')
admin.site.register(Chapter, ChapterModelAdmin)


class SermonModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'url', 'interdenominational')
    list_display_links = ('title', 'url')
    list_editable = ('interdenominational',)
admin.site.register(Sermon, SermonModelAdmin)



admin.site.register(Verse)


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date', 'time', 'location')
    list_display_links = ('event_title',)
admin.site.register(Event, EventModelAdmin)



admin.site.register(About)
admin.site.register(AboutFounder)



class BookModelAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'author', 'purchase_url')
    list_display_links = ('book_title', 'purchase_url')
admin.site.register(Book, BookModelAdmin)




class GivingModelAdmin(admin.ModelAdmin):
    list_display = ('giving_type', 'inverted')
    list_display_links = ('giving_type',)
    list_editable = ('inverted',)
admin.site.register(Giving, GivingModelAdmin)



admin.site.register(ImageSlider)
admin.site.register(ServiceSchedule)
admin.site.register(Belief)


class TestimonyModelAdmin(admin.ModelAdmin):
    list_display = ('full_name','testimony_subject', 'email', 'read')
    list_display_links = ('full_name', 'testimony_subject')
    list_editable = ('read',)
admin.site.register(Testimony, TestimonyModelAdmin)