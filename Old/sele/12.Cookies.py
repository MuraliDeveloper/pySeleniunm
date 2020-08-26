driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {"name" :"foo", "value" : "bar"}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
cookies = self.driver.get_cookies()

for cookie in cookies:
    print(cookie)


browser=webdriver.Firefox()
browser.get("https://reddit.com")
print(browser.get_cookies())
browser.add_cookie({"name":"python","domain":"reddit.com","value":"python"})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()