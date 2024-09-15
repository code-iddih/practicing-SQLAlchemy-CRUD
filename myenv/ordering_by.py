from main import User , session , engine
from sqlalchemy import desc

local_session = session(bind = engine)

# Ascending order

# users_asc = local_session.query(User).order_by(User.username).all()

# for user in users_asc:
#     print(f"User {user.username}")

# Descending order

users_desc = local_session.query(User).order_by(desc(User.username)).all()

for user in users_desc:
    print(f"User {user.username}")