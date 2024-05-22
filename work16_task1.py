class kassa(object):
    def __init__(self, b):
        self.balans = b

    def top_up(self, a):
        self.balans += a
        print(f'В кассе {self.balans} денег.')

    def count_1000(self):
        print(f'В кассе {self.balans // 1000} целых тысяч.')

    def take_away(self, a):
        if self.balans < a:
            print('Недостаточно денег в кассе.')
        else:
            self.balans -= a
            print(f'В кассе осталось {self.balans} рублей после снятия.')
ka = kassa(6000)
ka.take_away(6000)
