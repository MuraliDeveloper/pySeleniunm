from selenium import webdriver

"""
<form action="">
  <select name="Python numbers">
    <option value="int">Integer</option>
    <option value="float">Float</option>
    <option value="long">Long</option>
    <option value="complex">Complex</option>
  </select>
  <br><br>
  <input type="submit">
</form>
"""
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
element = driver.find_element_by_xpath("//select[@name='Python numbers']")
all_options = element.find_elements_by_tag_name("option")

for option in all_options:
    print("Value is: ", option.get_attribute("value"))
    print("text  is: ",option.text)
    option.click()
    
#select dropdown
#<option value="int">Integer</option>
selectObj = Select(driver.find_element_by_name('city'))
all_options = selectObj.options
selectObj.select_by_index(1)
selectObj.select_by_value('hyd')
selectObj.select_by_visible_text('Mumbai')

"""
Deselect_all( )
This method enables us to clear all the selected options. It is useful when we have selected multiple items from the drop-down. If we use this method in case of a single selection, it will throw a NotImplementedError exception.

Deselect_by_index( )
This API clears the selected option using the �index� attribute. It is the inverse of the select_by_index( ) method.

Deselect_by_value( )
This API  clears the selected option using the value of the option. It is the inverse of the select_by_value( ) method.

Deselect_by_visible_text( )
This API clears the selected option using the text of the option. It is the inverse of the select_by_visible_text( ) method.

"""

