from selenium.webdriver.support.select import Select

from seleniumEx.myBasetest import BaseTest
import time

class FormTest(BaseTest):


    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get("http://localhost:8087/myapp/form.html")
        time.sleep(2)
        # self.assertEqual("welcome to form1", self.driver.title,"invalid title for form.html")

    """
   how to check if element is enabled and displayed:
        element.is_enabled() -> returns boolean
        element.is_displayed() -> returns boolean
        
        
   How to get the attribute for the web element?
   use getAttribute()
  ex:
     <input type="text" id="myname" name="uName" class="abcd>
      firstNameObj = self.driver.find_element_by_name("uName")
      
      get type:
      ----------
      firstNameType = firstNameObj.getAttribute("type")  #text
      firstNameId = firstNameObj.getAttribute("id")  #myname
      firstNameclass  =  firstNameObj.getAttribute("class")  #abcd
   
   How to send data to the text field
     element.send_keys("kumar")

    """
    def testFirstName(self):
        #<input type="text" id="myname" name="uName">
        #get web element obj
        firstNameObj = self.driver.find_element_by_name("uName")

        # validate web elements obj
        self.assertTrue(firstNameObj.is_enabled())
        self.assertTrue(firstNameObj.is_displayed())

        #validate the type
        firstNameType = firstNameObj.get_attribute("type")
        self.assertEqual("text",firstNameType)

        firstNameObj.send_keys("krishna")
        time.sleep(3)

    def testMiddleName(self):
        # <input type="text" name="uName1" readonly="readonly" value="kumar">
        # get web element obj
        middleNameObj = self.driver.find_element_by_name("uName1")

        # validate web elements obj
        self.assertTrue(middleNameObj.is_enabled())
        self.assertTrue(middleNameObj.is_displayed())

        # validate the type
        middleNameType = middleNameObj.get_attribute("type")
        self.assertEqual("text", middleNameType)

        #validate readonly
        middleNameRead = middleNameObj.get_attribute("readonly")
        self.assertTrue(middleNameRead)

        #get value
        middleNameValue = middleNameObj.get_attribute("value")
        self.assertEqual("kumar", middleNameValue)


     #<input type="text" name="uName2" disabled="disabled">
    def testSurName(self):
        # get web element obj
        surNameObj =  self.driver.find_element_by_name("uName2")

        # validate web elements obj
        self.assertFalse(surNameObj.is_enabled())
        self.assertTrue(surNameObj.is_displayed())

        # validate the type
        type = surNameObj.get_attribute("type")
        self.assertEqual("text", type)

        self.assertTrue(surNameObj.get_attribute("disabled"))


     #<input type="text" name="LName" size="30" width="30">
    def testLastName(self):
        # get web element obj
        lastNameObj = self.driver.find_element_by_name("LName")

        # validate web elements obj
        self.assertTrue(lastNameObj.is_enabled())
        self.assertTrue(lastNameObj.is_displayed())

        # validate the type
        lastNameType = lastNameObj.get_attribute("type")
        self.assertEqual("text", lastNameType)

        # validate the size
        self.assertEqual("30", lastNameObj.get_attribute("size"))
        lastNameObj.send_keys("varma")

        time.sleep(3)

     #<input type="password" name="password">
    def testPassword(self):
        # get web element obj
        passwordObj =  self.driver.find_element_by_name("password")

        # validate web elements obj
        self.assertTrue(passwordObj.is_enabled())
        self.assertTrue(passwordObj.is_displayed())

        # validate the type
        passwordType = passwordObj.get_attribute("type")
        self.assertEqual("password", passwordType)

        passwordObj.send_keys("admin@123")
        time.sleep(3)


    #<input type="radio" name="gender" id="mRadio" value="male" checked="">
    #<input type="radio" name="gender" id="fRadio" value="female">
    #<input type="radio" name="gender" id="oRadio" value="other">
    """
    How to identify if the radio button is selected?
    ans) Use is_selected() method
    
    How to select a radio button
    ans) use click() method 
    
    """
    def testRadios(self):
        maleradiobuttonobj = self.driver.find_element_by_id("mRadio")
        femaleradiobuttonobj = self.driver.find_element_by_id("fRadio")
        otherradiobuttonobj = self.driver.find_element_by_id("oRadio")

        # validate enable and displayed
        self.assertTrue(maleradiobuttonobj.is_enabled())
        self.assertTrue(maleradiobuttonobj.is_displayed())

        self.assertTrue(femaleradiobuttonobj.is_enabled())
        self.assertTrue(femaleradiobuttonobj.is_displayed())

        self.assertTrue(otherradiobuttonobj.is_enabled())
        self.assertTrue(otherradiobuttonobj.is_displayed())

        # validate the type
        self.assertEqual("radio", maleradiobuttonobj.get_attribute("type"))
        self.assertEqual("radio", femaleradiobuttonobj.get_attribute("type"))
        self.assertEqual("radio", otherradiobuttonobj.get_attribute("type"))

        #validate the value
        self.assertEqual(maleradiobuttonobj.get_attribute("value"), "male")
        self.assertEqual(femaleradiobuttonobj.get_attribute("value"), "female")
        self.assertEqual(otherradiobuttonobj.get_attribute("value"), "other")

        #validate male radio is selected
        self.assertTrue(maleradiobuttonobj.is_selected())
        self.assertFalse(femaleradiobuttonobj.is_selected())
        self.assertFalse(otherradiobuttonobj.is_selected())

        #select female
        femaleradiobuttonobj.click()
        time.sleep(3)

        #select other
        otherradiobuttonobj.click()
        time.sleep(3)

    #<input type="checkbox" name="proof1" value="passport">
    #<input type="checkbox" name="proof2" value="voter">
    #<input type="checkbox" name="proof3" value="pan" checked="">

    """
        How to identify if the check button is selected?
        ans) Use is_selected() method

        How to select a check Box
        ans) use click() method 
        
        How to unSelect a check Box
        ans) use click() method 

        """
    def testCheckBoxes(self):
        passportObj = self.driver.find_element_by_name("proof1")
        voterObj = self.driver.find_element_by_name("proof2")
        panObj = self.driver.find_element_by_name("proof3")

        # validate enable and displayed
        self.assertTrue(passportObj.is_enabled())
        self.assertTrue(passportObj.is_displayed())

        self.assertTrue(voterObj.is_enabled())
        self.assertTrue(voterObj.is_displayed())

        self.assertTrue(panObj.is_enabled())
        self.assertTrue(panObj.is_displayed())

        # validate the type
        self.assertEqual("checkbox", passportObj.get_attribute("type"))
        self.assertEqual("checkbox", voterObj.get_attribute("type"))
        self.assertEqual("checkbox", panObj.get_attribute("type"))

        # validate the value
        self.assertEqual(passportObj.get_attribute("value"), "passport")
        self.assertEqual(voterObj.get_attribute("value"), "voter")
        self.assertEqual(panObj.get_attribute("value"), "pan")

        # validate pan is selected
        self.assertFalse(passportObj.is_selected())
        self.assertFalse(voterObj.is_selected())
        self.assertTrue(panObj.is_selected())

        #Unselect pan
        panObj.click()
        time.sleep(3)

        #select voter
        voterObj.click()
        time.sleep(3)

        #select the passport
        passportObj.click()
        time.sleep(3)

    """
    <select name="city">
			<option value="hyd">Hyderabad</option>
			<option value="bang" selected="selected">Bangalore</option>
			<option value="chen">Chennai</option>
			<option value="mum">Mumbai</option>
		</select>
    How to get all the options in a dropdown?
    ans)
       citydropdownobj =  self.driver.find_element_by_name("city")
       all_options = citydropdownobj.find_elements_by_tag_name("option")
    
    How to select dropDown value?
        selectObj.select_by_index()
        selectObj.select_by_value()
        selectObj.select_by_visible_text()
        
   How to get the selected value?
   ans)use selectObj.first_selected_option



       
    """
    def testDropdown(self):
        citydropdownobj =  self.driver.find_element_by_name("city")

        #check enabled and displayed

        self.assertTrue(citydropdownobj.is_enabled())
        self.assertTrue(citydropdownobj.is_displayed())

        #test the size
        all_options = citydropdownobj.find_elements_by_tag_name("option")
        self.assertEqual(4, len(all_options))

        #assert the Option text  and assert the Option value
        expectedCities = ["Hyderabad", "Bangalore", "Chennai", "Mumbai"]
        expectedCityValues = ["hyd", "bang", "chen", "mum"]

        for option in all_options:
            self.assertTrue(option.text in expectedCities,"Invalid text")
            v = option.get_attribute("value")
            self.assertTrue(v in expectedCityValues, "Invalid value "+v )

         #create select obj
        selectObj = Select(citydropdownobj)

        #validate default selected value
        firstObj = selectObj.first_selected_option
        self.assertEqual("Bangalore", firstObj.text)

        selectObj.select_by_index(2)
        time.sleep(3)

        selectObj.select_by_value("hyd")
        time.sleep(3)

        selectObj.select_by_visible_text("Mumbai")
        time.sleep(3)

        """
        with order:
         expectedcitytext = ["Hyderabad", "Bangalore", "Chennai", "Mumbai"]
        expectedcityvalues = ["hyd", "bang", "chen", "mum"]
        count = 0
        for option in all_options:
            self.assertEqual(expectedcityvalues[count], option.get_attribute("value"),
                             "invalid city found" + option.get_attribute("value"))
            self.assertEqual(expectedcitytext[count], option.text, "invalid city found" + option.text)
            count = count + 1
            
        """


    """
    <select name="citizen" multiple="">
			<option value="IN">India</option>
			<option value="PAK">Pakistan</option>
			<option value="US">America</option>
			<option value="AUS">Australia</option>
		</select>
		
	How to identify if the dropdown is single/multiple?
	ans)
	1st get select obj
	use "selectObj.is_multiple" method 
	  
	How to get all the options in a dropdown?
    ans)
       citydropdownobj =  self.driver.find_element_by_name("city")
       all_options = citydropdownobj.find_elements_by_tag_name("option")
    
    How to select dropDown value?
        selectObj.select_by_index()
        selectObj.select_by_value()
        selectObj.select_by_visible_text()
        
    How to deselect dropDown value?
        selectObj.deselect_by_index()
        selectObj.deselect_by_value()
        selectObj.deselect_by_visible_text()
        
   How to get the selected value?
   ans)use selectObj.first_selected_option

    Deselect_all( )
    This method enables us to clear all the selected options. It is useful when we have selected multiple items from the drop-down. If we use this method in case of a single selection, it will throw a NotImplementedError exception.
    
   Deselect_by_index( )
    This API clears the selected option using the �index� attribute. It is the inverse of the select_by_index( ) method.
    
   Deselect_by_value( )
    This API  clears the selected option using the value of the option. It is the inverse of the select_by_value( ) method.
    
   Deselect_by_visible_text( )
    This API clears the selected option using the text of the option. It is the inverse of the select_by_visible_text( ) method.


    """
    def testMultiDropdown(self):
        citizenDropdownObj = self.driver.find_element_by_name("citizen")

        # check enabled and displayed

        self.assertTrue(citizenDropdownObj.is_enabled())
        self.assertTrue(citizenDropdownObj.is_displayed())

        # test the size
        all_options = citizenDropdownObj.find_elements_by_tag_name("option")
        self.assertEqual(4, len(all_options))

        # assert the Option text  and assert the Option value
        expectedCities = ["India", "Pakistan", "America", "Australia"]
        expectedCityValues = ["IN", "PAK", "US", "AUS"]

        for option in all_options:
            self.assertTrue(option.text in expectedCities, "Invalid text")
            v = option.get_attribute("value")
            self.assertTrue(v in expectedCityValues, "Invalid value " + v)

        # create select obj
        selectObj = Select(citizenDropdownObj)

        #select dropdown
        selectObj.select_by_index(2)
        time.sleep(3)

        selectObj.select_by_value("AUS")
        time.sleep(3)

        selectObj.select_by_visible_text("India")
        time.sleep(3)


        #deselect
        selectObj.deselect_by_index(2)
        time.sleep(3)

        selectObj.deselect_by_value("AUS")
        time.sleep(3)

        selectObj.deselect_by_visible_text("India")
        time.sleep(3)

        """
         expectedcitzenshiptext = ["India", "Pakistan", "AMERICA", "AUSTRLIA"]
        expectedcitzenshipvalues = ["IN", "PAK", "US", "AUS"]
        count = 0
        for option in all_options:
            self.assertEqual(expectedcitzenshipvalues[count], option.get_attribute("value"),
                             "invalid city found" + option.get_attribute("value"))
            self.assertEqual(expectedcitzenshiptext[count], option.text, "invalid city found" + option.text)
            count = count + 1
        """


    """
      <textarea name="address" rows="5" cols="80"></textarea>
    """
    def testTextArea(self):
        # get web element obj
        textAreaObj = self.driver.find_element_by_name("address")

        # validate web elements obj
        self.assertTrue(textAreaObj.is_enabled())
        self.assertTrue(textAreaObj.is_displayed())

        # validate the type
        rows = textAreaObj.get_attribute("rows")
        cols = textAreaObj.get_attribute("cols")
        self.assertEqual("5", rows)
        self.assertEqual("80", cols)

        textAreaObj.send_keys("19-12,marathahalli, \n Bangalore, \n Karnataka560037")

        time.sleep(3)


    """
        <input type="file" name="fileupload" accept="image/*">
    """
    def testFileUpload(self):
        # get web element obj
        fileUploadObj = self.driver.find_element_by_name("fileupload")

        # validate web elements obj
        self.assertTrue(fileUploadObj.is_enabled())
        self.assertTrue(fileUploadObj.is_displayed())

        # validate the type
        type = fileUploadObj.get_attribute("type")
        accept = fileUploadObj.get_attribute("accept")
        self.assertEqual("file", type)
        self.assertEqual("image/*", accept)

        fileUploadObj.send_keys("C://test//test.png")

        time.sleep(3)























