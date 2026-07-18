from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from . import jwt_handler,schemas

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return jwt_handler.verify_token(
        token,
        credentials_exception
    )

def get_current_admin(current_user=Depends(get_current_user)):

    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can perform this action."
        )

    return current_user


def get_admin_or_player(
    current_user: schemas.TokenData = Depends(get_current_user)
):
    allowed_roles = ["ADMIN", "PLAYER"]

    if current_user.role not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )

    return current_user