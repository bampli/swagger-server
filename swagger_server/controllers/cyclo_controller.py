import connexion
import six

from swagger_server.models.cyclo import Cyclo  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.stage import Stage  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server import util


def add_cyclo(body):  # noqa: E501
    """Create a new Cyclo

    Adds a Cyclo # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Cyclo
    """
    if connexion.request.is_json:
        body = Cyclo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_stage(body):  # noqa: E501
    """Create a new Stage

    Adds a Stage # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Stage
    """
    if connexion.request.is_json:
        body = Stage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_task(body):  # noqa: E501
    """Create a new Task

    Adds a Task # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Task
    """
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_cyclo(cycloid):  # noqa: E501
    """Delete a Cyclo

    Deletes a Cyclo # noqa: E501

    :param cycloid: Identifier of the Cyclo
    :type cycloid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_stage(stageid):  # noqa: E501
    """Delete a Stage

    Deletes a Stage # noqa: E501

    :param stageid: Identifier of the Stage
    :type stageid: str

    :rtype: None
    """
    return 'do some magic!'


def delete_task(taskid):  # noqa: E501
    """Delete a Task

    Deletes a Task # noqa: E501

    :param taskid: Identifier of the Task
    :type taskid: str

    :rtype: None
    """
    return 'do some magic!'


def get_cyclo(cycloid):  # noqa: E501
    """Load an individual Cyclo

    Loads a Cyclo # noqa: E501

    :param cycloid: Identifier of the Cyclo
    :type cycloid: str

    :rtype: Cyclo
    """
    return 'do some magic!'


def get_stage(stageid):  # noqa: E501
    """Load an individual Stage

    Loads a Stage # noqa: E501

    :param stageid: Identifier of the Stage
    :type stageid: str

    :rtype: Stage
    """
    return 'do some magic!'


def get_task(taskid):  # noqa: E501
    """Load an individual Task

    Loads a Task # noqa: E501

    :param taskid: Identifier of the Task
    :type taskid: str

    :rtype: Task
    """
    return 'do some magic!'


def search_cyclos(size=None, page=None, sort=None, name=None, company_id=None):  # noqa: E501
    """Load the list of Cyclos

    Loads list of Cyclos # noqa: E501

    :param size: Size of the page to retrieve.
    :type size: int
    :param page: Number of the page to retrieve.
    :type page: float
    :param sort: Order in which to retrieve the results.
    :type sort: str
    :param name: Allows to filter the collections of result by name
    :type name: str
    :param company_id: Allows to filter the collections of result by company_id
    :type company_id: str

    :rtype: List[Cyclo]
    """
    return 'do some magic!'


def search_stages(size=None, page=None, sort=None, name=None, cyclo_id=None):  # noqa: E501
    """Load the list of Stages

    Loads list of Stages # noqa: E501

    :param size: Size of the page to retrieve.
    :type size: int
    :param page: Number of the page to retrieve.
    :type page: float
    :param sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC
    :type sort: str
    :param name: Allows to filter the collections of result by name
    :type name: str
    :param cyclo_id: Allows to filter the collections of result by cyclo_id
    :type cyclo_id: str

    :rtype: List[Stage]
    """
    return 'do some magic!'


def search_tasks(size=None, page=None, sort=None, name=None, stage_id=None):  # noqa: E501
    """Load the list of Tasks

    Loads list of Tasks # noqa: E501

    :param size: Size of the page to retrieve.
    :type size: int
    :param page: Number of the page to retrieve.
    :type page: float
    :param sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort&#x3D;name ASC,city DESC
    :type sort: str
    :param name: Allows to filter the collections of result by name
    :type name: str
    :param stage_id: Allows to filter the collections of result by stage_id
    :type stage_id: str

    :rtype: List[Task]
    """
    return 'do some magic!'


def update_cyclo(body, cycloid):  # noqa: E501
    """Update a Cyclo

    Stores a Cyclo # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param cycloid: Identifier of the Cyclo
    :type cycloid: str

    :rtype: Cyclo
    """
    if connexion.request.is_json:
        body = Cyclo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_stage(body, stageid):  # noqa: E501
    """Update a Stage

    Stores a Stage # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param stageid: Identifier of the Stage
    :type stageid: str

    :rtype: Stage
    """
    if connexion.request.is_json:
        body = Stage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_task(body, taskid):  # noqa: E501
    """Update a Task

    Stores a Task # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param taskid: Identifier of the Task
    :type taskid: str

    :rtype: Task
    """
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
