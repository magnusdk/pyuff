from pyuff.objects import Uff
from pyuff.objects.uff import Uff, compulsory_property
from pyuff.readers import LazyArray, LazyScalar


class Pulse(Uff):
    # Compulsory properties
    @compulsory_property
    def center_frequency(self):
        "Center frequency [Hz]"
        return LazyScalar(self._reader["center_frequency"])

    @compulsory_property
    def fractional_bandwidth(self):
        "Probe fractional bandwidth [unitless]"
        return LazyScalar(self._reader["fractional_bandwidth"])

    @compulsory_property
    def phase(self):
        "Initial phase [rad]"
        return LazyScalar(self._reader["phase"])

    @compulsory_property
    def waveform(self):
        "Transmitted waveform (for example used for match filtering)"
        return LazyArray(self._reader["waveform"])
