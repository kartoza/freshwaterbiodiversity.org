# coding=utf-8
"""Tests for models."""
from django.test import TestCase
from base.test.model_factories import LocationTypeF


class TestLocationTypeCRUD(TestCase):
    """
    Tests location type.
    """
    def setUp(self):
        """
        Sets up before each test
        """
        pass

    def test_LocationType_create(self):
        """
        Tests location type creation
        """
        model = LocationTypeF.create()

        # check if pk exists
        self.assertTrue(model.pk is not None)

        # check if name exists
        self.assertTrue(model.name is not None)

        # check if description exists
        self.assertTrue(model.description is not None)
