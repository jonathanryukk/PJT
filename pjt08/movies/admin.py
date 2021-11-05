from django.contrib import admin

from movies.models import Actor, Movie, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Actor)
