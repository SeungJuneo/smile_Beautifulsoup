from calendar import WEDNESDAY
import urllib.request as req
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os, glob
from PyPDF2 import PdfFileMerger, PdfFileReader


# day = input("오늘 날짜를 .을 붙여서 년도까지 쓰세오")

# code = req.urlopen("https://sgsg.hankyung.com/paper")
# soup = BeautifulSoup(code, "html.parser")
option = webdriver.ChromeOptions()
browser = webdriver.Chrome("C:/AI_파이썬/newfolders/chromedriver.exe", options=option)
browser.maximize_window()

# browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://sgsg.hankyung.com/paper/20220221/1")
time.sleep(2)
browser.switch_to.frame('pdfFrame')
browser.find_element_by_css_selector("button#download.toolbarButton.download.hiddenMediumView").click()
time.sleep(3)
browser.switch_to.default_content()
time.sleep(0.5)
browser.find_element_by_css_selector("button.btn-paper.next").click()

while True:
    pass

# time.sleep(1.5)
# browser.find_element_by_css_selector("div.cont-item").click()
# time.sleep(3)
# browser.find_element_by_css_selector("button#download").click()

# date = soup.select_one("span.date")
# paper_tab = soup.select_one("em.num > a") #다운로드 창 일부 주소
# paper_url = "https://sgsg.hankyung.com" + paper_tab.attrs["href"]
# # print(paper_url)
# code = req.urlopen(paper_url)
# soup = BeautifulSoup(code, "html.parser")
# soup = BeautifulSoup(soup, "html.parser")




# path = "./생글생글"
# filenames = glob.glob(path + '/*.pdf')
# merger = PdfFileMerger()
# for filename in filenames:
#     merger.append(PdfFileReader(open(filename, 'rb')))
#     print(filename)
        
#     merger.write(path + "/merge_files.pdf")
# if date == day:

# browser.close()
