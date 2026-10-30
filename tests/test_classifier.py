import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from classifier import ArabicIntentClassifier

class TestClassifier(unittest.TestCase):
    def setUp(self):
        lex = Path(__file__).resolve().parent.parent / "data" / "intent_lexicon_ar.json"
        self.clf = ArabicIntentClassifier(str(lex))
    def test_trans(self):
        self.assertEqual(self.clf.classify_query("سعر ايفون 16 في جرير مع تقسيط تابي")[0], "Transactional")
    def test_comm(self):
        self.assertEqual(self.clf.classify_query("افضل غسالة صحون ميديا او ال جي عيوب ومميزات")[0], "Commercial Investigation")
    def test_nav(self):
        self.assertEqual(self.clf.classify_query("تسجيل دخول منصة سلة")[0], "Navigational")
    def test_info(self):
        self.assertEqual(self.clf.classify_query("كيف اغير زيت السيارة في البيت")[0], "Informational")

if __name__ == "__main__":
    unittest.main()
