from pyuff.objects.uff import compulsory_property, dependent_property
from pyuff.objects.scan import Scan
from pyuff.readers import LazyArray, util


class SectorScan(Scan):
    # Compulsory properties
    @compulsory_property
    def azimuth_axis(self):
        "Vector containing the azimuth coordinates [rad]"
        return LazyArray(self._reader["azimuth_axis"])

    @compulsory_property
    def depth_axis(self):
        "Vector containing the distance coordinates [m]"
        return LazyArray(self._reader["depth_axis"])

    @compulsory_property
    def origin(self):
        "Vector of UFF.POINT objects"
        from pyuff.objects.point import Point

        if "origin" in self._reader:
            return util.read_potentially_list(self._reader["origin"], Point)
        if "apex" in self._reader:
            return Point(self._reader["apex"])

    # Dependent properties
    @dependent_property
    def n_azimuth_axis(self):
        "Number of pixels in azimuth_axis"
        # TODO

    @dependent_property
    def n_depth_axis(self):
        "Number of pixels in depth_axis"
        # TODO

    @dependent_property
    def n_origins(self):
        "Number of scanline origins"
        # TODO

    @dependent_property
    def depth_step(self):
        "Step size along the depth axis [m]"
        # TODO

    @dependent_property
    def reference_distance(self):
        "Distance used for the calculation of the phase term [m]"
        # TODO
