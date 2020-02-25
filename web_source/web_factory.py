from selenium import webdriver

from web_source.web import Web


def get_web(browser):
    if browser == "chrome":
        # desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        # desired_capabilities['version'] = 'latest'
        # desired_capabilities['platform'] = 'WINDOWS'
        # desired_capabilities['name'] = 'Testing Selenium with Behave'
        # return Web(webdriver.Remote(
        #     desired_capabilities=desired_capabilities,
        #     command_executor="http://localhost:4445/wd/hub"
        # ))
        return Web(webdriver.Chrome("C:\\Users\\johnathan.000\\PycharmProjects\\BlazorganizerBehaveTests\\drivers\\chromedriver.exe"))
