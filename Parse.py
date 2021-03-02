import json
import os
import requests

from bs4 import BeautifulSoup
import math
import sys
from tkinter import filedialog
from tkinter import *
from time import sleep
import aiohttp
import asyncio
import async_timeout

from PySide2.QtWidgets import QApplication, QMainWindow

from Window import Ui_MainWindow

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
           'accept': '*/*'}

# Создаем приложение
app = QApplication(sys.argv)

# Создаем окно и инициализируем его
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_soup():
    link_book = ui.lineEdit.text()
    html = get_html(link_book, params=None)
    return BeautifulSoup(html.text, 'html.parser')  # общий суп, кастрюля


def get_json():
    soup = get_soup()  # общий суп, кастрюля
    content = str(soup.find_all('script')[13])

    start_big_index = content.find('*/')
    finish_big_index = content.find('cur.bookPlayer')
    fine_content = content[start_big_index:finish_big_index]
    start_fine_index = fine_content.find('[{"id"')
    finish_fine_index = fine_content.find(', [{"label"')

    refine_content = fine_content[start_fine_index:finish_fine_index]
    return json.loads(refine_content)


def pb_info():
    duration_list = []
    for url_track in get_json():
        duration_list.append(url_track['duration_float'])

    duration_total = sum(duration_list)
    duration_hours = math.floor(duration_total / 3600)
    duration_mins = math.floor((duration_total - (duration_hours * 3600)) / 60)
    duration_secs = math.ceil(duration_total - ((duration_hours * 3600) + (duration_mins * 60)))
    str(duration_hours) + ':' + str(duration_mins) + ':' + str(duration_secs)
    duration = str(duration_hours) + 'ч:' + str(duration_mins) + 'м:' + str(duration_secs) + 'с'

    ui.label_time_value.setText(duration)

    number_of_tracks = str(len(duration_list)) + ' шт'

    ui.label_tracks.setText(number_of_tracks)

    items = get_soup().find_all("div", class_="page_content")

    for item in items:
        authors = item.find_all("span", itemprop="author")
        name_book = item.find_all("span", itemprop="name")
        reads = item.find_all("span", class_="book_title_elem")
        description = item.find('div', class_='book_page clearfix').find('div', itemprop="description").get_text()

        ui.textBrowser.setText(description)

        for author in authors:
            author_book = author.get_text(strip=True)
            ui.label_author_value.setText(author_book)
        for name in name_book:
            book = name.get_text(strip=True)
            ui.label_book_value.setText(book)
        for re in reads:
            try:
                red = re.find('a').get_text()
                ui.label_reads_value.setText(red)
            except:
                pass


def tb():
    global folder_func_tb
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    folder_func_tb = str(folder_selected).replace("/", "\ ").replace(" ", "")
    ui.lineEdit_way.setText(folder_func_tb)


def start_button():
    url_track_list = []
    number_of_track = []
    for url_track in get_json():
        url_track_list.append([url_track['url'], url_track['title']])
        number_of_track.append(url_track['title'])

    items = get_soup().find_all("div", class_="page_content")
    for item in items:
        name_book = item.find_all("span", itemprop="name")
        for name in name_book:
            book = name.get_text(strip=True)

    directory = folder_func_tb + '/' + book
    os.mkdir(directory)

    ui.textBrowser_progress.append('Начинается копирование книги' + book)

    async def download(session, url, abs_path_name, value_progress, track_number):

        ui.textBrowser_progress.append('Загружен файл ' + track_number)
        ui.progressBar.setValue(value_progress)

        with async_timeout.timeout(10):
            async with session.get(url) as response:
                with open(abs_path_name, 'wb') as file:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        file.write(chunk)
                return await response.release()

    async def main(loop):
        for count, track in enumerate(url_track_list):
            track_url = track[0]
            track_number = track[1] + '.mp3'
            abs_path_name = directory + '/' + track_number

            len_of_list = len(url_track_list)
            value_progress = ((count + 1) * (100 / len_of_list))

            async with aiohttp.ClientSession(loop=loop) as session:
                await asyncio.gather(download(session, track_url, abs_path_name, value_progress, track_number))


    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(loop))


ui.pushButton_info.clicked.connect(pb_info)

ui.toolButton_way.clicked.connect(tb)

ui.pushButton.clicked.connect(start_button)

sys.exit(app.exec_())
