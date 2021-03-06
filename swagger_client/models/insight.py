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

class Insight(object):
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
        'team_id': 'str',
        'project_id': 'str',
        'subject': 'str',
        'summary': 'str',
        'content': 'str',
        'creator': 'str',
        'created': 'datetime',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'team_id': 'team_id',
        'project_id': 'project_id',
        'subject': 'subject',
        'summary': 'summary',
        'content': 'content',
        'creator': 'creator',
        'created': 'created',
        'last_modified': 'last_modified'
    }

    def __init__(self, id=None, team_id=None, project_id=None, subject=None, summary=None, content=None, creator=None, created=None, last_modified=None):  # noqa: E501
        """Insight - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._team_id = None
        self._project_id = None
        self._subject = None
        self._summary = None
        self._content = None
        self._creator = None
        self._created = None
        self._last_modified = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if team_id is not None:
            self.team_id = team_id
        if project_id is not None:
            self.project_id = project_id
        if subject is not None:
            self.subject = subject
        if summary is not None:
            self.summary = summary
        if content is not None:
            self.content = content
        if creator is not None:
            self.creator = creator
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this Insight.  # noqa: E501


        :return: The id of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Insight.


        :param id: The id of this Insight.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """Gets the team_id of this Insight.  # noqa: E501


        :return: The team_id of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Insight.


        :param team_id: The team_id of this Insight.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def project_id(self):
        """Gets the project_id of this Insight.  # noqa: E501


        :return: The project_id of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Insight.


        :param project_id: The project_id of this Insight.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def subject(self):
        """Gets the subject of this Insight.  # noqa: E501


        :return: The subject of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Insight.


        :param subject: The subject of this Insight.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def summary(self):
        """Gets the summary of this Insight.  # noqa: E501


        :return: The summary of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Insight.


        :param summary: The summary of this Insight.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def content(self):
        """Gets the content of this Insight.  # noqa: E501


        :return: The content of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Insight.


        :param content: The content of this Insight.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def creator(self):
        """Gets the creator of this Insight.  # noqa: E501


        :return: The creator of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Insight.


        :param creator: The creator of this Insight.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """Gets the created of this Insight.  # noqa: E501


        :return: The created of this Insight.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Insight.


        :param created: The created of this Insight.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this Insight.  # noqa: E501


        :return: The last_modified of this Insight.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Insight.


        :param last_modified: The last_modified of this Insight.  # noqa: E501
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
        if issubclass(Insight, dict):
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
        if not isinstance(other, Insight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
