from django.core.management.base import BaseCommand, CommandError
import csv

from squirrel.models import happySquirrel


class Command(BaseCommand):
    help = 'Export the Squirrel data to csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        meta = happySquirrel._meta
        fields = [f.name for f in meta.fields]

        with open(options['path'], 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            for obj in happySquirrel.objects.all():
                writer.writerow([getattr(obj, att) for att in fields])
