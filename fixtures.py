from selenium import webdriver
from web_source.web import Web


def browser_chrome(context, timeout=30, **kwargs):
    # desired_capabilities = webdriver.DesiredCapabilities.CHROME
    # desired_capabilities['version'] = 'latest'
    # desired_capabilities['platform'] = 'WINDOWS'
    # desired_capabilities['name'] = 'Testing Selenium with Behave'
    #
    # browser = webdriver.Remote(
    #     desired_capabilities=desired_capabilities,
    #     command_executor="http://localhost:4445/wd/hub"
    # )
    # web = Web(browser)
    # context.web = web
    # yield context.web
    # browser.quit()
    browser = webdriver.Chrome(executable_path="/drivers/chromedriver.exe")
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()
