from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = "https://www.egitimokulu.com/ingilizce-2021-il-disi-atama-puanlari/"
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
    print("\nPuan bir sayı girilmedi\nProgram devam ediyor...")
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
            City = col[0].text
            District = col[1].text
            School = col[2].text
            Marks = col[3].text
            toDb = toDb.append({"City":City, "District":District, "School":School, "Marks":Marks}, ignore_index=True)

#print(toDb)
dataFrame = pd.DataFrame(toDb)
dataFrame.to_csv("Results.csv")


#for row in tables[table_index].tbody.find_all("tr"):
#    col = row.find_all("td")
#    if (col != []):
#        rank = col[0].text
#        country = col[1].text
#        population = col[2].text.strip()
#        area = col[3].text.strip()
#        density = col[4].text.strip()
#        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)
#
#population_data
