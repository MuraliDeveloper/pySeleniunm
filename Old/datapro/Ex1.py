

class Testing(unittest.TestCase):

    def setUp(self):
        self.driver = None

    def tearDown(self):
        print("driver close")

    def testEx1(self):
        print("helo")




