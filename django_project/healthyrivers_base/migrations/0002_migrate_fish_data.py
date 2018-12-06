import json
from django.db import migrations, models
from bims.models.biological_collection_record import (
    collection_post_save_handler,
    collection_post_save_update_cluster
)


def move_fish_data(apps, schema_editor):
    try:
        BioCollectionRecords = apps.get_model('bims',
                                              'BiologicalCollectionRecord')
        Fish = apps.get_model('fish', 'FishCollectionRecord')
    except LookupError:
        return
    models.signals.post_save.disconnect(
        collection_post_save_handler
    )
    models.signals.post_save.disconnect(
        collection_post_save_update_cluster
    )
    fishes = Fish.objects.filter(
        habitat__isnull=False
    )
    for fish in fishes:
        bio = BioCollectionRecords.objects.get(
            id=fish.id
        )

        additional_data = {}

        if fish.depth_cm:
            additional_data['depth_cm'] = fish.depth_cm
        if fish.near_bed_velocity:
            additional_data['near_bed_velocity'] = fish.near_bed_velocity
        if fish.substrate:
            additional_data['substrate'] = fish.substrate
        if fish.ec:
            additional_data['substrate'] = fish.ec
        if fish.ph:
            additional_data['ph'] = fish.ph
        if fish.do:
            additional_data['do'] = fish.do
        if fish.temp:
            additional_data['temp'] = fish.temp
        if fish.turbidity:
            additional_data['turbidity'] = fish.turbidity
        if fish.hydraulic_biotope:
            additional_data['hydraulic_biotope'] = fish.hydraulic_biotope
        if fish.fbis_site_code:
            additional_data['fbis_site_code'] = fish.fbis_site_code

        if additional_data:
            print("Found additional data for %s" % fish.id)
            additional_data_json = json.dumps(additional_data)
            bio.additional_data = additional_data_json
            bio.save()

    models.signals.post_save.connect(
        collection_post_save_handler
    )
    models.signals.post_save.connect(
        collection_post_save_update_cluster
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('healthyrivers_base', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            move_fish_data
        ),
    ]
