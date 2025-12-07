"""Authentication manager for password handling."""

from __future__ import annotations

import bcrypt

from utils.logger_util import Logger


class AuthManager:
    """Manages password hashing and verification.

    This is a stateless authentication helper that handles password
    operations. It does NOT know about databases or user storage -
    it only provides pure auth logic.

    Use this module when you need to:
    - Hash passwords before storing them
    - Verify passwords during login
    - Integrate with any user storage backend
    """

    def __init__(self) -> None:
        """Initialize AuthManager."""
        self.logger = Logger(name=__class__.__name__)

    def hash_password(self, plain: str) -> str:
        """Hash a plaintext password for secure storage.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain.encode("utf-8"), salt)
        return hashed.decode("utf-8")

    def verify_password(self, plain: str, hashed: str) -> bool:
        """Verify a plaintext password against a stored hash.

        Args:
            plain: The plaintext password to verify.
            hashed: The bcrypt hash from storage.
        """
        try:
            return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
        except (ValueError, TypeError):
            return False