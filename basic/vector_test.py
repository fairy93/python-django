# datatype.py 파일 클래스로 코딩

class VectorTest(object):
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': '30세'}

    def ls_create(self):
        self.ls.append('100')

    def ls_read(self):
        print(self.ls)

    def ls_update(self):
        self.ls = self.ls + self.tinyls

    def ls_delete(self):
        self.ls.remove(786)

    def tp_create(self):
        self.tp + ('100',)

    def tp_read(self):
        print(self.tp)

    def tp_update(self):
        self.tp = self.tp + self.tinytp

    def tp_delete(self):
        tmp = list(self.tp)
        tmp.remove(786)
        self = tuple(tmp)

    def dt_create(self):
        self.dt['tom'] = '100'

    def dt_read(self):
        print(self.dt)

    def dt_update(self):
        self.dt.update(self.tinydt)

    def dt_delete(self):
        self.dt.pop('abcd')

    @staticmethod
    def main():
        v = VectorTest()
        while 1:
            menu = input('0. Exit\n '
                         'LIST : 1. Create,2.Read,3.Update,4.Delete\n'
                         'Tuple : 5. Create,6.Read,7.Update,8.Delete\n '
                         'Dictionary : 9. Create,10.Read,11.Update,12.Delete')
            if menu == '0':
                pass
            elif menu == '1':
                v.ls_create()
            elif menu == '2':
                v.ls_read()
            elif menu == '3':
                v.ls_update()
            elif menu == '4':
                v.ls_delete()
            elif menu == '5':
                v.tp_create()
            elif menu == '6':
                v.tp_read()
            elif menu == '7':
                v.tp_update()
            elif menu == '8':
                v.tp_delete()
            elif menu == '9':
                v.dt_create()
            elif menu == '10':
                v.dt_read()
            elif menu == '11':
                v.dt_update()
            elif menu == '12':
                v.dt_delete()
            else:
                continue


VectorTest.main()
