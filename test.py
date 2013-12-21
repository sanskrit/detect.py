# -*- coding: utf-8 -*-
"""
    test
    ~~~~

    Tests for detect.py

    :license: MIT and BSD
"""

import pytest

from detect import detect, Scheme as S


def add(testcases, scheme, items):
    testcases.extend([(x, scheme) for x in items])


BASIC = []
add(BASIC, S.BENGALI, ['অ', '৺'])
add(BASIC, S.DEVANAGARI, ['ऄ', 'ॿ'])
add(BASIC, S.GUJARATI, ['અ', '૱'])
add(BASIC, S.GURMUKHI, ['ਅ', 'ੴ'])
add(BASIC, S.KANNADA, ['ಅ', '೯'])
add(BASIC, S.MALAYALAM, ['അ', 'ൿ'])
add(BASIC, S.ORIYA, ['ଅ', 'ୱ'])
add(BASIC, S.TAMIL, ['அ', '௺'])
add(BASIC, S.TELUGU, ['అ', '౿'])
add(BASIC, S.HK, [
    'a',
    'b',
    'c'
])
add(BASIC, S.IAST, [
    'rāga',
    'nadī',
    'vadhū',
    'kṛta',
    'pitṝn',
    'kḷpta',
    'ḹ',
    'tejasvī',
    'gomayaḥ'
    'haṃsa',
    'naraḥ',
    'aṅga',
    'añjana',
    'kuṭumba',
    'ḍamaru',
    'aruṇa',
    'śveta',
    'ṣaṣ',
])
add(BASIC, S.KOLKATA, [
    'tējas',
    'sōma',
])
add(BASIC, S.SLP1, [
    'BrAtf',
    'pitFn',
    'kxpta',
    'XkAra',
    'kEvalya',
    'kOsalya',
    'aYjana',
    'kuwumba',
    'kaWora'
    'qamaru',
    'soQA',
])


@pytest.mark.parametrize('data', BASIC)
def test_basic(data):
    text, scheme = data
    text = text.decode('utf-8')
    assert detect(text) == scheme


@pytest.mark.parametrize('data', BASIC)
def test_noisy(data):
    noise = ' \t\n 1234567890 !@#$%^&*(),.<>\'\"-_[]{}\\|;:`~ ΣД あア'
    text, scheme = data
    text = ''.join([noise, text, noise]).decode('utf-8')
    assert detect(text) == scheme
