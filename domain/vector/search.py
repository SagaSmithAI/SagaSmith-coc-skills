"""Shared ChromaDB dense-vector search helper.

This module provides a single function used by both ``RuleSearchService``
and ``ModuleSearchService`` when ChromaDB is enabled.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def chroma_dense_search(
    collection_name: str,
    query_vector: list[float],
    where: dict[str, Any] | None = None,
    *,
    limit: int = 50,
) -> list[tuple[str, float]]:
    """Search a ChromaDB collection and return ``(chunk_id, similarity)`` pairs.

    Args:
        collection_name: A ChromaDB collection name (e.g. ``"coc7_rules"``).
        query_vector: Normalized embedding vector.
        where: Optional ChromaDB metadata filter dict.
        limit: Maximum number of results.

    Returns:
        List of ``(chunk_id, similarity_score)`` ordered by descending
        similarity.  Stub implementation returns an empty list when ChromaDB
        is unavailable.
    """
    store = _get_store()
    if not store.enabled:
        logger.warning("ChromaDB is not configured; dense search is unavailable")
        return []
    # Stub implementation
    return []


def _get_store():
    """Avoid circular import at module level."""
    from .client import VectorStore

    return VectorStore()
