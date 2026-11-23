# 冬季菜篮子短报中的替代商品与到店告知

合成资料放在 `data/corpus.json`，记录类型载于 `data/context.json`。每条记录有独立的 `id`、业务类别 `kind` 及原始文字 `text`。`arrival_order` 表示收件先后，文字内注明的业务发生时间可以早于或晚于收件顺序。`references` 只列来源中已明示的记录关联，空值表示未附明示关联。

使用 Python 3.11 标准库，`materials.load_corpus()` 可读取 UTF-8 原始资料。在项目根目录运行资料校验。

    python3 -m unittest discover -s tests -v
