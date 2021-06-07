from seleniumEx.myBasetest import BaseTest
import time
"""
how to validate the title for a page?
validate: compare the expected value and actual value
          if expected is not matching with actual then test case should fail
ex:
self.assertEqual()
self.assertNotEqual()
self.assertFalse()
self.assertTrue()
self.assertGreater()
self.assertGreaterEqual()
self.assertLess()
self.assertLessEqual()
"""
class gTest(BaseTest):

  def test1(self):
      self.driver.get("http://www.google.com")
      pageTitle =self.driver.title

      self.assertEqual("Google" ,pageTitle , "Invalid Title")
      time.sleep(3)
