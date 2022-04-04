"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    'Name of a camera'
    mime_type: typing.Text = ...
    'Requested MIME type of response'

    def __init__(self, *, name: typing.Text=..., mime_type: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___GetFrameRequest = GetFrameRequest

class GetFrameResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIME_TYPE_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    WIDTH_PX_FIELD_NUMBER: builtins.int
    HEIGHT_PX_FIELD_NUMBER: builtins.int
    mime_type: typing.Text = ...
    'Actual MIME type of response'
    image: builtins.bytes = ...
    'Frame in bytes'
    width_px: builtins.int = ...
    'Width of frame in px'
    height_px: builtins.int = ...
    'Height of frame in px'

    def __init__(self, *, mime_type: typing.Text=..., image: builtins.bytes=..., width_px: builtins.int=..., height_px: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['height_px', b'height_px', 'image', b'image', 'mime_type', b'mime_type', 'width_px', b'width_px']) -> None:
        ...
global___GetFrameResponse = GetFrameResponse

class RenderFrameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    'Name of a camera'
    mime_type: typing.Text = ...
    'Requested MIME type of response'

    def __init__(self, *, name: typing.Text=..., mime_type: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___RenderFrameRequest = RenderFrameRequest

class GetPointCloudRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    'Name of a camera'
    mime_type: typing.Text = ...
    'Requested MIME type of response'

    def __init__(self, *, name: typing.Text=..., mime_type: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___GetPointCloudRequest = GetPointCloudRequest

class GetPointCloudResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIME_TYPE_FIELD_NUMBER: builtins.int
    POINT_CLOUD_FIELD_NUMBER: builtins.int
    mime_type: typing.Text = ...
    'Actual MIME type of response'
    point_cloud: builtins.bytes = ...
    'Frame in bytes'

    def __init__(self, *, mime_type: typing.Text=..., point_cloud: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mime_type', b'mime_type', 'point_cloud', b'point_cloud']) -> None:
        ...
global___GetPointCloudResponse = GetPointCloudResponse