# coding: utf-8
from requests.exceptions import HTTPError
from pygbif import species
from fish.models import Taxon


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
