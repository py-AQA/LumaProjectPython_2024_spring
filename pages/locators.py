

class SalePageLocators():
    GEAR_DEALS_TITLE = "//*[text()='Gear Deals']"
    BAGS_LINK = "//a[text()='Bags']"
    FITNESS_EQUIPMENT_LINK = "//a[text()='Fitness Equipment']"


class ProductLocators():
    RADIANT_TEE_URL = 'https://magento.softwaretestingboard.com/radiant-tee.html'
    RADIANT_TEE_SIZE = '[option-label="XS"]'
    RADIANT_TEE_COLOR = '[option-label="Orange"]'
    RADIANT_TEE_QTY = '#qty'
    ADD_TO_CART_BUTTON = '#product-addtocart-button'

    ARGUS_All_WEATHER_TANK = '[alt="Argus All-Weather Tank"]'
    ARGUS_All_WEATHER_TANK_SIZE = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="M"]'
    ARGUS_All_WEATHER_TANK_COLOR = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="Gray"]'
    ARGUS_All_WEATHER_TANK_ADD_TO_CARD = '//*[@title="Argus All-Weather Tank"]/../..//*[@title="Add to Cart"]'
    MINI_BASKET_WINDOW = '[class="action showcart"]'




class BaseLocators():
    PAGE_NAME = ".base"