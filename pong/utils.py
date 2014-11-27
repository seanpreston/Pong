# -*- coding: utf-8 -*-
import re
import unicodedata

from django.utils.encoding import smart_unicode
from short_url import UrlEncoder

SHORT_URL_ALPHABET = '3Mnt7goVNwpHvxqT06zUDuJFZeWs5b9jS8QKlaiBR4mAd2IykPGErYC1fXhLcO'
# Extra characters outside of alphanumerics that we'll allow.
SLUG_OK = '-_~.'


def slugify(s, ok=SLUG_OK, lower=True, spaces=False):
    # L and N signify letter/number.
    # http://www.unicode.org/reports/tr44/tr44-4.html#GC_Values_Table
    rv = []
    for c in unicodedata.normalize('NFKC', smart_unicode(s)):
        cat = unicodedata.category(c)[0]
        if cat in 'LN' or c in ok:
            rv.append(c)
        if cat == 'Z':  # space
            rv.append(' ')
    new = ''.join(rv).strip()
    if not spaces:
        new = re.sub('[-\s]+', '-', new)
    slug = new.lower() if lower else new
    if slug == '':
        slug = '-'
    elif slug[0] == '.':
        slug = '-' + slug

    return slug


def encode_uri(numeric_id):
    encoder = UrlEncoder(alphabet=SHORT_URL_ALPHABET)
    return encoder.encode_url(numeric_id)
