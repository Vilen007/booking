from selenium.webdriver.remote.webelement import WebElement

class Report:
    def __init__(self, hotel_boxes:WebElement):
        self.hotel_boxes = hotel_boxes
        self.hotel_box = self.hotel_box_pull()
    
    def hotel_box_pull(self):
        return self.hotel_boxes.find_elements_by_css_selector(
            'div[data-testid="property-card"]'
        )

    def Get_details(self):
        details = []
        for box in self.hotel_box:
            hotel_name = box.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute("innerHTML").strip()
            details.append(hotel_name)
        print(details)