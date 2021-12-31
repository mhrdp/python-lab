from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ImportViaShell, ImportViaDjangoImportExportDependencies

# Class to initialize django-import-export
class DjangoImportExportResources(resources.ModelResource):
    class Meta:
        model = ImportViaDjangoImportExportDependencies

class DjangoImportExportAdmin(ImportExportModelAdmin):
    resource_class = DjangoImportExportResources


# Register your models here.
admin.site.register(ImportViaShell)
admin.site.register(ImportViaDjangoImportExportDependencies, DjangoImportExportAdmin)
