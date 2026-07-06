# 🪶 SagaSmith CoC Skills — Standalone

**零依赖轻量版。** 无需安装 `sagasmith-coc` Python 包，Python 标准库即可运行。

所有命令在 `standalone/` 目录下执行：

```powershell
python portable.py doctor
python portable.py campaign start --name "Arkham"
python portable.py roll d100 --score 65
```

数据存 `~/.sagasmith/`。不支持 PDF 导入、FTS5 检索、ChromaDB。

详见 `SKILL.md`。
