import sqlite3

import requests
from bs4 import BeautifulSoup

try:
    # Database creation
    conn = sqlite3.connect('Database.sqlite')
    # Database Handler
    cur = conn.cursor()
    # Database table
    cur.executescript('''
    DROP TABLE IF EXISTS TeacherData
    ''')
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS TeacherData (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    city TEXT,
    district TEXT,
    school TEXT,
    points INTEGER
    )
    ''')

except Exception as E1:
    print('E1: Database creation error')
    print(E1)

conn.commit()

links = {
    1: "https://www.egitimokulu.com/beden-egitimi-2021-il-disi-atama-puanlari/",
    2: "https://www.egitimokulu.com/bilisim-teknolojileri-2021-il-disi-atama-puanlari/",
    3: "https://www.egitimokulu.com/cografya-2021-il-disi-atama-puanlari/",
    4: "https://www.egitimokulu.com/din-kulturu-ve-ahlak-bilgisi-2021-il-disi-atama-puanlari/",
    5: "https://www.egitimokulu.com/elektrik-elektronik-2021-il-disi-atama-puanlari/",
    6: "https://www.egitimokulu.com/felsefe-2021-il-disi-atama-puanlari/",
    7: "https://www.egitimokulu.com/fen-bilimleri-2021-il-disi-atama-puanlari/",
    8: "https://www.egitimokulu.com/gorsel-sanatlar-2021-il-disi-atama-puanlari/",
    9: "https://www.egitimokulu.com/ilkogretim-matematik-2021-il-disi-atama-puanlari/",
    10: "https://www.egitimokulu.com/ingilizce-2021-il-disi-atama-puanlari/",
    11: "https://www.egitimokulu.com/kimya-2021-il-disi-atama-puanlari/",
    12: "https://www.egitimokulu.com/matematik-2021-il-disi-atama-puanlari/",
    13: "https://www.egitimokulu.com/muzik-2021-il-disi-atama-puanlari/",
    14: "https://www.egitimokulu.com/okul-oncesi-anaokulu-2021-il-disi-atama-puanlari/",
    15: "https://www.egitimokulu.com/ozel-egitim-2021-il-disi-atama-puanlari/",
    16: "https://www.egitimokulu.com/rehberlik-2021-il-disi-atama-puanlari/",
    17: "https://www.egitimokulu.com/sinif-ogretmenligi-2021-il-disi-atama-puanlari/",
    18: "https://www.egitimokulu.com/sosyal-bilgiler-2021-il-disi-atama-puanlari/",
    19: "https://www.egitimokulu.com/tarih-2021-il-disi-atama-puanlari/",
    20: "https://www.egitimokulu.com/teknoloji-ve-tasarim-2021-il-disi-atama-puanlari/",
    21: "https://www.egitimokulu.com/turkce-2021-il-disi-atama-puanlari/",
    22: "https://www.egitimokulu.com/turk-dili-ve-edebiyati-2021-il-disi-atama-puanlari/"
}

print(
    "\n"
    " 1 -> Beden Egitimi", "\n",
    "2 -> Bilisim Teknolojileri", "\n",
    "3 -> Cografya", "\n",
    "4 -> Din Kulturu", "\n",
    "5 -> Elektrik Elektronik", "\n",
    "6 -> Felsefe", "\n",
    "7 -> Fen Bilimleri", "\n",
    "8 -> Gorsel sanatlar", "\n",
    "9 -> Ilkogretim Matematik", "\n",
    "10 -> Inglizce", "\n",
    "11 -> Kimya", "\n",
    "12 -> Matematik", "\n",
    "13 -> Muzik", "\n",
    "14 -> Okul Oncesi Anaokulu", "\n",
    "15 -> Ozel Egitim", "\n",
    "16 -> Rehberlik", "\n",
    "17 -> Sinif Ogretmenligi", "\n",
    "18 -> Sosyal Bilgiler", "\n",
    "19 -> Tarih", "\n",
    "20 -> Teknoloji ve Tasarim", "\n",
    "21 -> Turkce", "\n",
    "22 -> Turk Dili ve Edebiyati", "\n",

)

field = int(input("Choose a Field:"))
url = links[field]
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")
tables = soup.find_all('table')  # in html table is represented by the tag <table>

for index, table in enumerate(tables):
    table_index = index

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    city = col[0].text.strip()
    district = col[1].text.strip()
    school = col[2].text.strip()
    points = col[3].text.strip()
    try:
        # first we start to write the data to the database
        cur.execute('''INSERT OR IGNORE INTO TeacherData (city, district, school, points)
        VALUES (?,?,?,?)''', (city, district, school, points))
        cur.execute('DELETE FROM TeacherData WHERE city = "??l Ad??"')
    except Exception as E2:
        print('E2: Database writing error')
        print(E2)

    conn.commit()

# to check the results
try:
    cur.execute('SELECT city, district, school,points FROM TeacherData WHERE city = "ADANA" AND points < 200;')
    result = cur.fetchall()
    # print(result,"\n")
except Exception as E3:
    print('E3: Data checking error')
    print(E3)
conn.commit()

unique_cities = cur.execute('SELECT DISTINCT(city) from TeacherData')
city_dict = {}
counter = -1
for i in unique_cities:
    counter = counter + 1
    print(counter, i)
    city_dict[counter] = i
city_choice = int(input("choose a city:"))
print(city_dict[city_choice])
