# 调查员创建

1. 确认 Classic 或 Pulp 规则。
2. 生成 STR、CON、SIZ、DEX、APP、INT、POW、EDU。
3. 计算 HP、MP、SAN、Luck、MOV、DB 和 Build。
4. 选择职业并分配技能。
5. 展示完整草稿，等待玩家确认。
6. 确认后写入 Runtime。

```powershell
sagasmith-coc investigator create --campaign <id> --name "<name>" --player "<player>" --sheet '<json>' --json
```

不得在玩家确认前持久化草稿。
