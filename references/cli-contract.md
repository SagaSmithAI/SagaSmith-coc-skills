# SagaSmith CoC CLI Contract

- Executable: `sagasmith-coc`
- Agent calls always include `--json`.
- stdout contains exactly one JSON document.
- stderr is reserved for logs.

```json
{"ok":true,"data":{},"error":null,"meta":{"command":"group.action","version":"0.2.0"}}
```

Errors use `ok:false` and a stable `error.code`. Exit codes are 0 success, 2 input,
3 not found, 4 conflict, 5 configuration, 6 dependency, and 10 internal error.

Keep retrieval bounded with `--limit`; expand only selected chunks.

For `--sheet`, `--payload`, `--state`, `--metadata`, and other JSON objects,
prefer `@<path-to-utf8-json>` in Windows PowerShell. PowerShell 5 may strip
quotes from inline JSON passed to native executables. Inline JSON is acceptable
only when the platform's argument handling has been verified.

JSON stdout escapes non-ASCII characters so it remains valid on GBK Windows
consoles. Decode it as JSON; do not display the escaped wire representation.
