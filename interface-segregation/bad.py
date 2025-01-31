# pylint: disable=missing-docstring, useless-super-delegation
class WashingMachine:
    def wash(self, clothes):
        pass

    def dry(self, clothes):
        pass

class PremiumWashingMachine(WashingMachine):
    def wash(self, clothes):
        return f'Washing {clothes} with premium washer...'

    def dry(self, clothes):
        return f'Drying {clothes} with premium washer...'

class BasicWasher(WashingMachine):
    def wash(self, clothes):
        return f'Washing {clothes} with basic washer...'

    def dry(self, clothes):
        # MEMO: 洗濯機によっては乾燥機能がない
        raise NotImplementedError
