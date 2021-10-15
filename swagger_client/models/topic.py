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

class Topic(object):
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
        'board_id': 'str',
        'is_reply': 'bool',
        'replay_to': 'str',
        'creator': 'str',
        'subject': 'str',
        'body': 'str',
        'created': 'datetime',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'board_id': 'board_id',
        'is_reply': 'is_reply',
        'replay_to': 'replay_to',
        'creator': 'creator',
        'subject': 'subject',
        'body': 'body',
        'created': 'created',
        'last_modified': 'last_modified'
    }

    def __init__(self, id=None, board_id=None, is_reply=None, replay_to=None, creator=None, subject=None, body=None, created=None, last_modified=None):  # noqa: E501
        """Topic - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._board_id = None
        self._is_reply = None
        self._replay_to = None
        self._creator = None
        self._subject = None
        self._body = None
        self._created = None
        self._last_modified = None
        self.discriminator = None
        self.id = id
        self.board_id = board_id
        if is_reply is not None:
            self.is_reply = is_reply
        if replay_to is not None:
            self.replay_to = replay_to
        if creator is not None:
            self.creator = creator
        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this Topic.  # noqa: E501


        :return: The id of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Topic.


        :param id: The id of this Topic.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def board_id(self):
        """Gets the board_id of this Topic.  # noqa: E501


        :return: The board_id of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._board_id

    @board_id.setter
    def board_id(self, board_id):
        """Sets the board_id of this Topic.


        :param board_id: The board_id of this Topic.  # noqa: E501
        :type: str
        """
        if board_id is None:
            raise ValueError("Invalid value for `board_id`, must not be `None`")  # noqa: E501

        self._board_id = board_id

    @property
    def is_reply(self):
        """Gets the is_reply of this Topic.  # noqa: E501


        :return: The is_reply of this Topic.  # noqa: E501
        :rtype: bool
        """
        return self._is_reply

    @is_reply.setter
    def is_reply(self, is_reply):
        """Sets the is_reply of this Topic.


        :param is_reply: The is_reply of this Topic.  # noqa: E501
        :type: bool
        """

        self._is_reply = is_reply

    @property
    def replay_to(self):
        """Gets the replay_to of this Topic.  # noqa: E501


        :return: The replay_to of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._replay_to

    @replay_to.setter
    def replay_to(self, replay_to):
        """Sets the replay_to of this Topic.


        :param replay_to: The replay_to of this Topic.  # noqa: E501
        :type: str
        """

        self._replay_to = replay_to

    @property
    def creator(self):
        """Gets the creator of this Topic.  # noqa: E501


        :return: The creator of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Topic.


        :param creator: The creator of this Topic.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def subject(self):
        """Gets the subject of this Topic.  # noqa: E501


        :return: The subject of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Topic.


        :param subject: The subject of this Topic.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this Topic.  # noqa: E501


        :return: The body of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Topic.


        :param body: The body of this Topic.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def created(self):
        """Gets the created of this Topic.  # noqa: E501


        :return: The created of this Topic.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Topic.


        :param created: The created of this Topic.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this Topic.  # noqa: E501


        :return: The last_modified of this Topic.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Topic.


        :param last_modified: The last_modified of this Topic.  # noqa: E501
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
        if issubclass(Topic, dict):
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
        if not isinstance(other, Topic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other