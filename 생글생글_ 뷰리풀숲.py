# 파이썬 생글생글 신문 다운로드 #크롤링


#필요한 모듈들 import
from calendar import WEDNESDAY
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os, glob
from PyPDF2 import PdfFileMerger, PdfFileReader
import requests

code = req.urlopen("https://sgsg.hankyung.com/paper")
soup = BeautifulSoup(code, "html.parser")   #뷰리풀숲 모듈

#자동 다운로드 셀래니움
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# browser = webdriver.Chrome("C:/AI_파이썬/newfolders/chromedriver.exe", options=option) #셀레니움 모듈

day = soup.select_one('span.date').text
# print(day)
day2 = day.replace('.', '/')
day3 = day2.replace('/', '')        
# print(day2)

nb = 0
nb01 = str(0) + str(nb)
# print(nb01)
pdf_url = 'https://sgsg.hankyung.com/js/pdfjs/web/viewer.html?file=/pdfdata/{}/{}_0119_010{}.pdf'.format(day2, day3, nb01)
print(pdf_url)

#신문 주소 바꿔가며 다운로드 클릭
while nb < 24:      
    nb = nb + 1
    nb01 = str(0) + str(nb)
    print(nb)
    if nb < 10:
        pdf_url = 'https://sgsg.hankyung.com/js/pdfjs/web/viewer.html?file=/pdfdata/{}/{}_0119_010{}.pdf'.format(day2, day3, nb01)
        # print(pdf_url)
        browser.get(pdf_url)
        time.sleep(0.51)
        # browser.switch_to.frame('pdfFrame')
        browser.find_element_by_css_selector("button#download.toolbarButton.download.hiddenMediumView").click()
        time.sleep(0.32)

    elif nb < 25:
        pdf_url = 'https://sgsg.hankyung.com/js/pdfjs/web/viewer.html?file=/pdfdata/{}/{}_0119_010{}.pdf'.format(day2, day3, nb)
        # print(pdf_url)
        browser.get(pdf_url)
        time.sleep(0.5)
        # browser.switch_to.frame('pdfFrame')
        browser.find_element_by_css_selector("button#download.toolbarButton.download.hiddenMediumView").click()
        time.sleep(0.3)

    # elif nb < 26:
    #     pdf_url = 'https://sgsg.hankyung.com/js/pdfjs/web/viewer.html?file=/pdfdata/{}/{}_0119_010{}.pdf'.format(day2, day3, nb)
    #     # print(pdf_url)
    #     browser.get(pdf_url)
    #     time.sleep(1)
    #     # browser.switch_to.frame('pdfFrame')
    #     browser.find_element_by_css_selector("button#download.toolbarButton.download.hiddenMediumView").click()
    #     time.sleep(1)

#         time.sleep(2)

# pdf 병합
pdf_all = datetime.today().strftime('%Y-%m-%d') + " 생글생글" + ".pdf" 
filenames = glob.glob("C:/Users/corea/Downloads/*.pdf")
merger = PdfFileMerger()
for filename in filenames:
    merger.append(PdfFileReader(open(filename, 'rb')))
    print(filename)
merger.write(pdf_all)



    # code = req.urlopen(pdf_url)
    # soup = BeautifulSoup(code, "html.parser")


# https://sgsg.hankyung.com/js/pdfjs/web/viewer.html?file=/pdfdata/2022/02/21/20220221_0119_01001.pdf

# 1. 웹의 pdf 로컬에 다운
# for pageNo in range(1, 25):         # range(1, 25) = 페이지 1~ 24
    # print("pageNo >> ", pageNo)   # debug
# res = requests.get(pdf_url)
# with open("./생글생글/생글0.pdf", "wb") as f:
#     f.write(res.content)        # res.content