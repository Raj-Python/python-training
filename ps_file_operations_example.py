
def get_user_list(data_file, target_file):
    """
    get_user_list to get list of user's name from the passwd file
    :param data_file: string
    :return: None
    """

    try:
        users=[]
        with open(data_file) as fp:
            for line in fp:
                username = line.split(':')[0].upper()
                users.append(username)
                

            users.sort()
            with open(target_file, 'w') as fw:
                for index, value in enumerate(users,1):
                    content =  "{:>6}  {}".format(index, value)
                    print content
                    fw.write(content + '\n')

    except IOError as err:
        print err


get_user_list('resources/passwd.txt','resources/target_passwd.dat')


