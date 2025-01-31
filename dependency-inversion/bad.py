# pylint: disable=missing-docstring, useless-super-delegation
class Cheeseburger:
    def make_hamburger(self) -> str:
        return "Cheeseburger"

class FastFoodService:
    def order_hamburger(self, money: float) -> str:
        if money >= 5.0:
            # MEMO: 依存しているクラスを直接インスタンス化している
            return Cheeseburger().make_hamburger()
        else:
            return "Not enough money for a hamburger."


if __name__ == "__main__":
    fast_food_service_bad = FastFoodService()
    result = fast_food_service_bad.order_hamburger(5.0)

