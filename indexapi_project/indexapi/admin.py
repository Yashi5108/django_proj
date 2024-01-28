from django.contrib import admin
from .models import Index, DailyPrice
from .forms import IndexCSVUploadForm

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    form = IndexCSVUploadForm
    list_display = ['name', 'csv_file']
    search_fields = ['name']
