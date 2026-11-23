"""读取和列出项目的练习语料。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_corpus():
    """读取原样保存的语料条目。"""
    return json.loads((ROOT / "data" / "corpus.json").read_text(encoding="utf-8"))
