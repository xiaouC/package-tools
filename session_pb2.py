# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='session.proto',
  package='poem',
  serialized_pb='\n\rsession.proto\x12\x04poem\"F\n\x08\x46ileInfo\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x0b\n\x03md5\x18\x02 \x02(\t\x12\x0c\n\x04size\x18\x03 \x02(\x05\x12\x12\n\x03new\x18\x04 \x02(\x08:\x05\x66\x61lse\"\x8b\x01\n\x14\x43heckUpgradeResponse\x12\x14\n\x0cisbigupgrade\x18\x01 \x02(\x08\x12\x11\n\tversionId\x18\x02 \x01(\x05\x12\x13\n\x0bversionName\x18\x03 \x01(\t\x12\x1d\n\x05\x66iles\x18\x04 \x03(\x0b\x32\x0e.poem.FileInfo\x12\x16\n\x0e\x63onfig_version\x18\x05 \x01(\x05\x42\x02H\x03')




_FILEINFO = descriptor.Descriptor(
  name='FileInfo',
  full_name='poem.FileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='url', full_name='poem.FileInfo.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='md5', full_name='poem.FileInfo.md5', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='poem.FileInfo.size', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new', full_name='poem.FileInfo.new', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=93,
)


_CHECKUPGRADERESPONSE = descriptor.Descriptor(
  name='CheckUpgradeResponse',
  full_name='poem.CheckUpgradeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='isbigupgrade', full_name='poem.CheckUpgradeResponse.isbigupgrade', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='versionId', full_name='poem.CheckUpgradeResponse.versionId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='versionName', full_name='poem.CheckUpgradeResponse.versionName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='files', full_name='poem.CheckUpgradeResponse.files', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='config_version', full_name='poem.CheckUpgradeResponse.config_version', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=96,
  serialized_end=235,
)

_CHECKUPGRADERESPONSE.fields_by_name['files'].message_type = _FILEINFO
DESCRIPTOR.message_types_by_name['FileInfo'] = _FILEINFO
DESCRIPTOR.message_types_by_name['CheckUpgradeResponse'] = _CHECKUPGRADERESPONSE

class FileInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEINFO
  
  # @@protoc_insertion_point(class_scope:poem.FileInfo)

class CheckUpgradeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKUPGRADERESPONSE
  
  # @@protoc_insertion_point(class_scope:poem.CheckUpgradeResponse)

# @@protoc_insertion_point(module_scope)