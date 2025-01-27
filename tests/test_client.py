"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

from client.client import Client
import unittest

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Sahil", "Choudhary", "schoudhary4@rrc.ca")
    
    def test_initialization_with_valid_inputs(self):
        expected = Client(1, "Sahil", "Choudhary", "schoudhary4@rrc.ca")

        self.assertEqual(1, expected._Client__client_number)
        self.assertEqual("Sahil", expected._Client__first_name)
        self.assertEqual("Choudhary", expected._Client__last_name)
        self.assertEqual("schoudhary4@rrc.ca", expected._Client__email_address)

    def test_invalid_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client("one", "Sahil", "Choudhary", "schoudhary4@rrc.ca")

    def test_blank_first_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client(1, " ", "Choudhary", "schoudhary4@rrc.ca")

    def test_blank_last_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client(1, "Sahil", " ", "schoudhary4@rrc.ca")

    def test_invalid_email_address_sets_default_value(self):
        invalid_email = "invalid-email"
        expected = Client(1, "Sahil", "Choudhary", invalid_email)

        self.assertEqual("email@pixell-river.com", expected._Client__email_address)

    def test_client_number_property_returns_client_number(self):
        self.assertEqual(1, self.client.client_number)

    def test_first_name_property_returns_first_name(self):
        self.assertEqual("Sahil", self.client.first_name)

    def test_last_name_property_returns_last_name(self):
        self.assertEqual("Choudhary", self.client.last_name)

    def test_email_address_property_returns_email_address(self):
        self.assertEqual("schoudhary4@rrc.ca", self.client.email_address)

    def test_string_representation_returns_formatted_string(self):
        expected = "Choudhary, Sahil [1] - schoudhary4@rrc.ca\n"
        
        self.assertEqual(expected, str(self.client))
