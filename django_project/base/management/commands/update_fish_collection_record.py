from django.core.management.base import BaseCommand
from base.utils.gbif import update_fish_collection_record
from fish.models import FishCollectionRecord


class Command(BaseCommand):
    """Update Fish Collection Record.
    """

    def handle(self, *args, **options):
        fish_collections = FishCollectionRecord.objects.all()
        for record in fish_collections:
            print('Update record : %s' % record.original_species_name)
            update_fish_collection_record(record)
