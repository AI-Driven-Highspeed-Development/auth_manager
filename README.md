# Auth Manager

Lightweight password hashing and verification using bcrypt.

## Overview

- Pure authentication logic - no database knowledge
- Uses bcrypt for secure password hashing
- Stateless helper class for easy integration
- Works with any user storage backend

## Features

- Secure bcrypt password hashing
- Password verification
- Standalone utility functions available
- Type hints throughout

## Quickstart

```python
from managers.auth_manager import AuthManager

auth = AuthManager()

# Hash a password for storage
hashed = auth.hash_password("my_secret_password")

# Verify during login
if auth.verify_password("user_input", hashed):
    print("Login successful!")
```

## API

```python
class AuthManager:
    def hash_password(self, plain: str) -> str: ...
    def verify_password(self, plain: str, hashed: str) -> bool: ...

# Standalone functions also available
def hash_password(plain: str) -> str: ...
def verify_password(plain: str, hashed: str) -> bool: ...
```

## Requirements

- `bcrypt>=4.0.0`

## Module Structure

```
managers/auth_manager/
├── __init__.py          # Module exports
├── init.yaml            # Module metadata
├── auth_manager.py      # AuthManager class
├── password_utils.py    # Standalone hash functions
├── requirements.txt     # bcrypt dependency
└── README.md            # This file
```

## See Also

- Session Manager - For token-based session management
- Secret Manager - For storing API keys securely
