"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from ...... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MoveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DESTINATION_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    WORLD_STATE_FIELD_NUMBER: builtins.int

    @property
    def destination(self) -> proto.api.common.v1.common_pb2.PoseInFrame:
        ...

    @property
    def component_name(self) -> proto.api.common.v1.common_pb2.ResourceName:
        ...

    @property
    def world_state(self) -> proto.api.common.v1.common_pb2.WorldState:
        ...

    def __init__(self, *, destination: typing.Optional[proto.api.common.v1.common_pb2.PoseInFrame]=..., component_name: typing.Optional[proto.api.common.v1.common_pb2.ResourceName]=..., world_state: typing.Optional[proto.api.common.v1.common_pb2.WorldState]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'world_state', b'world_state']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'world_state', b'world_state']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_world_state', b'_world_state']) -> typing.Optional[typing_extensions.Literal['world_state']]:
        ...
global___MoveRequest = MoveRequest

class MoveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool = ...

    def __init__(self, *, success: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['success', b'success']) -> None:
        ...
global___MoveResponse = MoveResponse

class GetPoseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FRAME_FIELD_NUMBER: builtins.int

    @property
    def component_name(self) -> proto.api.common.v1.common_pb2.ResourceName:
        ...
    destination_frame: typing.Text = ...
    'world if unset'

    def __init__(self, *, component_name: typing.Optional[proto.api.common.v1.common_pb2.ResourceName]=..., destination_frame: typing.Text=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['component_name', b'component_name']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_name', b'component_name', 'destination_frame', b'destination_frame']) -> None:
        ...
global___GetPoseRequest = GetPoseRequest

class GetPoseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> proto.api.common.v1.common_pb2.PoseInFrame:
        ...

    def __init__(self, *, pose: typing.Optional[proto.api.common.v1.common_pb2.PoseInFrame]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___GetPoseResponse = GetPoseResponse