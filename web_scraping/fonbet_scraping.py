from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://fontbet.by/sports")
try: 
    elem = browser.find_element(By.CSS_SELECTOR, "css-selector")
except:
    print("there is no such an element")