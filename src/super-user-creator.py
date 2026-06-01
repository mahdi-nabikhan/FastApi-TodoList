# scripts/create_superuser.py

from sqlalchemy.orm import Session

from core.database import SessionLocal
from users.models import *
from tasks.models import TaskModel


def create_superuser():
    db: Session = SessionLocal()

    try:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        # check if user exists
        user = db.query(UserModel).filter_by(username=username).first()

        if user:
            print("❌ User already exists")
            return

        # create superuser
        superuser = UserModel(
            username=username,
            is_superuser=True
        )

        superuser.set_password(password)

        db.add(superuser)
        db.commit()
        db.refresh(superuser)

        print("✅ Superuser created successfully")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    create_superuser()