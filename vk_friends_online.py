import vk_requests


APP_ID = 5673982


def get_user_login():
    return input('Login ')


def get_user_password():
    return input('Password ')


def get_online_friends(login, password):
    api = vk_requests.create_api(
        app_id=APP_ID,
        login=login,
        password=password,
        scope=['friends'])
    id_friends_online = api.friends.getOnline()
    name_friends_online = api.users.get(user_ids=id_friends_online)
    return name_friends_online


def output_friends_to_console(friends_online):
    for friend_online in friends_online:
        first_name = friend_online.get('first_name')
        last_name = friend_online.get('last_name')
        print('{} {}'.format(first_name, last_name))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
