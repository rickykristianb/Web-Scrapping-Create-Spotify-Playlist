import data
import spotify


def main():
    date_in = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    date_list = date_in.split("-")
    year = date_list[0]

    web_data = data.WebScrap(date=date_in)
    title_100 = web_data.get_100_charts_title()
    singer_100 = web_data.get_100_charts_singers()
    print(title_100)

    spotify_brain = spotify.Spotify()
    # code = auth.authorization()
    spotify_brain.create_playlist(charts=title_100, year=year, date=date_in)


if __name__ == '__main__':
    main()
