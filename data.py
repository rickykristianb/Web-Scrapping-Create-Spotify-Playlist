import requests
import bs4

URL = "https://www.billboard.com/charts/hot-100/"

class WebScrap():

    def __init__(self, date):
        self.date = date
        response = requests.get(url=f"{URL}{self.date}/")
        contents = response.text
        self.soup = bs4.BeautifulSoup(contents, "html.parser")

    def get_100_charts_title(self):
        charts_titles = self.soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
        no1_title = self.soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
        chart1_title = no1_title.get_text().strip()
        song_title = [title.text.strip() for title in charts_titles]
        song_title.insert(0, chart1_title)
        return song_title

    def get_100_charts_singers(self):
        singers = self.soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
        chart_singers = [singer.text.strip() for singer in singers]
        no1_singers = self.soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
        no1 = no1_singers.get_text().strip()
        chart_singers.insert(0, no1)
        return chart_singers
        
