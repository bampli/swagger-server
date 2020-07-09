# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.facility import Facility  # noqa: E501
from swagger_server.models.wip import Wip  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFacilityController(BaseTestCase):
    """FacilityController integration test stubs"""

    def test_add_facility(self):
        """Test case for add_facility

        Create a new Facility
        """
        body = Facility()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_wip(self):
        """Test case for add_wip

        Create a new Wip
        """
        body = Wip()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_facility(self):
        """Test case for delete_facility

        Delete a Facility
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility/{facilityid}'.format(facilityid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_wip(self):
        """Test case for delete_wip

        Delete a Wip
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip/{wipid}'.format(wipid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_facility(self):
        """Test case for get_facility

        Load an individual Facility
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility/{facilityid}'.format(facilityid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_wip(self):
        """Test case for get_wip

        Load an individual Wip
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip/{wipid}'.format(wipid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_facility(self):
        """Test case for search_facility

        Load the list of Facilities
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"George Street Brewery\"'),
                        ('company_id', '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_wips(self):
        """Test case for search_wips

        Load the list of Wips
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"George Street Brewery\"'),
                        ('facility_id', '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_facility(self):
        """Test case for update_facility

        Update a Facility
        """
        body = Facility()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility/{facilityid}'.format(facilityid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_wip(self):
        """Test case for update_wip

        Update a Wip
        """
        body = Wip()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip/{wipid}'.format(wipid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
