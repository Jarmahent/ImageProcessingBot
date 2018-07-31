import sqlite3
import datetime
# Table is ImgurLinks fields are (url, date) TEXT



class DbConnection:

    def __init__(self):
        self._connection = sqlite3.connect("bot_db/bot.db")


    def insert_url(self, imgur_link=None):

        date = str(datetime.datetime.now().date())
        self._connection.execute('''INSERT INTO ImgurLinks(url, date)
        VALUES (?,?)
        ''',
        (imgur_link, date))
        commit_data = self._connection.commit()
        return commit_data

    def urlIsDupe(self, url):
        get_all_urls = self._connection.execute(
        "SELECT url from ImgurLinks").fetchall()

        to_list = [i[0] for i in get_all_urls]

        if str(url) in to_list:
            return True
        else:
            return False


#
# if __name__ == "__main__":
#     checker = DbConnection()
#     print(checker.urlIsDupe("thisisaurl"))
