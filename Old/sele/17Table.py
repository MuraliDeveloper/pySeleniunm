from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("")

rows = driver.find_elements_by_xpath("/html/body/table/tbody/tr")  #gets all the Table rows
print(len(rows))

cols = driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")  #gets all the Table rows
print(len(cols))

for r in range(2,rows+1): #print 1st 4 rows
    for c in range(1,cols+1):
        data= driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/th["+str(c)+"]")
        print(data.text)
driver.quit() #close all windows