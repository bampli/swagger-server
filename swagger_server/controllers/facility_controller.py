import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.facility import Facility  # noqa: E501
from swagger_server.models.wip import Wip  # noqa: E501
from swagger_server import util


def add_facility(body):  # noqa: E501
    """Create a new Facility

    Adds a Facility # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Facility
    """
    if connexion.request.is_json:
        body = Facility.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_wip(body):  # noqa: E501
    """Create a new Wip

    Adds a Wip # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Wip
    """
    if connexion.request.is_json:
        body = Wip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_facility(facilityid):  # noqa: E501
    """Delete a Facility

    Deletes a Facility # noqa: E501

    :param facilityid: Identifier of the Facility
    :type facilityid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_wip(wipid):  # noqa: E501
    """Delete a Wip

    Deletes a Wip # noqa: E501

    :param wipid: Identifier of the Wip
    :type wipid: str

    :rtype: None
    """
    return 'do some magic!'


def get_facility(facilityid):  # noqa: E501
    """Load an individual Facility

    Loads a Facility # noqa: E501

    :param facilityid: Identifier of the Facility
    :type facilityid: str

    :rtype: Facility
    """
    return 'do some magic!'


def get_wip(wipid):  # noqa: E501
    """Load an individual Wip

    Loads a Wip # noqa: E501

    :param wipid: Identifier of the Wip
    :type wipid: str

    :rtype: Wip
    """
    return 'do some magic!'


def search_facility(size=None, page=None, sort=None, name=None, company_id=None):  # noqa: E501
    """Load the list of Facilities

    Loads list of Facilities # noqa: E501

    :param size: Size of the page to retrieve.
    :type size: int
    :param page: Number of the page to retrieve.
    :type page: float
    :param sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC
    :type sort: str
    :param name: Allows to filter the collections of result by name
    :type name: str
    :param company_id: Allows to filter the collections of result by company_id
    :type company_id: str

    :rtype: List[Facility]
    """
    return 'do some magic!'


def search_wips(size=None, page=None, sort=None, name=None, facility_id=None):  # noqa: E501
    """Load the list of Wips

    Loads list of Wips # noqa: E501

    :param size: Size of the page to retrieve.
    :type size: int
    :param page: Number of the page to retrieve.
    :type page: float
    :param sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC
    :type sort: str
    :param name: Allows to filter the collections of result by name
    :type name: str
    :param facility_id: Allows to filter the collections of result by facility_id
    :type facility_id: str

    :rtype: List[Wip]
    """
    return 'do some magic!'


def update_facility(body, facilityid):  # noqa: E501
    """Update a Facility

    Stores a Facility # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param facilityid: Identifier of the Facility
    :type facilityid: str

    :rtype: Facility
    """
    if connexion.request.is_json:
        body = Facility.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_wip(body, wipid):  # noqa: E501
    """Update a Wip

    Stores a Wip # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param wipid: Identifier of the Wip
    :type wipid: str

    :rtype: Wip
    """
    if connexion.request.is_json:
        body = Wip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
