# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cyclo import Cyclo  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.stage import Stage  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCycloController(BaseTestCase):
    """CycloController integration test stubs"""

    def test_add_cyclo(self):
        """Test case for add_cyclo

        Create a new Cyclo
        """
        body = Cyclo()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_stage(self):
        """Test case for add_stage

        Create a new Stage
        """
        body = Stage()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_task(self):
        """Test case for add_task

        Create a new Task
        """
        body = Task()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_cyclo(self):
        """Test case for delete_cyclo

        Delete a Cyclo
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo/{cycloid}'.format(cycloid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_stage(self):
        """Test case for delete_stage

        Delete a Stage
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage/{stageid}'.format(stageid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task(self):
        """Test case for delete_task

        Delete a Task
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task/{taskid}'.format(taskid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cyclo(self):
        """Test case for get_cyclo

        Load an individual Cyclo
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo/{cycloid}'.format(cycloid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stage(self):
        """Test case for get_stage

        Load an individual Stage
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage/{stageid}'.format(stageid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task(self):
        """Test case for get_task

        Load an individual Task
        """
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task/{taskid}'.format(taskid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_cyclos(self):
        """Test case for search_cyclos

        Load the list of Cyclos
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"George Street Brewery\"'),
                        ('company_id', '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_stages(self):
        """Test case for search_stages

        Load the list of Stages
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"Painting\"'),
                        ('cyclo_id', '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_tasks(self):
        """Test case for search_tasks

        Load the list of Tasks
        """
        query_string = [('size', 10),
                        ('page', 1),
                        ('sort', '\"name ASC\"'),
                        ('name', '\"George Street Brewery\"'),
                        ('stage_id', '\"0e8cedd0-ad98-11e6-bf2e-47644ada7c0f\"')]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_cyclo(self):
        """Test case for update_cyclo

        Update a Cyclo
        """
        body = Cyclo()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo/{cycloid}'.format(cycloid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_stage(self):
        """Test case for update_stage

        Update a Stage
        """
        body = Stage()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage/{stageid}'.format(stageid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task(self):
        """Test case for update_task

        Update a Task
        """
        body = Task()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task/{taskid}'.format(taskid='\"0e8c9fb0-ad98-11e6-bf2e-47644ada7c0f\"'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
