#!/usr/bin/env python
import unittest
import app
import xmlrunner


class BasicTest(unittest.TestCase):

    # Executed prior to each test
    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_health(self):
        result = self.app.get('/health')
        print result
        self.assertEqual(result.status, '200 OK')


if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
