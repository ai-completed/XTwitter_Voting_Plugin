def authenticate_user(username, password):
    user_database = {
        'user1': {'password': 'password123', 'authenticated': True},
        'user2': {'password': 'pass456', 'authenticated': False}
    }
    user = user_database.get(username, None)
    if user and user['password'] == password:
        return user['authenticated']
    else:
        return False