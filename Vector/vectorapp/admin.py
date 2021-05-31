from django.contrib import admin

from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name')
    list_display_links = ('id', 'last_name')

admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name')
    list_display_links = ('id', 'last_name')

admin.site.register(Teacher, TeacherAdmin)

class DiscAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Disciplines, DiscAdmin)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date')
    list_display_links = ('id', 'title')

admin.site.register(Articles, PostsAdmin)


