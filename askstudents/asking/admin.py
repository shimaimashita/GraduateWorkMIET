from django.contrib import admin

from .models import Mailing, Question, Faculty, Group, Student, Result, Institute


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk_question',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk_mailing', 'mailing_date')


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('institute_name',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'institute')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'faculty')

#
# class BookInline(admin.StackedInline):
#    model = Book
#
# class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('last_name', 'first_name',
#                    'date_of_birth', 'date_of_death')
#
#    fields = ['first_name', 'last_name',
#            ('date_of_birth', 'date_of_death')]
#
#    inlines = [BookInline]
#
#
#
## admin.site.register(Author)
## admin.site.register(Book)
## admin.site.register(BookInstance)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Genre)
# admin.site.register(Language)
#
#
# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#    list_display = ('book', 'status', 'due_back', 'id')
#    list_filter = ('status', 'due_back')
#    fieldsets = (
#            (None, {
#                'fields': ('book', 'imprint', 'id')
#            }),
#            ('Availability', {
#                'fields': ('status', 'due_back')
#            }),
#    )
#
# class BookInstanceInline(admin.StackedInline):
#    model = BookInstance
#
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'author', 'display_genre')
#
#    inlines = [BookInstanceInline]
