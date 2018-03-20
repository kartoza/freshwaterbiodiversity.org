# coding=utf-8
"""Tests for models."""
from django.test import TestCase
from django.db.models import signals
from fish.test.model_factories import (
    FishCollectionRecordF,
    TaxonF,
    IUCNStatusF,
)
from fish.models.iucn_status import iucn_status_pre_save_handler
from fish.models.fish_collection_record import \
    fish_collection_post_save_handler


class TestIUCNStatusCRUD(TestCase):
    """
       Tests iucn status.
    """

    def setUp(self):
        """
        Sets up before each test
        """
        pass

    def test_IUCNStatus_create(self):
        """
        Tests iucn status creation
        """
        model = IUCNStatusF.create()

        # check if pk exists
        self.assertTrue(model.pk is not None)

        # check if name exists
        self.assertTrue(model.category is not None)

    def test_IUCNStatus_read(self):
        """
        Tests iucn status model read
        """
        model = IUCNStatusF.create(
            category=u'custom iucn status',
            sensitive=False,
        )

        self.assertTrue(model.category == 'custom iucn status')
        self.assertFalse(model.sensitive)

    def test_IUCNStatus_update(self):
        """
        Tests iucn status model update
        """
        model = IUCNStatusF.create()
        new_data = {
            'category': u'new name',
            'sensitive': False,
        }
        model.__dict__.update(new_data)
        model.save()

        # check if updated
        for key, val in new_data.items():
            self.assertEqual(model.__dict__.get(key), val)

    def test_IUCNStatus_delete(self):
        """
        Tests iucn status model delete
        """
        model = IUCNStatusF.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_signal_registry(self):
        """
        Test signal is registered.
        """
        registered_signal = [r[1]() for r in signals.pre_save.receivers]
        self.assertIn(iucn_status_pre_save_handler, registered_signal)


class TestTaxonCRUD(TestCase):
    """
    Tests taxon.
    """

    def setUp(self):
        """
        Sets up before each test
        """
        pass

    def test_Taxon_create(self):
        """
        Tests taxon creation
        """
        model = TaxonF.create()

        # check if pk exists
        self.assertTrue(model.pk is not None)

        # check if iucn_status exists
        self.assertTrue(model.iucn_status is not None)

        # check if scientific name exists
        self.assertTrue(model.scientific_name is not None)

    def test_Taxon_read(self):
        """
        Tests taxon model read
        """
        iucn_status = IUCNStatusF.create(
            category=u'custom iucn status',
            sensitive=True,
        )
        model = TaxonF.create(
            iucn_status=iucn_status,
            scientific_name=u'custom scientific name',
            common_name=u'custom common name',
            author=u'custom author'
        )

        self.assertTrue(model.iucn_status.category == 'custom iucn status')
        self.assertTrue(model.scientific_name == 'custom scientific name')
        self.assertTrue(model.common_name == 'custom common name')
        self.assertTrue(model.author == 'custom author')

    def test_Taxon_update(self):
        """
        Tests taxon model update
        """
        model = TaxonF.create()
        iucn_status = IUCNStatusF.create(
            category=u'custom iucn status',
            sensitive=True,
        )
        new_data = {
            'iucn_status': iucn_status,
            'scientific_name': u'new scientific name',
            'common_name': u'new common name',
            'author': u'custom author',
        }
        model.__dict__.update(new_data)
        model.save()

        # check if updated
        for key, val in new_data.items():
            self.assertEqual(model.__dict__.get(key), val)

    def test_Taxon_delete(self):
        """
        Tests taxon model delete
        """
        model = TaxonF.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)


class TestFishCollectionRecordCRUD(TestCase):
    """
    Tests fish collection record.
    """
    def setUp(self):
        """
        Sets up before each test
        """
        pass

    def test_FishCollectionRecord_create(self):
        """
        Tests fish collection record creation
        """

        model = FishCollectionRecordF.create()

        # check if pk exists
        self.assertTrue(model.pk is not None)

        # check if site exists
        self.assertTrue(model.site is not None)

        # check if original species name exists
        self.assertTrue(model.original_species_name is not None)

    def test_FishCollectionRecord_read(self):
        """
        Tests fish collection record model read
        """
        model = FishCollectionRecordF.create(
            habitat=u'freshwater',
            original_species_name=u'custom original_species_name',
            present=False,
        )

        self.assertTrue(model.habitat == 'freshwater')
        self.assertTrue(
                model.original_species_name == 'custom original_species_name')

    def test_FishCollectionRecord_update(self):
        """
        Tests fish collection record model update
        """
        model = FishCollectionRecordF.create()
        new_data = {
            'habitat': u'freshwater',
            'original_species_name': u'custom original_species_name update',
            'present': False,
        }
        model.__dict__.update(new_data)

        # check if updated
        for key, val in new_data.items():
            self.assertEqual(model.__dict__.get(key), val)

    def test_FishCollectionRecord_delete(self):
        """
        Tests fish collection record model delete
        """
        model = FishCollectionRecordF.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)
