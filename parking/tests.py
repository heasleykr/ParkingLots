from django.test import TestCase

# Create your tests here.



'''
Clearable File Input Test()
    assert 'accept="image/jpeg"' in widget.render(name='file', value='test.jpg')
        assert {"Content-Type": 'image/jpeg'} in widget.get_conditions('image/jpeg')

'''