from busmusic import BugsMusic
from melon import Melon


def main():
    b = BugsMusic()
    m = Melon()
    print('벅스뮤직 차트')
    b.main()
    print('멜론 차트')
    m.main()


if __name__ == '__main__':
    main()
