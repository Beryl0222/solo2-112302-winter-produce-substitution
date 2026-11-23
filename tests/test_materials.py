import unittest

from materials import load_corpus

class MaterialsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_corpus()

    def test_project_has_materials(self):
        self.assertEqual(self.data["project"], "分布式演出讲解稿的游客请求与剧目口径")
        self.assertEqual(self.data["material_nature"], "本地合成演练资料")

    def test_record_identifiers_are_unique(self):
        identifiers = [record["id"] for record in self.data["records"]]
        self.assertEqual(len(identifiers), len(set(identifiers)))

    def test_records_retain_their_raw_context(self):
        self.assertTrue(all(record["kind"] and record["text"] for record in self.data["records"]))
        self.assertTrue(any(len(record["text"]) > 12 for record in self.data["records"]))

if __name__ == "__main__":
    unittest.main()
