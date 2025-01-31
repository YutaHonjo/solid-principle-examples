# pylint: disable=missing-docstring, useless-super-delegation
from abc import ABC, abstractmethod

class Washer(ABC):
    @abstractmethod
    def wash(self, clothes):
        pass

class Dryer(ABC):
    @abstractmethod
    def dry(self, clothes):
        pass


class BasicWasher(Washer):
    def wash(self, clothes):
        print(f"Washing clothes: {clothes}")

class WasherDryer(Washer, Dryer):
    def wash(self, clothes):
        print(f"Washing clothes: {clothes}")

    def dry(self, clothes):
        print(f"Drying clothes: {clothes}")