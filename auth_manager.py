"""Authentication manager for password handling."""

from __future__ import annotations

from managers.auth_manager.password_utils import hash_password, verify_password


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

    def hash_password(self, plain: str) -> str:
        """Hash a plaintext password for secure storage.

        Args:
            plain: The plaintext password.

        Returns:
            The bcrypt hash as a string.

        Example:
            auth = AuthManager()
            hashed = auth.hash_password("my_secret_password")
            # Store `hashed` in your database
        """
        return hash_password(plain)

    def verify_password(self, plain: str, hashed: str) -> bool:
        """Verify a plaintext password against a stored hash.

        Args:
            plain: The plaintext password to verify.
            hashed: The bcrypt hash from storage.

        Returns:
            True if password matches, False otherwise.

        Example:
            auth = AuthManager()
            if auth.verify_password(user_input, stored_hash):
                print("Login successful!")
        """
        return verify_password(plain, hashed)
