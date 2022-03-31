from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
# First the teacher must provide some information:
# 1- Working field.
# 2- Teacher's Marks.
# 3- Desired City.
# 4- Desired District and School.
# the program must return all the reuslts if no inforamtion was given.
# the program must save all the data in a database.
# the program must have an interactive web app to allow maximum benifet.
"""
2021 links count 22:
https://www.egitimokulu.com/beden-egitimi-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/bilisim-teknolojileri-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/cografya-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/din-kulturu-ve-ahlak-bilgisi-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/elektrik-elektronik-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/felsefe-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/fen-bilimleri-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/gorsel-sanatlar-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/ilkogretim-matematik-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/ingilizce-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/kimya-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/matematik-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/muzik-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/okul-oncesi-anaokulu-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/ozel-egitim-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/rehberlik-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/sinif-ogretmenligi-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/sosyal-bilgiler-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/tarih-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/teknoloji-ve-tasarim-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/turkce-2021-il-disi-atama-puanlari/
https://www.egitimokulu.com/turk-dili-ve-edebiyati-2021-il-disi-atama-puanlari/
"""
links = {
"beden":"https://www.egitimokulu.com/beden-egitimi-2021-il-disi-atama-puanlari/",
"bilTek":"https://www.egitimokulu.com/bilisim-teknolojileri-2021-il-disi-atama-puanlari/",
"cografya":"https://www.egitimokulu.com/cografya-2021-il-disi-atama-puanlari/",
"din":"https://www.egitimokulu.com/din-kulturu-ve-ahlak-bilgisi-2021-il-disi-atama-puanlari/",
"elektrik":"https://www.egitimokulu.com/elektrik-elektronik-2021-il-disi-atama-puanlari/",
"felsefe":"https://www.egitimokulu.com/felsefe-2021-il-disi-atama-puanlari/",
"fenBil":"https://www.egitimokulu.com/fen-bilimleri-2021-il-disi-atama-puanlari/",
"gorSan":"https://www.egitimokulu.com/gorsel-sanatlar-2021-il-disi-atama-puanlari/",
"ilkMat":"https://www.egitimokulu.com/ilkogretim-matematik-2021-il-disi-atama-puanlari/",
"ingilizce":"https://www.egitimokulu.com/ingilizce-2021-il-disi-atama-puanlari/",
"kimya":"https://www.egitimokulu.com/kimya-2021-il-disi-atama-puanlari/",
"matematik":"https://www.egitimokulu.com/matematik-2021-il-disi-atama-puanlari/",
"muzik":"https://www.egitimokulu.com/muzik-2021-il-disi-atama-puanlari/",
"okulOnce":"https://www.egitimokulu.com/okul-oncesi-anaokulu-2021-il-disi-atama-puanlari/",
"ozelEgit":"https://www.egitimokulu.com/ozel-egitim-2021-il-disi-atama-puanlari/",
"rehberlik":"https://www.egitimokulu.com/rehberlik-2021-il-disi-atama-puanlari/",
"sinifOgre":"https://www.egitimokulu.com/sinif-ogretmenligi-2021-il-disi-atama-puanlari/",
"sosyal":"https://www.egitimokulu.com/sosyal-bilgiler-2021-il-disi-atama-puanlari/",
"tarih":"https://www.egitimokulu.com/tarih-2021-il-disi-atama-puanlari/",
"tekVeTas":"https://www.egitimokulu.com/teknoloji-ve-tasarim-2021-il-disi-atama-puanlari/",
"turkce":"https://www.egitimokulu.com/turkce-2021-il-disi-atama-puanlari/",
"turkDili":"https://www.egitimokulu.com/turk-dili-ve-edebiyati-2021-il-disi-atama-puanlari/"
}
print(
    "\n"
    " 1 -> Beden Egitimi","\n",
    "2 -> Bilisim Teknolojileri","\n",
    "3 -> Cografya","\n",
    "4 -> Din Kulturu","\n",
    "5 -> Elektrik Elektronik","\n",
    "6 -> Felsefe","\n",
    "7 -> Fen Bilimleri","\n",
    "8 -> Gorsel sanatlar","\n",
    "9 -> Ilkogretim Matematik","\n",
    "10 -> Inglizce","\n",
    "11 -> Kimya","\n",
    "12 -> Matematik","\n",
    "13 -> Muzik","\n",
    "14 -> Okul Oncesi Anaokulu","\n",
    "15 -> Ozel Egitim","\n",
    "16 -> Rehberlik","\n",
    "17 -> Sinif Ogretmenligi","\n",
    "18 -> Sosyal Bilgiler","\n",
    "19 -> Tarih","\n",
    "20 -> Teknoloji ve Tasarim","\n",
    "21 -> Turkce","\n",    
    "22 -> Turk Dili ve Edebiyati","\n",    

)
"""a loop to choose a feild and give it the link for it"""

feild = int(input("Feild seç:"))
for i in range(1,23):
    if i == feild:
        print(i, links["beden"])
    else:
        break


English = "https://www.egitimokulu.com/ingilizce-2021-il-disi-atama-puanlari/"
#if field == "English":
#    print("English")
url = English
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")
tables = soup.find_all('table') # in html table is represented by the tag <table>

toDb = pd.DataFrame(columns=["City", "District", "School","Marks"])
for index,table in enumerate(tables):
    table_index = index

# Check Section
print("\nÖzelleştirmeleri giriniz [Uygulamamak için boş bırakın]\n")
try:
    city = str(input("Şehir ismi giriniz: "))
    district = str(input("İlçe ismi giriniz: "))
    mark = int(input("maksimum puan giriniz: "))
except:
    print("\nPuan bir sayı girilmedi\nProgram Tum Puanlar Gosteryor...")
    mark = 1000

#print(tables[table_index].prettify())
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")

    # Check Section - bool variables
    cityCheck = city.lower().strip() in col[0].text.strip().lower()
    districtCheck = district.lower().strip() in col[1].text.strip().lower()
    try:
        markCheck = int(col[3].text.strip()) <= mark
    except:
        markCheck = True

    if (col != []):
        if (cityCheck and districtCheck and markCheck):
            City = col[0].text.lower().strip()
            District = col[1].text.lower().strip()
            School = col[2].text.lower().strip()
            Marks = col[3].text.lower().strip()
            toDb = toDb.append({"City":City, "District":District, "School":School, "Marks":Marks}, ignore_index=True)

dataFrame = pd.DataFrame(toDb)
dataFrame.to_csv("Results.csv")
