"""
    Pod API

    This document refers to Symphony API calls that do not need encryption or decryption of content.  - sessionToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have made no change to the system even if ome subset of the request would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X.   # noqa: E501

    The version of the OpenAPI document: 20.14.0-SNAPSHOT
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
from typing import List, Union

from symphony.bdk.gen.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from symphony.bdk.gen.exceptions import ApiAttributeError


from symphony.bdk.gen.pod_model.message_download_receipt_count import MessageDownloadReceiptCount
from symphony.bdk.gen.pod_model.message_receipt_detail import MessageReceiptDetail
from symphony.bdk.gen.pod_model.message_stream import MessageStream
from symphony.bdk.gen.pod_model.message_user import MessageUser
from symphony.bdk.gen.pod_model.pagination import Pagination
globals()['MessageDownloadReceiptCount'] = MessageDownloadReceiptCount
globals()['MessageReceiptDetail'] = MessageReceiptDetail
globals()['MessageStream'] = MessageStream
globals()['MessageUser'] = MessageUser
globals()['Pagination'] = Pagination

class MessageReceiptDetailResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a pod_model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a pod_model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'creator': (MessageUser, none_type),  # noqa: E501
            'on_behalf_of_user': (MessageUser, none_type),  # noqa: E501
            'stream': (MessageStream, none_type),  # noqa: E501
            'creation_date': (int, none_type),  # noqa: E501
            'delivery_receipt_count': (int, none_type),  # noqa: E501
            'read_receipt_count': (int, none_type),  # noqa: E501
            'email_notification_count': (int, none_type),  # noqa: E501
            'download_receipt_counts': ([MessageDownloadReceiptCount], none_type),  # noqa: E501
            'message_receipt_detail': ([MessageReceiptDetail], none_type),  # noqa: E501
            'pagination': (Pagination, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'creator': 'creator',  # noqa: E501
        'on_behalf_of_user': 'onBehalfOfUser',  # noqa: E501
        'stream': 'stream',  # noqa: E501
        'creation_date': 'creationDate',  # noqa: E501
        'delivery_receipt_count': 'deliveryReceiptCount',  # noqa: E501
        'read_receipt_count': 'readReceiptCount',  # noqa: E501
        'email_notification_count': 'emailNotificationCount',  # noqa: E501
        'download_receipt_counts': 'downloadReceiptCounts',  # noqa: E501
        'message_receipt_detail': 'MessageReceiptDetail',  # noqa: E501
        'pagination': 'pagination',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MessageReceiptDetailResponse - a pod_model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the pod_model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            creator (MessageUser): [optional]  # noqa: E501
            on_behalf_of_user (MessageUser): [optional]  # noqa: E501
            stream (MessageStream): [optional]  # noqa: E501
            creation_date (int): [optional]  # noqa: E501
            delivery_receipt_count (int): [optional]  # noqa: E501
            read_receipt_count (int): [optional]  # noqa: E501
            email_notification_count (int): [optional]  # noqa: E501
            download_receipt_counts ([MessageDownloadReceiptCount]): [optional]  # noqa: E501
            message_receipt_detail ([MessageReceiptDetail]): [optional]  # noqa: E501
            pagination (Pagination): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MessageReceiptDetailResponse - a pod_model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the pod_model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            creator (MessageUser): [optional]  # noqa: E501
            on_behalf_of_user (MessageUser): [optional]  # noqa: E501
            stream (MessageStream): [optional]  # noqa: E501
            creation_date (int): [optional]  # noqa: E501
            delivery_receipt_count (int): [optional]  # noqa: E501
            read_receipt_count (int): [optional]  # noqa: E501
            email_notification_count (int): [optional]  # noqa: E501
            download_receipt_counts ([MessageDownloadReceiptCount]): [optional]  # noqa: E501
            message_receipt_detail ([MessageReceiptDetail]): [optional]  # noqa: E501
            pagination (Pagination): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.creator: MessageUser = None
        self.on_behalf_of_user: MessageUser = None
        self.stream: MessageStream = None
        self.creation_date: int = None
        self.delivery_receipt_count: int = None
        self.read_receipt_count: int = None
        self.email_notification_count: int = None
        self.download_receipt_counts: List[MessageDownloadReceiptCount] = None
        self.message_receipt_detail: List[MessageReceiptDetail] = None
        self.pagination: Pagination = None
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
