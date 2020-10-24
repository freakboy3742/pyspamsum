import unittest

import spamsum


class SpamSumTest(unittest.TestCase):
    def setUp(self):
        self.s1 = "I am the very model of a modern Major-General, I've information animal and vegetable and mineral"
        self.s2 = "I am the very model of a modern Brigadier, I've information animal and vegetable and something else"
        self.s3 = "Huh? Gilbert and Who?"

    def test_edit_distance(self):
        self.assertEqual(spamsum.edit_distance(self.s1, self.s2), 27)
        self.assertEqual(spamsum.edit_distance(self.s2, self.s1), 27)
        self.assertEqual(spamsum.edit_distance(self.s1, self.s3), 93)
        self.assertEqual(spamsum.edit_distance(self.s2, self.s3), 96)

    def test_spamsum(self):
        self.assertEqual(
            spamsum.spamsum(self.s1),
            '3:kEvyc/sFIKwYclQY4MKLFE4Igu0uLzIKygn:kE6Ai3KQ/MKOgDKZn'
        )
        self.assertEqual(
            spamsum.spamsum(self.s2),
            '3:kEvyc/sFIKwpErXLsCTApY4MKLFE4Igu0uLzWKIAYjtn:kE6Ai3jjTU/MKOgdK9Yjt'
        )
        self.assertEqual(
            spamsum.spamsum(self.s3),
            '3:uZ3B:uZx'
        )

    def test_match(self):
        self.assertEqual(
            spamsum.match(spamsum.spamsum(self.s1), spamsum.spamsum(self.s1)),
            100
        )
        self.assertEqual(
            spamsum.match(spamsum.spamsum(self.s1), spamsum.spamsum(self.s2)),
            72
        )
        self.assertEqual(
            spamsum.match(spamsum.spamsum(self.s2), spamsum.spamsum(self.s1)),
            72
        )
        self.assertEqual(
            spamsum.match(spamsum.spamsum(self.s1), spamsum.spamsum(self.s3)),
            0
        )
        self.assertEqual(
            spamsum.match(spamsum.spamsum(self.s2), spamsum.spamsum(self.s3)),
            0
        )
