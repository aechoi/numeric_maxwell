"""Module for modeling charged particles"""

from dataclasses import dataclass
from typing import TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from field import EField, BField


@dataclass
class Particle:
    charge: float
    mass: float
    _pos: np.array_like = None
    _vel: np.array_like = None

    def __post_init__(self):
        if self._pos is None:
            self._pos = np.zeros(3)
        self._pos = np.array(self._pos)

        if self._vel is None:
            self._vel = np.zeros(3)
        self._vel = np.array(self._vel)

    def _apply_force(
        self, efield: "EField", bfield: "BField", ext_force: np.ndarray = np.zeros(3)
    ) -> np.ndarray:
        """Apply forces from the fields and external sources. Return acceleration."""
        e_force = self.charge * efield.get_vec(self._pos)
        b_force = self.charge * np.cross(self._vel, bfield.get_vec(self._pos))

        return (e_force + b_force + ext_force) / self.mass

    def iterate(
        self,
        dt,
        efield: "EField",
        bfield: "BField",
        ext_force: np.ndarray = np.zeros(3),
    ):
        """Simulate the movement of the particle through a space"""
        acc = self._apply_force(efield, bfield, ext_force)
        self._pos = self._pos + self._vel * dt
        self._vel = self._vel + acc * dt

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self._vel = 0
