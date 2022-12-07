from django.shortcuts import render
from django.views import generic
from django.views import View
from .models import Chapter, Sermon, Verse, Event, About, AboutFounder, Giving, ImageSlider, ServiceSchedule, Belief
from django.core.paginator import Paginator

# Create your views here.

class IndexPageView(View):
    def get(self, *args, **kwargs):

        landing_images = ImageSlider.objects.all().order_by('-created_at')[:4]
        sermons = Sermon.objects.all().order_by('-created_at')[:4]
        chapters = Chapter.objects.all().order_by('-created_at')
        verses = Verse.objects.all().order_by('-created_at')[:1]
        events = Event.objects.all().order_by('-created_at')[:3]
        timing = ServiceSchedule.objects.all()[:1]
        founder = AboutFounder.objects.all()[:1]
        beliefs = Belief.objects.all()[:1]
        about = About.objects.all()


        context = {
            'chapters': chapters,
            'sermons': sermons,
            'verses': verses,
            'events': events,
            'about_us': about,
            'founders': founder,
            'images': landing_images,
            'timings': timing,
            'beliefs': beliefs
        }
        return render(self.request, 'pages/index.html', context=context)




# Giving
class GivingView(View):
    def get(self, *args, **kwargs):
        giving_types = Giving.objects.all()

        context = {
            'givings': giving_types
        }
        return render(self.request, 'pages/giving.html', context)



# Chapter Detail View
class ChapterDetailView(generic.DetailView):
    slug_field = 'slug'
    context_object_name = 'chapter'
    template_name = 'pages/chapter.html'
    

    def get_queryset(self):
        queryset = Chapter.objects.filter(slug=self.kwargs['slug'])
        return queryset 



# Sermons ListView
class FounderSermons(View):
    def get(self, *args, **kwargs):
        sermons = Sermon.objects.filter(
            interdenominational=True
        ).order_by('-created_at')

        # pagination
        paginator = Paginator(sermons, 1)
        page = self.request.GET.get('page')
        paged_sermons = paginator.get_page(page)


        context = {
            'sermons': paged_sermons
        }
        return render(self.request, 'pages/sermons.html', context)


# Events List
class EventList(View):
    def get(self, *args, **kwargs):

        events = Event.objects.all().order_by('-created_at')

         # pagination
        paginator = Paginator(events, 1)
        page = self.request.GET.get('page')
        paged_events = paginator.get_page(page)

        context = {
            'events': paged_events
        }
        return render(self.request, 'pages/events.html', context)




# About Us
class AboutUsDetailView(generic.DetailView):
    slug_field = 'slug'
    context_object_name = 'about'
    template_name = 'pages/about.html'

    def get_queryset(self):
        queryset = About.objects.filter(slug=self.kwargs['slug'])
        return queryset 




# Founder
class FounderDetailView(generic.DetailView):
    slug_field = 'slug'
    context_object_name = 'founder'
    template_name = 'pages/founder.html'

    def get_queryset(self):
        queryset = AboutFounder.objects.filter(slug=self.kwargs['slug'])
        return queryset