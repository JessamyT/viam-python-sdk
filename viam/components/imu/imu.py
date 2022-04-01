import abc
from dataclasses import dataclass

from viam.proto.api.component.imu import (Acceleration, AngularVelocity,
                                          EulerAngles, Magnetometer)

from ..component_base import ComponentBase


@dataclass
class Orientation():
    """
    An object used to express the different parameterizations
    of the orientation of a rigid object or a frame of
    reference in 3D Euclidean space.
    """
    euler_angles: EulerAngles


class IMU(ComponentBase):
    """
    Abstract representation of a physical IMU

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def read_angular_velocity(self) -> AngularVelocity:
        """
        Return the angular velocity of the IMU

        Returns:
            AngularVelocity
        """
        ...

    @abc.abstractmethod
    async def read_orientation(self) -> Orientation:
        """
        Return the orientation of the IMU

        Returns:
            Orientation
        """
        ...

    @abc.abstractmethod
    async def read_acceleration(self) -> Acceleration:
        """
        Return the acceleration of the IMU

        Returns:
            Acceleration
        """
        ...

    @abc.abstractmethod
    async def read_magnetometer(self) -> Magnetometer:
        """
        Return the most recent reading from the magnetometer of the IMU

        Returns:
            Magnetometer
        """
        ...
