from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")