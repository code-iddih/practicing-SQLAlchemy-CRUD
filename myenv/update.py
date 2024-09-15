from main import User , session , engine

local_session = session(bind = engine)

user_to_update = local_session.query(User).filter(User.username == 'john').first()

user_to_update.username = "james"

user_to_update.email = "james@company.com"

local_session.commit()