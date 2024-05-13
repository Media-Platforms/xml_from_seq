import unittest
from xml_from_seq import CDATA, INLINE, XML, XMLdecl, end_tag, start_tag


class XMLTests(unittest.TestCase):

    def test_XML(self):
        s = ['a', {'b': 123, 'c': None}, 1 == 2 and 'omit this', [None, ['d', INLINE, 'e']]]
        assert XML(s) == '<a b="123">\n\t<d>e</d>\n</a>\n'

    def test_CDATA(self):
        s = ['a', [CDATA, '<p>this is a paragraph of unescaped HTML</p>']]
        assert XML(s) == '<a>\n\t<![CDATA[<p>this is a paragraph of unescaped HTML</p>]]>\n</a>\n'

    def test_start_tag(self):
        assert start_tag('foo', {'bar': 123}) == '<foo bar="123">'

    def test_end_tag(self):
        assert end_tag('foo') == '</foo>'

    def test_XMLdecl(self):
        x = XMLdecl(xmlns='http://example.com/foo.xml')
        assert x == '<?xml version="1.0" xmlns="http://example.com/foo.xml"?>\n'


if __name__ == '__main__':
    unittest.main()
