class Gugudan(object):
    dan = 0

    def mul(self):
        for i in range(1, 10):
            print(f'{self.dan} * {i} = {self.dan * i}')

    @staticmethod
    def all_mul():
        for i in range(2, 10):
            print('------------------------')
            for j in range(1, 10):
                print(f'{i} * {j} = {j * i}')

    @staticmethod
    def main():
        g = Gugudan()
        while True:
            menu = int(input('메뉴 0 종료 1 1~9구구단출력 2 all단'))
            if menu == 0:
                print('구구단 종료')
                break
            elif menu == 1:
                g.dan = int(input('1~9 구구단출력'))
                g.mul()
            else:
                g.all_mul()
                pass


Gugudan.main()
