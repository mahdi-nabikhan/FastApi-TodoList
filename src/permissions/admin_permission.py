from users.models import UserModel
from core.auth.jwt_auth import get_authenticated_user
from fastapi import Depends
from fastapi import status
from fastapi.exceptions import HTTPException

def get_superuser(
    current_user: UserModel = Depends(get_authenticated_user),
):
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user