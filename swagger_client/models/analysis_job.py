# coding: utf-8

"""
    42di API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@42docs.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnalysisJob(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'creator': 'str',
        'status': 'str',
        'message': 'str',
        'created': 'datetime',
        'last_live_time': 'datetime',
        'adopter': 'str',
        'description': 'AnalysisJobDescription'
    }

    attribute_map = {
        'id': 'id',
        'creator': 'creator',
        'status': 'status',
        'message': 'message',
        'created': 'created',
        'last_live_time': 'last_live_time',
        'adopter': 'adopter',
        'description': 'description'
    }

    def __init__(self, id=None, creator=None, status=None, message=None, created=None, last_live_time=None, adopter=None, description=None):  # noqa: E501
        """AnalysisJob - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._creator = None
        self._status = None
        self._message = None
        self._created = None
        self._last_live_time = None
        self._adopter = None
        self._description = None
        self.discriminator = None
        self.id = id
        if creator is not None:
            self.creator = creator
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if created is not None:
            self.created = created
        if last_live_time is not None:
            self.last_live_time = last_live_time
        if adopter is not None:
            self.adopter = adopter
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this AnalysisJob.  # noqa: E501


        :return: The id of this AnalysisJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalysisJob.


        :param id: The id of this AnalysisJob.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def creator(self):
        """Gets the creator of this AnalysisJob.  # noqa: E501


        :return: The creator of this AnalysisJob.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AnalysisJob.


        :param creator: The creator of this AnalysisJob.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def status(self):
        """Gets the status of this AnalysisJob.  # noqa: E501


        :return: The status of this AnalysisJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AnalysisJob.


        :param status: The status of this AnalysisJob.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this AnalysisJob.  # noqa: E501


        :return: The message of this AnalysisJob.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AnalysisJob.


        :param message: The message of this AnalysisJob.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def created(self):
        """Gets the created of this AnalysisJob.  # noqa: E501


        :return: The created of this AnalysisJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AnalysisJob.


        :param created: The created of this AnalysisJob.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_live_time(self):
        """Gets the last_live_time of this AnalysisJob.  # noqa: E501


        :return: The last_live_time of this AnalysisJob.  # noqa: E501
        :rtype: datetime
        """
        return self._last_live_time

    @last_live_time.setter
    def last_live_time(self, last_live_time):
        """Sets the last_live_time of this AnalysisJob.


        :param last_live_time: The last_live_time of this AnalysisJob.  # noqa: E501
        :type: datetime
        """

        self._last_live_time = last_live_time

    @property
    def adopter(self):
        """Gets the adopter of this AnalysisJob.  # noqa: E501


        :return: The adopter of this AnalysisJob.  # noqa: E501
        :rtype: str
        """
        return self._adopter

    @adopter.setter
    def adopter(self, adopter):
        """Sets the adopter of this AnalysisJob.


        :param adopter: The adopter of this AnalysisJob.  # noqa: E501
        :type: str
        """

        self._adopter = adopter

    @property
    def description(self):
        """Gets the description of this AnalysisJob.  # noqa: E501


        :return: The description of this AnalysisJob.  # noqa: E501
        :rtype: AnalysisJobDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnalysisJob.


        :param description: The description of this AnalysisJob.  # noqa: E501
        :type: AnalysisJobDescription
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AnalysisJob, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalysisJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
