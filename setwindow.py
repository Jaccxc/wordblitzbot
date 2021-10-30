from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://facebook.com')
driver.set_window_position(0, 0)
driver.set_window_size(688, 1264)
