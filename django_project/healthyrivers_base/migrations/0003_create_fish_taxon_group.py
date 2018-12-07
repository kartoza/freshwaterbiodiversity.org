from django.db import migrations
from bims.enums.taxonomic_group_category import TaxonomicGroupCategory


def create_fish_taxon_group(apps, schema_editor):
    try:
        TaxonGroup = apps.get_model('bims', 'TaxonGroup')
        Taxonomy = apps.get_model('bims', 'Taxonomy')
    except LookupError:
        return

    taxon_group, status = TaxonGroup.objects.get_or_create(
        name='Fish',
        category=TaxonomicGroupCategory.SPECIES_MODULE.name
    )

    # From http://www.fishbase.org/tools/Classification/ClassificationList.php
    fish_classes = [
        'Myxini',
        'Cephalaspidomorphi',
        'Elasmobranchii',
        'Holocephali',
        'Actinopterygii',
        'Sarcopterygii'
    ]

    for fish_class in fish_classes:
        try:
            taxonomy = Taxonomy.objects.get(
                scientific_name=fish_class
            )
            print('Found taxonomy %s' % taxonomy.scientific_name)
            taxon_group.taxonomies.add(taxonomy)
            taxon_group.save()
        except Taxonomy.DoesNotExist:
            continue

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('healthyrivers_base', '0002_migrate_fish_data'),
    ]

    operations = [
        migrations.RunPython(
            create_fish_taxon_group
        ),
    ]
