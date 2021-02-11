import time
import unittest

from pom import commons
from pom.commonpage import commonpage


class changepasswordpage(commonpage,unittest.TestCase):

    def open(self):

        self.passobj=self.findbyid("changePwd").click()
    def intializeelement(self):

        self.correctobj=self.findbyname("currPass")
        self.newobj=self.findbyname("newPass")
        self.confirmobj=self.findbyname("confirmPass")
        self.submitobj=self.findbyname("Change Password")

    def changepassword(self,correct,new,confirm ):
        self.open()

        self.intializeelement()

        self.correctobj.send_keys(correct)
        self.newobj.send_keys(new)
        self.confirmobj.send_keys(confirm)
        self.submitobj.click()
        time.sleep(5)

