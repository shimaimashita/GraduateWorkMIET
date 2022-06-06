import datetime
import uuid

from django.db import models
from django.urls import reverse


class Question(models.Model):
    """Model representing a question."""
    pk_question = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                   help_text='Unique ID for this particular question')
    question = models.TextField(max_length=1000, help_text='Enter a question', default="")
    ACTIVE_STATUS = (
        ('y', 'Yes'),
        ('n', 'No'),
    )

    employed = models.CharField(
        max_length=1,
        choices=ACTIVE_STATUS,
        blank=True,
        default='n',
    )

    studying = models.CharField(
        max_length=1,
        choices=ACTIVE_STATUS,
        blank=True,
        default='n',
    )

    year = models.DateField(default=datetime.date.today())


    def __str__(self):
        """String for representing the Model object."""
        return self.question

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.pk_question)])



class Mailing(models.Model):
    pk_mailing = models.UUIDField(primary_key=True, default=uuid.uuid4)
    mailing_date = models.DateField()

    class Meta:
        ordering = ['-mailing_date']

    def __str__(self):
        return f'{self.pk_mailing} mailing'

    def print_all_question(self):
        return ', '.join(question.question for question in self.question.all()[:4])

    def set_status(self):
        pass

    def get_status(self):
        pass

    def get_year(self):
        return self.mailing_date.strftime('%Y')


class Institute(models.Model):
    institute_name = models.CharField(primary_key=True, max_length=30)

    class Meta:
        ordering = ['-institute_name']

    def __str__(self):
        return f'{self.institute_name}'


class Faculty(models.Model):
    faculty_name = models.CharField(primary_key=True, max_length=30)
    institute = models.ForeignKey('Institute', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['-faculty_name']

    def print_all_groups(self):
        ', '.join(faculty.faculty_name for faculty in self.faculty_name[:4])

    def __str__(self):
        return f'{self.faculty_name}'

    def print_full_name(self):
        pass


class Group(models.Model):
    group_name = models.CharField(primary_key=True, max_length=30)
    faculty = models.ForeignKey('Faculty', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.group_name}'

    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.pk_group)])


class Result(models.Model):
    pk_result = models.UUIDField(primary_key=True, default=uuid.uuid4)
    graduate_number = models.IntegerField()
    answer_number = models.IntegerField()
    causes = models.IntegerField()
    coefficient = models.FloatField()
    employed = models.IntegerField()
    graduate_year = models.DateField()
    mailing = models.ManyToManyField('Mailing')

    class Meta:
        ordering = ['pk_result']

    def __str__(self):
        return f'{self.graduate_year}'

    def get_absolute_url(self):
        return reverse('result-detail', args=[str(self.pk_result)])

    def print_all_mailing(self):
        return ', '.join(mailing.mailing_date for mailing in self.mailing.all()[:4])


class Student(models.Model):
    pk_student = models.BigAutoField(primary_key=True)
    group = models.ForeignKey('Group', on_delete=models.RESTRICT)
    status = models.CharField(max_length=30)

    STUDY_STATUS = (
        ('s', 'Study'),
        ('g', 'Graduate'),
    )

    status = models.CharField(
        max_length=1,
        choices=STUDY_STATUS,
        blank=True,
        default='s',
    )

    mail = models.CharField(max_length=50)
    graduate_year = models.DateField(default=datetime.date.today())

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.pk_student)])

    def __str__(self):
        return f'{self.group} {self.status}'


class Upload(models.Model):
    upload_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)
    file_checked = models.BooleanField(default=False)


# class Book(models.Model):
#     """Model representing a book (but not a specific copy of a book)."""
#     title = models.CharField(max_length=200)
#
#     # Foreign Key used because book can only have one author, but authors can have multiple books
#     # Author as a string rather than object because it hasn't been declared yet in the file
#     author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
#
# summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book') isbn =
# models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a
# href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
#
#     # ManyToManyField used because genre can contain many books. Books can cover many genres.
#     # Genre class has already been defined so we can specify the object above.
#     genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
#     language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return self.title
#
#     def get_absolute_url(self):
#         """Returns the URL to access a detail record for this book."""
#         return reverse('book-detail', args=[str(self.id)])
#
#     def display_genre(self):
#         """Returns list of genres of book, separeted by coma."""
#         return ', '.join(genre.name for genre in self.genre.all()[:3])
#
#     display_genre.short_description = 'Genre'

# class Author(models.Model):
#     """Model representing an author."""
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('Died', null=True, blank=True)
#
#     class Meta:
#         ordering = ['last_name', 'first_name']
#
#     def get_absolute_url(self):
#         """Returns the URL to access a particular author instance."""
#         return reverse('author-detail', args=[str(self.id)])
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.last_name}, {self.first_name}'

# class BookInstance(models.Model):
#     """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
#     book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
#     imprint = models.CharField(max_length=200)
#     due_back = models.DateField(null=True, blank=True)
#     language = models.ForeignKey('Language', on_delete=models.RESTRICT, null=True)
#
# LOAN_STATUS = (
#     ('m', 'Maintenance'),
#     ('o', 'On loan'),
#     ('a', 'Available'),
#     ('r', 'Reserved'),
# )
#
# status = models.CharField(
#     max_length=1,
#     choices=LOAN_STATUS,
#     blank=True,
#     default='m',
#     help_text='Book availability',
# )
#
#     class Meta:
#         ordering = ['due_back']
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.id} ({self.book.title})'
