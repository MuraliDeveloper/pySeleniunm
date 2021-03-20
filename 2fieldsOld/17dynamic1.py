"""
dynamic elements:
-----------------------
best locator to use is xpath or css

ex1:
<input type="button" id="btnCheckStatus18181821" value="Check Status" >
XPath - //input[starts-with(@id, ‘btnCheckStatus’)]

ex2:
<input type="submit" id=" 1002-VALIDATE-655" >
XPath - //input[contains(@id, ‘VALIDATE’)]

ex3:
<input type="submit" id="save87876" class="publish">
<input type="submit" id="cancel1313" class="publish">
<input type="submit" id="save1313" class="cancel">
Xpath- //button[starts-with(@id, 'save') and contains(@class,'publish')]




"""