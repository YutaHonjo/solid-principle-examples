# pylint: disable=missing-docstring, useless-super-delegation
class Toaster:
    def make_toast(self):
        return 'Making toast...'

class Human:
    def __init__(self):
        self.toaster = Toaster()

    def eat_toast(self):
        # 継承ではなく、委譲を使う
        toast = self.toaster.make_toast()
        return f'Eating {toast}'


class PremiumToaster(Toaster):
    def make_toast(self):
        # 親クラスと同じメソッドを持つなら、継承しても問題ない
        return 'Making premium toast...'