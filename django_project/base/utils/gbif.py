# coding: utf-8
from requests.exceptions import HTTPError
from pygbif import species
from fish.models import Taxon, FishCollectionRecord


def update_taxa():
    """Get all taxon, then update the data based on the gbif id.
    """
    taxa = Taxon.objects.all()
    for taxon in taxa:
        print('Update taxon for %s with gbif id %s' % (
            taxon.common_name, taxon.gbif_id
        ))
        try:
            response = species.name_usage(key=taxon.gbif_id)
            if response:
                taxon.common_name = response['canonicalName']
                taxon.scientific_name = response['scientificName']
                taxon.author = response['authorship']
                taxon.save()
                print('Taxon updated')
        except HTTPError as e:
            print('Taxon not updated')
            print(e)


def update_fish_collection_record(fish_collection_id=None):
    """
    Check fish record if there is a matching taxon for the species
    name in the taxon table. If there is not
    we need to do a name search using pygbif to
    fetch the authoriative name and GBIF taxon id,
    """
    if not fish_collection_id:
        fish_collections = FishCollectionRecord.objects.all()
        for record in fish_collections:
            print('Update record : %s' % record.original_species_name)
            response = species.name_lookup(
                    q=record.original_species_name,
                    limit=3,
                    offset=2)
            results = response['results']
            if not results:
                continue

            for result in results:
                if 'nubKey' in result:
                    taxon, created = Taxon.objects.get_or_create(
                            gbif_id=result['nubKey'])
                    taxon.common_name = result['canonicalName']
                    taxon.scientific_name = result['scientificName']
                    taxon.author = result['authorship']
                    taxon.save()
                    record.taxon_gbif_id = taxon
                    record.save()
                    continue
