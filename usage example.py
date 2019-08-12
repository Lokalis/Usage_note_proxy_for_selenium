
from browsermobproxy import Server
from selenium import webdriver

server = Server(r"browsermob-proxy-2.1.4\bin\browsermob-proxy")

""" Preparing proxy server """
server.start()
proxy = server.create_proxy()
url='http://google.com'
proxy.new_har(title=url,options={'captureContent': True}) #captureContent -  allows you to capture Data Post in request and response


"""Add arguments in ChromeOptions"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy.proxy}")
driver = webdriver.Chrome(r"path to Webdriver",options = chrome_options)


driver.get(url)

""" Returns a HAR JSON blob"""
print(proxy.har)


driver.quit()
proxy.close()
server.stop()
