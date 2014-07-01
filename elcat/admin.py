# coding=utf-8
__author__ = 'taksenov'

from django.contrib import admin
from django import forms
from elcat.models import book, bookstotal, booksatlibrary, author, bbk1, bbk2, genre, series, content, publisher, language, shelfplace, library, librarytown

# class BookAdminForm(forms.ModelForm):
#     class Meta:
#         model = book
#     authors = forms.ModelChoiceField(queryset=book.objects.prefetch_related('author_id').all())

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'library', 'librarytown', 'genre')
    search_fields = ('name',)
    list_filter = ('library',)
    raw_id_fields = (
#                     'author_id',
                     'bbk1', 'bbk2', 'genre', 'series', 'content', 'publisher', 'language', 'shelfplace', 'library', 'librarytown')
#    filter_horizontal = ('author_id',)
#     form = BookAdminForm

class BooksAtLibraryAdmin(admin.ModelAdmin):
    list_display = ('library',)



# class UserProfile(models.Model):
#   name = models.CharField()
#   info = models.OneToOneField(UserInfo, related_name='user')
#
# class UserInfo(models.Model):
#   def __unicode__(self):
#     return self.user.__unicode__() + self.age
#   age = models.IntegerField()
#
# class Ticket(models.Model):
#   userinfo = models.ForeignKey(UserInfo)

# ===================================
# class TicketAdminForm(forms.ModelForm):
#   class Meta:
#     model = Ticket
#   userinfo = forms.ModelChoiceField(queryset=UserInfo.objects.prefetch_related('user').all())
#
# class TicketAdmin(admin.ModelAdmin):
#   form = TicketAdminForm
#
# admin.site.register(Ticket, TicketAdmin)


admin.site.register(book, BookAdmin)
admin.site.register(bookstotal)
admin.site.register(booksatlibrary, BooksAtLibraryAdmin)
# admin.site.register(author)
# admin.site.register(bbk1)
# admin.site.register(bbk2)
# admin.site.register(genre)
# admin.site.register(series)
# admin.site.register(content)
# admin.site.register(publisher)
# admin.site.register(language)
# admin.site.register(shelfplace)
#admin.site.register(library)
#admin.site.register(librarytown)