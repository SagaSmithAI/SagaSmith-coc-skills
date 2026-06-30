"""BGE embedding profiles and configuration for CoC7 rules."""

from __future__ import annotations

import os
from dataclasses import dataclass

ENGINE_SOURCE_ID = "coc7-keeper-skill"

DEFAULT_BGE_M3_MODEL = "BAAI/bge-m3"
DEFAULT_BGE_SMALL_EN_MODEL = "BAAI/bge-small-en-v1.5"
DEFAULT_EMBEDDING_DIMENSIONS = 1024


@dataclass(frozen=True)
class EmbeddingProfile:
    key: str
    model_name: str
    dimensions: int
    language: str

    @property
    def model_id(self) -> str:
        return f"embedding-{self.key.replace('_', '-')}"


BGE_M3_PROFILE = EmbeddingProfile("bge_m3", DEFAULT_BGE_M3_MODEL, 1024, "multi")
BGE_SMALL_EN_PROFILE = EmbeddingProfile(
    "bge_small_en_v1_5", DEFAULT_BGE_SMALL_EN_MODEL, 384, "en"
)
EMBEDDING_PROFILES = {
    profile.key: profile
    for profile in (BGE_M3_PROFILE, BGE_SMALL_EN_PROFILE)
}
_PROFILES_BY_MODEL = {profile.model_name: profile for profile in EMBEDDING_PROFILES.values()}
_PROFILE_ALIASES = {
    "m3": BGE_M3_PROFILE.key,
    "bge-m3": BGE_M3_PROFILE.key,
    "en": BGE_SMALL_EN_PROFILE.key,
    "small-en": BGE_SMALL_EN_PROFILE.key,
}


def configured_profiles() -> tuple[EmbeddingProfile, ...]:
    """Return explicitly enabled model choices; default preserves BGE-M3."""
    raw = os.environ.get("COC7_EMBEDDING_PROFILES", BGE_M3_PROFILE.key)
    keys = []
    for item in raw.split(","):
        value = item.strip().lower()
        if not value:
            continue
        key = _PROFILE_ALIASES.get(value, value)
        if key not in EMBEDDING_PROFILES:
            choices = ", ".join(EMBEDDING_PROFILES)
            raise ValueError(
                f"unknown COC7_EMBEDDING_PROFILES entry {item!r}; choose from {choices}"
            )
        if key not in keys:
            keys.append(key)
    if not keys:
        raise ValueError("COC7_EMBEDDING_PROFILES must enable at least one model")
    return tuple(EMBEDDING_PROFILES[key] for key in keys)


def resolve_profile(name: str) -> EmbeddingProfile:
    """Return a single EmbeddingProfile by name or model string."""
    key = _PROFILE_ALIASES.get(name.strip().lower(), name.strip().lower())
    if key in EMBEDDING_PROFILES:
        return EMBEDDING_PROFILES[key]
    raise ValueError(
        f"unknown profile {name!r}; choose from {', '.join(EMBEDDING_PROFILES)}"
    )


def collection_name(base_name: str, profile: EmbeddingProfile) -> str:
    return f"{base_name}__{profile.key}"
