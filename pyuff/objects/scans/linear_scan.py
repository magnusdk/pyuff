import numpy as np

from pyuff.objects.scans.scan import Scan
from pyuff.objects.uff import compulsory_property, dependent_property
from pyuff.readers import LazyArray


class LinearScan(Scan):
    # Compulsory properties
    @compulsory_property
    def x_axis(self) -> np.ndarray:
        "Vector containing the x coordinates of the x-axis [m]"
        return LazyArray(self._reader["x_axis"])

    @compulsory_property
    def z_axis(self) -> np.ndarray:
        "Vector containing the z coordinates of the z-axis [m]"
        return LazyArray(self._reader["z_axis"])

    # Dependent properties
    @dependent_property
    def N_x_axis(self) -> int:
        "Number of pixels in the x_axis"
        return len(self.x_axis)

    @dependent_property
    def N_z_axis(self) -> int:
        "Number of pixels in the z_axis"
        return len(self.z_axis)

    @dependent_property
    def x_step(self) -> float:
        "The step size in m of the x samples"
        return np.mean(np.diff(self.x_axis))

    @dependent_property
    def z_step(self) -> float:
        "The step size in m of the z samples"
        return np.mean(np.diff(self.z_axis))

    @dependent_property
    def reference_distance(self) -> np.ndarray:
        "Distance used for the calculation of the phase term"
        return self.z

    # Unlike the base scan object (pyuff.Scan), x, y, and z are not compulsory
    # properties, but calculated based on azimuth_axis, depth_axis, and origin.
    @dependent_property
    def x(self) -> np.ndarray:
        X, Z = np.meshgrid(self.x_axis, self.z_axis, indexing="ij")
        N_pixels = X.size
        return np.reshape(X, [N_pixels])

    @dependent_property
    def y(self) -> np.ndarray:
        N_pixels = self.N_x_axis * self.N_z_axis
        return np.zeros((N_pixels,))

    @dependent_property
    def z(self) -> np.ndarray:
        X, Z = np.meshgrid(self.x_axis, self.z_axis, indexing="ij")
        N_pixels = Z.size
        return np.reshape(Z, [N_pixels])
