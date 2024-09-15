from main import User , session , engine

local_session = session(bind = engine)

user_to_delete = local_session.query(User).filter(User.username == "jerry").first()

local_session.delete(user_to_delete)

local_session.commit()