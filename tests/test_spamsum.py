import pytest

import spamsum

GILBERT = (
    "I am the very model of a modern Major-General, "
    "I've information animal and vegetable and mineral"
)
NOT_GILBERT = (
    "I am the very model of a modern Brigadier, "
    "I've information animal and vegetable and something else"
)
IGNORANCE = "Huh? Gilbert and Who?"


@pytest.mark.parametrize(
    "s1, s2, distance",
    [
        (GILBERT, NOT_GILBERT, 27),
        (NOT_GILBERT, GILBERT, 27),
        (GILBERT, IGNORANCE, 93),
        (NOT_GILBERT, IGNORANCE, 96),
    ],
)
def test_edit_distance(s1, s2, distance):
    assert spamsum.edit_distance(s1, s2) == distance


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            GILBERT,
            "3:kEvyc/sFIKwYclQY4MKLFE4Igu0uLzIKygn:kE6Ai3KQ/MKOgDKZn",
        ),
        (
            NOT_GILBERT,
            "3:kEvyc/sFIKwpErXLsCTApY4MKLFE4Igu0uLzWKIAYjtn:kE6Ai3jjTU/MKOgdK9Yjt",
        ),
        (
            IGNORANCE,
            "3:uZ3B:uZx",
        ),
    ],
)
def test_spamsum(value, expected):
    assert spamsum.spamsum(value) == expected


@pytest.mark.parametrize(
    "s1, s2, match",
    [
        (GILBERT, GILBERT, 100),
        (GILBERT, NOT_GILBERT, 72),
        (NOT_GILBERT, GILBERT, 72),
        (GILBERT, IGNORANCE, 0),
        (NOT_GILBERT, IGNORANCE, 0),
    ],
)
def test_match(s1, s2, match):
    assert spamsum.match(spamsum.spamsum(s1), spamsum.spamsum(s2)) == match
