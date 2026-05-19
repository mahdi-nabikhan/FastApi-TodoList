from core.database import SessionLocal

from sqlalchemy.orm import session
from users.models import *
from tasks.models import *
from faker import Faker

fake = Faker()

def seed_user(db):
    user= UserModel(username=fake.user_name())
    user.set_password('12345678')
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f'username : {user.username}')
    return user
    


def seed_tasks(db,user,count=10):
    task_list = []
    for _ in range(count):
        
        task_list.append(TaskModel(
                user_id=user.id,
                title=fake.sentence(nb_words=6),
                description=fake.text(),
                is_complated=fake.boolean()
                ))
    db.add_all(task_list)
    db.commit()

def main():
    db = SessionLocal()
    try:
        user = seed_user(db,)
        tasks = seed_tasks(db,user)
        
    finally:
        db.close()

if __name__  == '__main__':
    main()