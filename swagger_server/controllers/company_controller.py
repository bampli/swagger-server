import connexion
import six

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def add_company(body):  # noqa: E501
    """Create a new Company

    Adds a Company # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Company
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_product(body):  # noqa: E501
    """Create a new Product

    Adds a Product # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_company(companyid):  # noqa: E501
    """Delete a Company

    Deletes a Company # noqa: E501

    :param companyid: Identifier of the Company
    :type companyid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_product(productid):  # noqa: E501
    """Delete a Product

    Deletes a Product # noqa: E501

    :param productid: Identifier of the Product
    :type productid: str

    :rtype: None
    """
    return 'do some magic!'


def get_company(companyid):  # noqa: E501
    """Load an individual Company

    Loads a Company # noqa: E501

    :param companyid: Identifier of the Company
    :type companyid: str

    :rtype: Company
    """
    return 'do some magic!'


def get_product(productid):  # noqa: E501
    """Load an individual Product

    Loads a Product # noqa: E501

    :param productid: Identifier of the Product
    :type productid: str

    :rtype: Product
    """
    return 'do some magic!'


def search_companies(size=None, page=None, sort=None, name=None):  # noqa: E501
    """Load the list of Companies

    Loads list of Companies # noqa: E501

    :param size: Size of the page to retrieve.
    :type size: int
    :param page: Number of the page to retrieve.
    :type page: float
    :param sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC
    :type sort: str
    :param name: Allows to filter the collections of result by the value of name
    :type name: str

    :rtype: List[Company]
    """
    return 'do some magic!'


def search_products(size=None, page=None, sort=None, name=None, company_id=None):  # noqa: E501
    """Load the list of Products

    Loads list of Products # noqa: E501

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

    :rtype: List[Product]
    """
    return 'do some magic!'


def update_company(body, companyid):  # noqa: E501
    """Update a Company

    Stores a Company # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param companyid: Identifier of the Company
    :type companyid: str

    :rtype: Company
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_product(body, productid):  # noqa: E501
    """Update a Product

    Stores a Product # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param productid: Identifier of the Product
    :type productid: str

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
