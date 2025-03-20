import numpy as np

from particle import Particle


class EMField:
    """Ensure interlieved field pair"""

    def __init__(
        self,
        particles: list[Particle],
        spatial_limits: list[list[float]] = None,
        dx: float = 0.1,
        dt: float = 0.1,
    ):

        if spatial_limits is None:
            spatial_limits = [[[0, 1], [0, 1], [0, 1]]]
        self.spatial_limits = np.array(spatial_limits)

        self.x_coords = np.arange(*spatial_limits[0], dx)
        self.y_coords = np.arange(*spatial_limits[1], dx)
        self.z_coords = np.arange(*spatial_limits[2], dx)


class EField:
    def __init__(self, particles: list[Particle]):

        pass

    def get_vec(self, pos):
        pass


class BField:
    pass
