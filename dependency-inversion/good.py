# pylint: disable=missing-docstring, useless-super-delegation
from abc import ABC, abstractmethod

class HamburgerWithCheese(ABC):
    @abstractmethod
    def make_hamburger(self) -> str:
        pass

class Cheeseburger(HamburgerWithCheese):
    def make_hamburger(self) -> str:
        return "Cheeseburger"

class DoubleCheeseburger(HamburgerWithCheese):
    def make_hamburger(self) -> str:
        return "Double Cheeseburger"

class FastFoodService:
    # MEMO: 低水準モジュールのロジックを知らなくてもいい
    def __init__(self, hamburger: HamburgerWithCheese):
        self.hamburger = hamburger

    def order_hamburger(self, money: float) -> str:
        if money >= 5.0:
            return self.hamburger.make_hamburger()
        else:
            return "Not enough money for a hamburger."

if __name__ == "__main__":
    cheeseburger = Cheeseburger()
    fast_food_service = FastFoodService(cheeseburger)

    result = fast_food_service.order_hamburger(5.0)

    double_cheeseburger = DoubleCheeseburger()
    fast_food_service = FastFoodService(double_cheeseburger)

    result = fast_food_service.order_hamburger(5.0)
