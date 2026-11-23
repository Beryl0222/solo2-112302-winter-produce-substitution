import unittest

from materials import load_corpus


class MaterialsTest(unittest.TestCase):
    def test_records_preserve_source_text_and_sequence(self):
        records = load_corpus()["records"]
        keys = [record["id"] for record in records]
        self.assertTrue(keys)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual([r["arrival_order"] for r in records], list(range(1, len(records) + 1)))
        self.assertTrue(all(r["text"].strip() and r["kind"].strip() for r in records))

    def test_explicit_cross_references_resolve(self):
        records = load_corpus()["records"]
        positions = {record["id"]: record["arrival_order"] for record in records}
        refs = [(r["id"], ref) for r in records for ref in r["references"]]
        self.assertTrue(refs)
        for source, target in refs:
            with self.subTest(source=source, target=target):
                self.assertIn(target, positions)
                self.assertLess(positions[target], positions[source])
