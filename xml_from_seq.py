from collections.abc import Sequence
from functools import partial
from xml.sax.saxutils import escape, quoteattr


INLINE = object()


def XML(*seq, indent=0, cr=True):
    e = partial(element_or_text, i=indent, cr=cr)
    return ''.join(filter(None, map(e, seq)))


def element_or_text(x, i=0, cr=True):
    t = '\n' if cr else ''
    if is_seq(x):
        return element(*x, i=i) + t
    else:
        return ('\t' * i) + escape(str(x)) + t


def element(tag_name, *content, i=0):
    if is_seq(tag_name):
        return tag_name[0]

    if content and isinstance(content[0], dict):
        attrs, *content = content
    else:
        attrs = None

    inline = False
    if content and content[0] == INLINE:
        _, *content = content
        inline = True

    if not tag_name:
        return XML(*content, indent=i, cr=False)

    parts = ['\t' * i, '<', tag_name, attributes(attrs)]
    if inline:
        parts.extend(('>', XML(*content, indent=0, cr=False), f'</{tag_name}>'))
    elif content:
        parts.extend(('>\n', XML(*content, indent=i+1), '\t' * i, f'</{tag_name}>'))
    else:
        parts.append('/>')

    return ''.join(parts)


def start_tag(tag_name, attrs=None):
    parts = '<', tag_name, attributes(attrs), '>'
    return ''.join(filter(None, parts))


def end_tag(tag_name):
    parts = '</', tag_name, '>'
    return ''.join(parts)


def attributes(attrs):
    if not attrs:
        return ''

    html = ['']
    for name, value in attrs.items():
        if value is not None:
            html.append(name + '=' + quoteattr(str(value)))

    return ' '.join(html)


def is_seq(x):
    return isinstance(x, Sequence) and not isinstance(x, str)


def XMLdecl(**attrs):
    if not attrs.get('version'):
        attrs['version'] = '1.0'
    parts = '<?xml', attributes(attrs), '?>\n'
    return ''.join(parts)
