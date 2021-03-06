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

class Token(object):
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
        'token_type': 'str',
        'token_string': 'str'
    }

    attribute_map = {
        'token_type': 'token_type',
        'token_string': 'token_string'
    }

    def __init__(self, token_type=None, token_string=None):  # noqa: E501
        """Token - a model defined in Swagger"""  # noqa: E501
        self._token_type = None
        self._token_string = None
        self.discriminator = None
        if token_type is not None:
            self.token_type = token_type
        if token_string is not None:
            self.token_string = token_string

    @property
    def token_type(self):
        """Gets the token_type of this Token.  # noqa: E501


        :return: The token_type of this Token.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this Token.


        :param token_type: The token_type of this Token.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def token_string(self):
        """Gets the token_string of this Token.  # noqa: E501


        :return: The token_string of this Token.  # noqa: E501
        :rtype: str
        """
        return self._token_string

    @token_string.setter
    def token_string(self, token_string):
        """Sets the token_string of this Token.


        :param token_string: The token_string of this Token.  # noqa: E501
        :type: str
        """

        self._token_string = token_string

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
        if issubclass(Token, dict):
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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
