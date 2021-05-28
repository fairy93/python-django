from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class NaverMovie(object):
    URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = 'tit3'
    driver_path = 'C:\Program Files\Google\Chrome\chromedriver.exe'
    dict = {}
    df = {}

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.URL)
        driver.implicitly_wait(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {"class": self.class_name})
        self.dict = {i + 1: all_div[i].text.strip().split('\n')[0] for i in range(len(all_div))}
        self.df = pd.DataFrame.from_dict(self.dict, orient='index').rename(columns={0: '영화제목'})
        path = './data/naverMovie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print(self.df)
        driver.close()


if __name__ == '__main__':
    naver = NaverMovie()
    naver.scrap()
