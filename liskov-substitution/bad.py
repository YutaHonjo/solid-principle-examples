# pylint: disable=missing-docstring, useless-super-delegation
class Toaster:
    def make_toast(self):
        return 'Making toast...'

class Human(Toaster):
    def eat_toast(self):
        # 継承しているのに、Humanクラスにはmake_toastメソッドがない
        toast = self.make_toast()
        return f'Eating {toast}'