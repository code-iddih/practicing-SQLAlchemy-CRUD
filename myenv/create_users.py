from main import User , session , engine

# A list of users
users = [
    {
        "username" : "jerry",
        "email" : "jerry@gmail.com"
        
    },
        {
        "username" : "jordan",
        "email" : "jordan@gmail.com"
        
    },
        {
        "username" : "jackson",
        "email" : "jackson@gmail.com"
        
    },
        {
        "username" : "jarden",
        "email" : "j@gmail.com"
        
    },
        {
        "username" : "john",
        "email" : "john@gmail.com"
        
    },
        {
        "username" : "jack",
        "email" : "jack@gmail.com"
        
    }
]

# how to interact with the database (transaction / operations)
local_session = session(bind = engine)

# new_user = User(username = "Eric" , email = "ericn_nyamwaya@gmail.com")

# # How to add the new user
# local_session.add(new_user)

# # How to commit user to the database
# local_session.commit()

for u in users:
    new_user = User(username = u["username"], email = u["email"])
    print(new_user)

    local_session.add(new_user)

    local_session.commit()

    print(f"Added {u['username']}")

