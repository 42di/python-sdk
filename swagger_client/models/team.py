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

class Team(object):
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
        'name': 'str',
        'is_user_primary': 'bool',
        'creator': 'str',
        'created': 'datetime',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_user_primary': 'is_user_primary',
        'creator': 'creator',
        'created': 'created',
        'last_modified': 'last_modified'
    }

    def __init__(self, id=None, name=None, is_user_primary=None, creator=None, created=None, last_modified=None):  # noqa: E501
        """Team - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_user_primary = None
        self._creator = None
        self._created = None
        self._last_modified = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if is_user_primary is not None:
            self.is_user_primary = is_user_primary
        if creator is not None:
            self.creator = creator
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501


        :return: The id of this Team.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.


        :param id: The id of this Team.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501


        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.


        :param name: The name of this Team.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_user_primary(self):
        """Gets the is_user_primary of this Team.  # noqa: E501


        :return: The is_user_primary of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_primary

    @is_user_primary.setter
    def is_user_primary(self, is_user_primary):
        """Sets the is_user_primary of this Team.


        :param is_user_primary: The is_user_primary of this Team.  # noqa: E501
        :type: bool
        """

        self._is_user_primary = is_user_primary

    @property
    def creator(self):
        """Gets the creator of this Team.  # noqa: E501


        :return: The creator of this Team.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Team.


        :param creator: The creator of this Team.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """Gets the created of this Team.  # noqa: E501


        :return: The created of this Team.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Team.


        :param created: The created of this Team.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this Team.  # noqa: E501


        :return: The last_modified of this Team.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Team.


        :param last_modified: The last_modified of this Team.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

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
        if issubclass(Team, dict):
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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
