"""Password hashing utilities using bcrypt."""

from __future__ import annotations

import bcrypt


def hash_password(plain: str) -> str:
    """Hash a plaintext password using bcrypt.

    Args:
        plain: The plaintext password to hash.

    Returns:
        The bcrypt hash as a string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plaintext password against a bcrypt hash.

    Args:
        plain: The plaintext password to verify.
        hashed: The bcrypt hash to check against.

    Returns:
        True if the password matches, False otherwise.
    """
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
    except (ValueError, TypeError):
        return False
