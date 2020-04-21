from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from meadow.models import Book, BookAuthor


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class BookResourceAdmin(ImportExportModelAdmin):
    resource_class = BookResource


class BookAuthorResource(resources.ModelResource):
    class Meta:
        model = BookAuthor


class BookAuthorResourceAdmin(ImportExportModelAdmin):
    resource_class = BookAuthorResource


admin.site.register(BookAuthor, BookAuthorResourceAdmin)
admin.site.register(Book, BookResourceAdmin)
