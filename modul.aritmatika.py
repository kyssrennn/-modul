# nama file ; modulAritmatika
import aritmatika

def main():
    a = int(input('Masukan nilai a :  '))
    b = int(input('Masukan nilai b :  '))

    print('a\t: %d' %a)
    print('b\t: %d' %b)

    print('a=b\t: %d' % aritmatika.tambah(a, b))
    print('')