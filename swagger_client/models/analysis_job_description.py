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

class AnalysisJobDescription(object):
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
        'algorithm': 'str',
        'parameters': 'object',
        'input': 'list[AnalysisJobDescriptionDatasource]',
        'output': 'list[AnalysisJobDescriptionDatasource]'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'parameters': 'parameters',
        'input': 'input',
        'output': 'output'
    }

    def __init__(self, algorithm=None, parameters=None, input=None, output=None):  # noqa: E501
        """AnalysisJobDescription - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._parameters = None
        self._input = None
        self._output = None
        self.discriminator = None
        self.algorithm = algorithm
        if parameters is not None:
            self.parameters = parameters
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output

    @property
    def algorithm(self):
        """Gets the algorithm of this AnalysisJobDescription.  # noqa: E501


        :return: The algorithm of this AnalysisJobDescription.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this AnalysisJobDescription.


        :param algorithm: The algorithm of this AnalysisJobDescription.  # noqa: E501
        :type: str
        """
        if algorithm is None:
            raise ValueError("Invalid value for `algorithm`, must not be `None`")  # noqa: E501

        self._algorithm = algorithm

    @property
    def parameters(self):
        """Gets the parameters of this AnalysisJobDescription.  # noqa: E501


        :return: The parameters of this AnalysisJobDescription.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this AnalysisJobDescription.


        :param parameters: The parameters of this AnalysisJobDescription.  # noqa: E501
        :type: object
        """

        self._parameters = parameters

    @property
    def input(self):
        """Gets the input of this AnalysisJobDescription.  # noqa: E501


        :return: The input of this AnalysisJobDescription.  # noqa: E501
        :rtype: list[AnalysisJobDescriptionDatasource]
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this AnalysisJobDescription.


        :param input: The input of this AnalysisJobDescription.  # noqa: E501
        :type: list[AnalysisJobDescriptionDatasource]
        """

        self._input = input

    @property
    def output(self):
        """Gets the output of this AnalysisJobDescription.  # noqa: E501


        :return: The output of this AnalysisJobDescription.  # noqa: E501
        :rtype: list[AnalysisJobDescriptionDatasource]
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this AnalysisJobDescription.


        :param output: The output of this AnalysisJobDescription.  # noqa: E501
        :type: list[AnalysisJobDescriptionDatasource]
        """

        self._output = output

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
        if issubclass(AnalysisJobDescription, dict):
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
        if not isinstance(other, AnalysisJobDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
