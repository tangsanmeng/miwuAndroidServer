import leancloud


def test_connect():

    leancloud.init("ILpxKphAjAghfoPeZkNVtN0w-gzGzoHsz", "jI1kxeh2mhYrSfzZHapy5Y3w")
    TestObject = leancloud.Object.extend('TestObject')
    test_object = TestObject()
    test_object.set('words', "Hello world!")
    test_object.save()