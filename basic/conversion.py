import pandas as pd
import pandas as pd


class Conversion(object):
    ls = []
    tp = ()
    dict = {}
    str = ''
    n = 0
    f = 0.0
    frame = ''

    def set_tp(self):
        for i in range(1, 11):
            self.tp += (i,)
        return self.tp

    def change_tp(self):
        self.ls = list(self.tp)
        return self.ls

    def change_ls_f(self):
        self.ls = list(map(float, self.ls))
        return self.ls

    def change_ls_int(self):
        self.ls = list(map(int, self.ls))
        return self.ls

    def change_ls_dict(self):
        self.dict = {str(i): self.ls[i] for i in range(len(self.ls))}
        return self.dict

    def chang_str_tp(self):
        self.tp = tuple('hello')
        return self.tp

    def chang_ls(self):
        self.ls = list(self.tp)
        return self.ls

    def chang_def_frame(self):
        return print(pd.DataFrame.from_dict(self.dict, orient='index').rename(columns={0: 'col'}))

    @staticmethod
    def main():
        c = Conversion()
        while True:
            m = int(input('0 종료 1 튜플생성 2 튜플->리스트 3 리스트->실수형으로 4 실수형리스트->정수형리스트 5 리스트->딕셔너리 6 "hello"->튜플로 7 튜플을->리스트 8딕셔너리->데이터 프레임'))
            if m == 0:
                print('프로그램 종료')
                break
            # 1번 / 1~10 요소를 가진튜플을 생성하시오
            elif m == 1:
                print(c.set_tp())
            # 2번 / 1번 튜플을 리스트로 전환하시오
            elif m == 2:
                print(c.change_tp())
            # 3번 / 2번의 리스트를 실수(float) 리스트로 바꾸시오
            elif m == 3:
                print(c.change_ls_f())
            # 4번 / 3번의 정수리스트로 바꾸시오
            elif m == 4:
                print(c.change_ls_int())
            # 5번 / 4번에서만든 리스트를 딕셔너리로 전환하시오
            elif m == 5:
                print(c.change_ls_dict())
            # 6번 / hello를 튜플로 전환하시오
            elif m == 6:
                print(c.chang_str_tp())
            # 7번 / 튜플을 리스트로  
            elif m == 7:
                print(c.chang_ls())
            #8번 / 딕셔너리를 데이터프레임으로
            elif m == 8:
                print(c.chang_def_frame())
            else:
                continue


# 캡슐화
Conversion.main()
