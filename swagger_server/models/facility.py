# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Facility(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, facility_id: str=None, name: str=None, active: bool=True, company_id: str=None):  # noqa: E501
        """Facility - a model defined in Swagger

        :param facility_id: The facility_id of this Facility.  # noqa: E501
        :type facility_id: str
        :param name: The name of this Facility.  # noqa: E501
        :type name: str
        :param active: The active of this Facility.  # noqa: E501
        :type active: bool
        :param company_id: The company_id of this Facility.  # noqa: E501
        :type company_id: str
        """
        self.swagger_types = {
            'facility_id': str,
            'name': str,
            'active': bool,
            'company_id': str
        }

        self.attribute_map = {
            'facility_id': 'facility_id',
            'name': 'name',
            'active': 'active',
            'company_id': 'company_id'
        }
        self._facility_id = facility_id
        self._name = name
        self._active = active
        self._company_id = company_id

    @classmethod
    def from_dict(cls, dikt) -> 'Facility':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Facility of this Facility.  # noqa: E501
        :rtype: Facility
        """
        return util.deserialize_model(dikt, cls)

    @property
    def facility_id(self) -> str:
        """Gets the facility_id of this Facility.

        Auto-generated primary key field  # noqa: E501

        :return: The facility_id of this Facility.
        :rtype: str
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id: str):
        """Sets the facility_id of this Facility.

        Auto-generated primary key field  # noqa: E501

        :param facility_id: The facility_id of this Facility.
        :type facility_id: str
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")  # noqa: E501

        self._facility_id = facility_id

    @property
    def name(self) -> str:
        """Gets the name of this Facility.


        :return: The name of this Facility.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Facility.


        :param name: The name of this Facility.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def active(self) -> bool:
        """Gets the active of this Facility.


        :return: The active of this Facility.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this Facility.


        :param active: The active of this Facility.
        :type active: bool
        """

        self._active = active

    @property
    def company_id(self) -> str:
        """Gets the company_id of this Facility.

        This property is a reference to a Company  # noqa: E501

        :return: The company_id of this Facility.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: str):
        """Sets the company_id of this Facility.

        This property is a reference to a Company  # noqa: E501

        :param company_id: The company_id of this Facility.
        :type company_id: str
        """
        if company_id is None:
            raise ValueError("Invalid value for `company_id`, must not be `None`")  # noqa: E501

        self._company_id = company_id
