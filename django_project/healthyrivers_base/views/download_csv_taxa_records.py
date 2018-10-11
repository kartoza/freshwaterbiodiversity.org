# coding=utf-8
import csv
from django.http import HttpResponse
from bims.models.biological_collection_record import BiologicalCollectionRecord
from bims.models.taxon import Taxon


def download_csv_site_taxa_records(request, taxon_id):
    records = BiologicalCollectionRecord.objects.filter(
        taxon_gbif_id=taxon_id
    )
    fields = [f.name for f in BiologicalCollectionRecord._meta.get_fields()]
    fields.remove('ready_for_validation')
    fields.remove('validated')
    fields.remove('fishcollectionrecord')

    taxon = Taxon.objects.get(pk=taxon_id)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename="'+ taxon.common_name +'.csv"'

    writer = csv.writer(response)
    writer.writerow(['Taxon', taxon.common_name])
    writer.writerow(['Total records', len(records)])
    writer.writerow(['GBIF ID', taxon.gbif_id])
    writer.writerow([''])
    writer.writerow(fields)

    for record in records:
        row_object = []
        for field in fields:
            row_object.append(getattr(record, field))
        writer.writerow(row_object)

    return response
