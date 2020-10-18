from selenium import webdriver
"""
how to get all rows?
rows = driver.find_elements_by_xpath("/html/body/table/tbody/tr")  #gets all the Table rows


how to get all cols?
cols = driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")  #gets all the Table cols

"""
from basics.commons import getChromeDriver

driver = getChromeDriver()
driver.maximize_window()
driver.get("")

rows = driver.find_elements_by_xpath("/html/body/table/tbody/tr")  #gets all the Table rows
print(len(rows))

cols = driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")  #gets all the Table rows
print(len(cols))

print(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[1]").text)
print(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[2]").text)
print(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th[3]").text)



print(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]").text)
print(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[3]").text)

print("print all")
for r in range(1,len(rows)+1): #print 1st 4 rows
    for c in range(1,len(cols)+1):
        data= driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/th["+str(c)+"]")
        print(data.text)
driver.quit() #close all windows