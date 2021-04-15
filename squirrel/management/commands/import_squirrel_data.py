from django.core.management.base import BaseCommand
import csv
from datetime import date

from squirrel.models import happySquirrel


class Command(BaseCommand):
    help = 'Import the Squirrel Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        # create a helper function to handle the boolean input
        def handle_boolean(text):
            if text.lower() == 'true':
                return True
            elif text.lower() == 'false':
                return False
            else:
                return 'N/A'
            
        # create a helper function to handle date
        def handle_date(text):
            if len(text) == 8:
                m = text[:2]
                d = text[2:4]
                y = text[4:]
                return y+"-"+m+"-"+d
            else:
                return text

        file_path = options['path']
        with open(file_path) as f:

            reader = csv.reader(f, delimiter=',')
            next(reader, None)

            happySquirrel.objects.all().delete()
            for row in reader:
                if happySquirrel.objects.filter(unique_squirrel_id=row[2]).exists():
                    continue
                squirrel, created = happySquirrel.objects.get_or_create(
                    latitude=float(row[1]),
                    longitude=float(row[0]),
                    unique_squirrel_id=row[2],
                    shift=row[4],
                    date=handle_date(row[5]),
                    age=row[7],
                    primary_fur_color=row[8],
                    color_notes=row[11],
                    location=row[12],
                    specific_location=row[14],
                    running=handle_boolean(row[15]),
                    chasing=handle_boolean(row[16]),
                    climbing=handle_boolean(row[17]),
                    eating=handle_boolean(row[18]),
                    foraging=handle_boolean(row[19]),
                    other_activities=row[20],
                    kuks=handle_boolean(row[21]),
                    quaas=handle_boolean(row[22]),
                    moans=handle_boolean(row[23]),
                    tail_flags=handle_boolean(row[24]),
                    tail_twitches=handle_boolean(row[25]),
                    approaches=handle_boolean(row[26]),
                    indifferent=handle_boolean(row[27]),
                    runs_from=handle_boolean(row[28]),
                    other_interactions=row[29],
                )
                if created:
                    squirrel.save()
