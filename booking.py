from time import time
from selenium import webdriver
import os
import time
from soupsieve import select
from booking.constants import BASE_URL
from booking.booking_filteration import bookingFilteration
from booking.booking_report import Report

class Booking(webdriver.Chrome):
    def __init__(self,driver_path="D:/tools",tearDown=False):
        self.driver_path = driver_path
        self.tearDown = tearDown
        os.environ['PATH'] += self.driver_path 
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",['enable-logging'])
        super(Booking,self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.tearDown:
            self.quit()
    
    def land_home_page(self):
        self.get(BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        currency_change_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        currency_change_element.click()
    
    def select_place_to_go(self,place_to_go):
        search_field = self.find_element_by_id("ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        if place_to_go == "Pakistan":
            first_result = self.find_element_by_css_selector(
                'li[data-i="1"]'
            )
        else:
            first_result = self.find_element_by_css_selector(
                'li[data-i="0"]'
            )
        first_result.click()
    
    def select_dates(self, check_in,check_out):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        check_out_element.click()
    
    def adult_select(self,count=2):
        detailField = self.find_element_by_id("xp__guests__toggle")
        detailField.click()
        if count != 2:
            if count == 1:
                adult1 = self.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/button[1]/span')
                adult1.click()
            else:
                i = 2
                while True:
                    adultM = self.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/button[2]/span')
                    adultM.click()
                    i = i + 1
                    if count == i:
                        break
    
    def child_select(self,agee,count=0):
        i = 0
        if count != 0:
            while True:
                child = self.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]/span')
                child.click()
                age = self.find_element_by_css_selector(
                    f'select[data-group-child-age="{i}"]'
                )
                age.click()
                ages = self.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[3]/select[{i+1}]/option[{agee+2}]')
                ages.click()
                i = i + 1
                if count == i:
                    break
    
    def room_select(self,count=1):
        i = 1
        if count != 1:
            while True:
                room = self.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[4]/div/div[2]/button[2]/span')
                room.click()
                i = i + 1
                if i == count:
                    break

    def search(self):
        search_button = self.find_element_by_css_selector(
            'button[data-sb-id="main"]'
        )            
        search_button.click()
                
    def apply_filterations(self):
        booking = bookingFilteration(driver = self)
        booking.star_rating(1,5)
        time.sleep(1)
        booking.lowest_price()

    def report_result(self):
        hotel_box = self.find_element_by_id('search_results_table')
        report = Report(hotel_box)
        report.Get_details()