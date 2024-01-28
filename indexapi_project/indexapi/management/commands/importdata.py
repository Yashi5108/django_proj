# indexapi/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
from indexapi.models import Index, DailyPrice

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        # Add your logic to read and import data from the CSV file
        # Example: Read CSV and create Index and DailyPrice objects
        with open('your_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                index, created = Index.objects.get_or_create(name=row['index_name'])
                DailyPrice.objects.create(
                    index=index,
                    date=row['date'],
                    open_price=row['open'],
                    high_price=row['high'],
                    low_price=row['low'],
                    close_price=row['close'],
                    shares_traded=row['shares_traded'],
                    turnover=row['turnover'],
                    # Add other fields
                )
