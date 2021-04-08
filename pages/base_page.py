class BasePage():
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_browser(self):
        self.browser.get(self.link)
        self.browser.implicitly_wait(10)
