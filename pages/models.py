from django.db import models
from pages.slug import unique_slugify
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# images
import uuid
import os


def image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4}.{ext}"
    return os.path.join('photos/', filename)


# Books Model
class Founder(models.Model):
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    founder_photo = models.ImageField(upload_to=image_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subtitle



# Chapter Model
class Chapter(models.Model):
    chapter_name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    service_plan = models.TextField()
    url = models.URLField()
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    front_photo = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    pastor_photo = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_1 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_2 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_3 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_4 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_5 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_6 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # slugify
            slug_str = "%s %s %s" % (self.chapter_name, self.created_at, self.subtitle)
            unique_slugify(self, slug_str)
            
        return super(Chapter, self).save()

    def __str__(self):
        return self.chapter_name




# Sermon Model
class Sermon(models.Model):
    title = models.CharField(max_length=150)
    speaker = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField()
    banner = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    interdenominational = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.speaker} • {self.title}"



# Landing page Images
class ImageSlider(models.Model):
    caption = models.CharField(blank=True, null=True, max_length=50)
    image = models.ImageField(upload_to=image_file_path)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name = 'Landing Page Image'


    def __str__(self):
        if self.caption:
            return self.caption
        return f"No Caption"
    


# Verse of Week
class Verse(models.Model):
    book = models.CharField(max_length=50)
    verse = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.verse




# Events
class Event(models.Model):
    event_title = models.CharField(max_length=150)
    event_date = models.DateField()
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    description = models.TextField()
    banner = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    inverted = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_title



class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_subtitle = models.CharField(max_length=100)
    description = models.TextField()
    banner_image = models.ImageField(upload_to=image_file_path)
    photo_1 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_2 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    photo_3 = models.ImageField(blank=True, null=True, upload_to=image_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)


    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def save(self, *args, **kwargs):
        if not self.id:
            # slugify
            slug_str = "%s %s %s" % (self.about_title, self.created_at, self.about_subtitle)
            unique_slugify(self, slug_str)
            
        return super(About, self).save()

    def __str__(self):
        return self.about_title



class Book(models.Model):   
    book_title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    purchase_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=image_file_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title



# Giving
class Giving(models.Model):
    giving_type = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    png = models.ImageField(upload_to=image_file_path)
    inverted = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Giving'
        verbose_name_plural = 'Giving'


    def __str__(self):
        return self.giving_type





# Founder
class AboutFounder(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    books = models.ManyToManyField("Book", blank=True, null=True)
    photo = models.ImageField(upload_to=image_file_path)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = 'Founder'
        verbose_name_plural = 'About the Founder'


    def save(self, *args, **kwargs):

        if not self.id:
            # slugify
            slug_str = "%s %s %s" % (self.title, self.created_at, self.subtitle)
            unique_slugify(self, slug_str)
            
        return super(AboutFounder, self).save()


    def __str__(self):
        return self.name




# Service Schedule
class ServiceSchedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    timing = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.timing}"



# What We Believe
class Belief(models.Model):
    title = models.CharField(max_length=100)
    what_we_believe = models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


    def __str__(self):
        return self.title