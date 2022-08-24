from selenium.webdriver.remote.webdriver import WebDriver

class bookingFilteration:
    def __init__(self, driver:WebDriver):
        self.driver= driver

    def star_rating(self,*starValue):
        stars_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_box_child = stars_box.find_elements_by_css_selector('*')
        for star in starValue:
            for child in star_box_child:
                if star == 1:
                    if str(child.get_attribute("innerHTML")).strip() == f'{star} star':
                        child.click()
                else:
                    if str(child.get_attribute("innerHTML")).strip() == f'{star} stars':
                        child.click()
    
    def lowest_price(self):
        price = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        price.click()

        
    
