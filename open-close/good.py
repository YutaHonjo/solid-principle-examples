# pylint: disable=missing-docstring, useless-super-delegation
from abc import abstractmethod, ABCMeta


class MemberRegistry:
    def __init__(self):
        self.member_registry = {}

    def register_member(self, rank_name, rank_class):
        self.member_registry[rank_name] = rank_class

    def create_member(self, rank_name):
        if rank_name in self.member_registry:
            return self.member_registry[rank_name]
        return None


class Member(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_discount(self):
        pass


class GoldMember(Member):
    def __init__(self, name):
        super().__init__(name)

    def get_discount(self):
        return 0.1


class SilverMember(Member):
    def __init__(self, name):
        super().__init__(name)

    def get_discount(self):
        return 0.05

class BronzeMember(Member):
    def __init__(self, name):
        super().__init__(name)

    def get_discount(self):
        return 0.02

# TODO: add PlatinumMember class
# MEMO: 既存のMemberクラスを変更せずに、新しいクラスを追加する
# class PlatinumMember(Member):
#     def __init__(self, name):
#         super().__init__(name)

#     def get_discount(self):
#         return 0.15

member_registry = MemberRegistry()
# TODO: add platinum rank to member_registry
member_registry.register_member('gold', GoldMember)
member_registry.register_member('silver', SilverMember)
member_registry.register_member('bronze', BronzeMember)

gold_member = member_registry.create_member('gold')('John')
silver_member = member_registry.create_member('silver')('Jane')
bronze_member = member_registry.create_member('bronze')('Joe')
print(gold_member.get_discount())
print(silver_member.get_discount())
print(bronze_member.get_discount())
