from PyPDF2 import PdfFileMerger, PdfFileReader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time, os, glob

###########################################
# 1. 지면보기
#    https://sgsg.hankyung.com/paper/20220221/1
#    https://sgsg.hankyung.com/paper/20220214/1
# 크롬전체 화면
options = Options()
options.add_argument('--start-fullscreen')
# 버전 98.0.4758.102 (64비트)
br = webdriver.Chrome("D:/AI_파이썬/파이썬_생글다운/chromedriver.exe", options=options)
# br.set_window_size(1920, 1080)
url = "https://sgsg.hankyung.com/paper/20220221/1"
br.get(url)
print(">> 1. 지면보기\n")
time.sleep(2)

###########################################
# 2. 다운로드반복(24번)
#   1) 다운로드버튼
#      switch_to.frame('pdfFrame')
#      butt#down.클릭
#   2) 다음페이지
#      switch_to.default_content()
#      butt.btn.클릭
for pageNo in range(1, 3):         # range(1, 24) = 페이지 1~ 23
  print("pageNo >> ", pageNo)   # debug

  # <iframe> 시 필요
  br.switch_to.frame('pdfFrame')
  # 다운로드 <button id="download"> 
  br.find_element_by_css_selector("button#download").click()
  time.sleep(2)

  # default_content로 이동
  br.switch_to.default_content()
  # 다음 <button class="btn-paper next"> # selenium.common.exceptions.NoSuchElementException
  br.find_element_by_css_selector("button.btn-paper.next").click()

# 마지막pdf 다운
br.switch_to.frame('pdfFrame')
br.find_element_by_css_selector("button#download").click()
print(">> 2. PDF 생성 완료\n")
###########################################

# 3. pdf병합
pdf_all = "생글_전체_" + datetime.today().strftime('%Y-%m-%d') + ".pdf"
filenames = glob.glob("C:/Users/h110/Downloads/*.pdf")
merger = PdfFileMerger()
for filename in filenames:
    merger.append(PdfFileReader(open(filename, 'rb')))
    print(filename)
merger.write(pdf_all)
print(">> 3. PDF 합치기 완료")
###########################################
