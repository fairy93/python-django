from bs4 import BeautifulSoup
import requests


class BugsMusic(object):
    URL = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'

    # 곡명(title) 순위별
    @staticmethod
    def get_chart_titles(titles):
        for i in range(len(titles)):
            title = titles[i].text.strip().split('\n')[0]
            print('{:3}위 {}'.format(i + 1, title))

    # 가수(artist) 순위별
    @staticmethod
    def get_chart_artist(artists):
        for i in range(len(artists)):
            artist = artists[i].text.strip().split('\n')[0]
            print('{:3}위 {}'.format(i + 1, artist))

    # 앨범(album) 순위별
    @staticmethod
    def get_chart_albums(albums):
        for i in range(len(albums)):
            album = albums[i].text.strip().split('\n')[0]
            print('{:3}위 {}'.format(i + 1, album))

    # 곡명(title), 가수(artist) 순위별, 앨범(album) 순위별
    @staticmethod
    def get_chart_all(titles, artists, albums):
        for i in range(len(titles)):
            title = titles[i].text.strip().split('\n')[0]
            artist = artists[i].text.strip().split('\n')[0]
            album = albums[i+1].text.strip().split('\n')[0]
            print('{:3}위 ● 가수{} ● 곡명{} ● 앨범{}'.format(i + 1, title, artist, album))

    @staticmethod
    def main():
        request = requests.get(BugsMusic.URL)
        html = request.text
        soup = BeautifulSoup(html, 'lxml')
        titles = soup.select('p.title')
        artists = soup.select('p.artist')
        albums = soup.select('a.album')
        BugsMusic.get_chart_all(titles, artists, albums)
