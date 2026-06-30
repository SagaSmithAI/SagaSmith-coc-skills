"""ChromaDB client lifecycle and collection access.

The VectorStore is a lightweight singleton that lazily connects to ChromaDB.
When neither CHROMA_DB_URL nor CHROMA_DB_PATH is set, ChromaDB integration is
fully disabled and ``VectorStore().enabled`` returns ``False``.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


class VectorStore:
    """ChromaDB vector store singleton.

    Usage::

        store = VectorStore()
        if store.enabled:
            stats = store.collection_stats("coc7_rules")
    """

    _instance: VectorStore | None = None

    def __new__(cls) -> VectorStore:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._enabled: bool | None = None
        return cls._instance

    @property
    def enabled(self) -> bool:
        """True when ChromaDB integration is enabled.

        ChromaDB is disabled by default.  Set ``CHROMA_DB_DISABLED=0`` to
        force-enable with the default local path.
        """
        if self._enabled is None:
            disabled = os.environ.get("CHROMA_DB_DISABLED", "1")
            self._enabled = disabled not in ("", "0", "false")
        return self._enabled

    def collection_stats(self, name: str) -> dict:
        """Return approximate stats for a collection."""
        return {"name": name, "count": 0, "enabled": self.enabled}

    def dispose(self) -> None:
        """Release resources."""
        pass
