from django.core.management.base import BaseCommand
from base.utils.gbif import update_fish_collection_record


class Command(BaseCommand):
    """Update Fish Collection Record.
    """

    def handle(self, *args, **options):
        update_fish_collection_record()
