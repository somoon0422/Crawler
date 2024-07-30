import requests # 웹 사이트에 요청을 보내고 응답을 받는 라이브러리
from bs4 import BeautifulSoup # HTML을 파싱하는 라이브러리
import urllib.request as req # url을 열고 html을 읽어오는 라이브러리
from selenium import webdriver # 웹드라이버를 사용하기 위한 라이브러리
from time import sleep # sleep을 사용하기 위한 라이브러리
from selenium.webdriver.common.by import By # 웹드라이버에서 By를 사용하기 위한 라이브러리


def book_futsal_reservation(court_name):
    
     # 크롬드라이버 사용 지정
    driver = webdriver.Chrome('./chromedriver')

    # HTML 가져오기
    url =  "http://www.futsalbase.com/login"

    # 크롬드라이버로 url 열기
    driver.get(url)

    # 검색어 입력    
    id = driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div[2]/div[1]/div[1]/div[1]").send_keys(input_id)
    password = driver.find_element(By.XPATH, "/html/body/div/div/div/section/div/div[2]/div[1]/div[1]/div[2]").send_keys(input_password)

    # 페이지 로딩 기다리기
    sleep(1)

    # 검색 버튼 클릭
    login_btn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > section > div > div.form-wrap > div.form.row > div.col-12.col-md-4.p-0.pl-md-2.pt-2.pt-md-0 > button').click()
    sleep(1)
    

if __name__ == "__main__":
    court_name = int(input("코트 번호를 입력하세요 : "))
    input_id = input("아이디를 입력하세요 : ")
    input_password = input("비밀번호를 입력하세요 : ")
    book_futsal_reservation(court_name)
    print('-- Crawling Complete --')
