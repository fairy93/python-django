from bs4 import BeautifulSoup
import pandas as pd
import requests


class BugsMusic(object):
    URL = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
    titles = ''
    artists = ''
    albums = ''

    # req_bugs
    def req_bugs(self):
        request = requests.get(self.URL)
        return BeautifulSoup(request.text, 'lxml')

    # 곡명(title) 순위별
    def get_chart_titles(self):
        for i in range(len(self.titles)):
            title = self.titles[i].text.strip().split('\n')[0]
            print('{:3}위 {}'.format(i + 1, title))

    # 가수(artist) 순위별
    def get_chart_artist(self):
        for i in range(len(self.artists)):
            artist = self.artists[i].text.strip().split('\n')[0]
            print('{:3}위 {}'.format(i + 1, artist))

    # 앨범(album) 순위별
    def get_chart_albums(self):
        for i in range(len(self.albums)):
            album = self.albums[i].text.strip().split('\n')[0]
            print('{:3}위 {}'.format(i + 1, album))

    # 곡명(title), 가수(artist) 순위별, 앨범(album) 순위별
    def get_chart_all(self):
        for i in range(len(self.titles)):
            title = self.titles[i].text.strip().split('\n')[0]
            artist = self.artists[i].text.strip().split('\n')[0]
            album = self.albums[i + 1].text.strip().split('\n')[0]
            print('{:3}위 ({}{}) - {}'.format(i + 1, title, album, artist))

    @staticmethod
    def main():
        b = BugsMusic()
        soup = b.req_bugs()
        b.titles = soup.select('p.title')
        b.artists = soup.select('p.artist')
        b.albums = soup.select('a.album')
        b.get_chart_all()
