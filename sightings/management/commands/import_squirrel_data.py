from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sq
import csv
import datetime

def importData(filePath):
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sq = Sq(
                X=row['X'],
                Y=row['Y'],
                uid=row['Unique Squirrel ID'],
                hectare=row['Hectare'],
                shift=row['Shift'],
                date=datetime.datetime.strptime(row['Date'], "%m%d%Y").date(),
                hectarenumber=row['Hectare Squirrel Number'],
                age=row['Age'],
                color=row['Primary Fur Color'],
                hcolor=row['Highlight Fur Color'],
                ccolor=row['Combination of Primary and Highlight Color'],
                cnotes=row['Color notes'],
                location=row['Location'],
                measurement=row['Above Ground Sighter Measurement'],
                slocation=row['Specific Location'],
                running=row['Running'],
                chasing=row['Chasing'],
                climbing=row['Climbing'],
                eating=row['Eating'],
                foraging=row['Foraging'],
                otheract=row['Other Activities'],
                kuks=row['Kuks'],
                quaas=row['Quaas'],
                moans=row['Moans'],
                tflag=row['Tail flags'],
                ttwitch=row['Tail twitches'],
                approach=row['Approaches'],
                idiff=row['Indifferent'],
                runsfrom=row['Runs from'],
                otherinter=row['Other Interactions'],
                ll=row['Lat/Long'],
                zc=row['Zip Codes'],
                cdistricts=row['Community Districts'],
                bb=row['Borough Boundaries'],
                ccd=row['City Council Districts'],
                pp=row['Police Precincts'])
            sq.save()

class Command(BaseCommand):
    help = 'Import data from csv'

    def add_arguments(self, parser):
        parser.add_argument('filePaths', nargs='+', type=str)

    def handle(self, *args, **options):
        for filePath in options['filePaths']:
            importData(filePath)

            self.stdout.write(self.style.SUCCESS('Import Success'))
