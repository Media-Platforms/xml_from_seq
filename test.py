import unittest
from xml_from_seq import INLINE, XML, XMLdecl, end_tag, start_tag


class XMLTests(unittest.TestCase):

    def test_XML(self):
        s = ['a', {'b': 123, 'c': None}, [None, ['d', INLINE, 'e']]]
        assert XML(s) == '<a b="123">\n\t<d>e</d>\n</a>\n'

    def test_start_tag(self):
        assert start_tag('foo', {'bar': 123}) == '<foo bar="123">'

    def test_end_tag(self):
        assert end_tag('foo') == '</foo>'

    def test_XMLdecl(self):
        x = XMLdecl(xmlns='http://example.com/foo.xml')
        assert x == '<?xml xmlns="http://example.com/foo.xml" version="1.0"?>\n'


if __name__ == '__main__':
    unittest.main()