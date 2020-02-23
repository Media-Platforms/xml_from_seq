# xml_from_seq

Generate XML from a Python data structure.

## Examples

The `XML()` function renders a Python list or tuple to an XML element. The first item is the
element name, the second item – if it's a dict – is the attributes, and the rest of the items
are either text or nested elements.
```py
from xml_from_seq import XML

item = ['item', {'attr1': 123, 'attr2': 'other value'}, 'This is the content of the item.']
assert XML(item) == '<item attr1="123" attr2="other value">This is the content of the item.</item>'

item = [
    'item',
    'This is some content of the item.'
    ['sub', 'This is the content of a subelement.']
]
print(XML(item))
```
```xml
 <item>
    This is some content of the item.
    <sub>
        This is the content of a subelement.
    </sub>
</item>
```

If a element's name is `None` its contents will appear in its place. If an attribute's value is
`None` it will be omitted.

If an element's name is a list or tuple, it will be inserted into the XML as-is – so you can inclue
already-rendered XML by double-bracketing it:
```py
print(XML([['<foo>123</foo>']]))
```
```xml
<foo>123</foo>
```

### Indentation and line breaks

If the first item in an element (not counting an attribute dict) is `xml_from_seq.INLINE`, that
element's contents won't be indented on separate lines from the element's start and end tags.
```py
from xml_from_seq import INLINE, XML

item = [
    'item',
    'This is some content of the item.'
    ['sub', INLINE, 'This is the content of a subelement.']
]
print(XML(item))
```
```xml
 <item>
    This is some content of the item.
    <sub>This is the content of a subelement.</sub>
</item>
```

You can pass an integer `indent` parameter to the `XML()` function to indent the output XML by
that many tabs.
