from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sq
import csv
import datetime


class Command(BaseCommand):
    help = 'Export data from csv'

    def add_arguments(self, parser):
        parser.add_argument('filePath', type=str)

    def handle(self, *args, **options):
        filePath = options['filePath']
        with open(filePath, 'w') as f:
            fileWriter = csv.writer(f)
            colNames = [i.name for i in Sq._meta.fields]
            fileWriter.writerow(colNames)
            for sq in Sq.objects.all():
                fileWriter.writerow([getattr(sq, col) for col in colNames])
            self.stdout.write(self.style.SUCCESS('Export Success'))
