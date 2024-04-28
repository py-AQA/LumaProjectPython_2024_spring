

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


class HomeLocators:
    STORE_LOGO = 'a.logo'


class NavigatorLocators:
    NAV_NEW = '#ui-id-3'
    NAV_WOMEN = '#ui-id-4'
    NAV_MEN = '#ui-id-5'
    NAV_GEAR = '#ui-id-6'
    NAV_TRAINING = '#ui-id-7'
    NAV_SALE = '#ui-id-8'    


class SideBarLocators:
    BREADCRUMBS = '.breadcrumbs'
    ITEM_HOME = '.item.home a'
    SIDEBAR_MAIN = '.sidebar.sidebar-main'
    CATEGORIES_MENU = '.categories-menu'
    FILTER = '.block.filter'


class BaseLocators():
    PAGE_NAME = ".base"