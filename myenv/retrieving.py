from main import User , session , engine

local_session = session(bind = engine)

# Returning all objects
# users = local_session.query(User).all()

# Returning all objects but with limits
# users = local_session.query(User).all()[:3]



# for user in users:
#     print(user.username)

# Returning one object
john = local_session.query(User).filter(User.username == "john").first()
print(john)
