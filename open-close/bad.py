# pylint: disable=missing-docstring, useless-super-delegation
class Member:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def get_discount(self):
        if self.rank == 'gold':
            return 0.1
        elif self.rank == 'silver':
            return 0.05
        elif self.rank == 'bronze':
            return 0.02
        # TODO: add platinum rank
        # MEMO: 既存コードを変更する必要がある
        # elif self.rank == 'platinum':
        #     return 0.15
        else:
            return 0


gold_member = Member('John', 'gold')
silver_member = Member('Jane', 'silver')
bronze_member = Member('Joe', 'bronze')
print(gold_member.get_discount())
print(silver_member.get_discount())
print(bronze_member.get_discount())
