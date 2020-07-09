# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCompanyController(BaseTestCase):
    """CompanyController integration test stubs"""

    def test_add_company(self):
        """Test case for add_company

        Create a new Company
        """
        body = Company()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_product(self):
        """Test case for add_product

        Create a new Product
        """
        body = Product()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_company(self):
        """Test case for delete_company

        Delete a Company
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company/{companyid}'.format(companyid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product(self):
        """Test case for delete_product

        Delete a Product
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product/{productid}'.format(productid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_company(self):
        """Test case for get_company

        Load an individual Company
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company/{companyid}'.format(companyid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product(self):
        """Test case for get_product

        Load an individual Product
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product/{productid}'.format(productid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_companies(self):
        """Test case for search_companies

        Load the list of Companies
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"George Street Brewery\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_products(self):
        """Test case for search_products

        Load the list of Products
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"George Street Brewery\"'),
                        ('company_id', '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_company(self):
        """Test case for update_company

        Update a Company
        """
        body = Company()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company/{companyid}'.format(companyid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Update a Product
        """
        body = Product()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product/{productid}'.format(productid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
