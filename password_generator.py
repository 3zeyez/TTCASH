# password generator - générateur de mot de passe
# ABBASSI Ahmed Aziz

# import random and pickle - importer random and pickle
from pickle import dump, load
import random as rd
import string as s
import time


# creer un mot de passe au hazard - generate a random password
def creer_pwd_rand():
    # declarer les caracteres que le mot de passe peut contenir
    # declare the chars that the password could contain
    all_char = s.ascii_letters + s.digits + s.punctuation

    # generer le mot de passe - generate the password
    pwd = ''.join([rd.choice(all_char) for _ in range(rd.randint(8, 16))])
    print(pwd)
    return pwd


# verifier si le mot de passe contient des lettres, des numeros et des symboles
# verify that the password contain chars, digits and symbols
def isabc123(pwd):
    all_char = s.ascii_letters + s.digits + s.punctuation

    for _ in pwd:
        if _ not in all_char:
            return False
    return True


# creer un mot de passe par l'utilisateur
# generate a password by the user himself
def creer_pwd():
    while True:
        pwd = input('Password (at least 4 characters) : ')
        if len(pwd) >= 8 and isabc123(pwd):
            break
        else:
            print('Password is very week. Try another one!')
    return pwd


# nommer le ficher dont nous travaillons
# name the file that we work on
def file_name():
    while True:
        _file_name = input('Name your file : ')
        if verif(_file_name):
            if _file_name[-4:] == '.pwd':
                return _file_name[:-4]
            return _file_name
        else:
            print('File name doesn\'t support the following characters: \\/:*?"<>|')


# verifier si le nom du fichier est valid
# verify if the file's name is valid
def verif(chaine):
    for i in chaine:
        if i in '\\/:*?"<>|':
            return False
    return True


# creer un nouveau fichier
# create a new file
def creer_file():
    file = open(file_name() + '.pwd', 'wb')
    file.close()
    # cette fonction n'est pas terminee
    # this function is not completed


# ajouter dans un fichier existant
# append in an existed file
# noinspection PyBroadException
def ajout_in_file(_file_name):
    try:
        file = open(_file_name + '.pwd', 'ab')

        domain = lire_domain()

        if existed_domain(domain, _file_name):
            raise Exception

        pwd_rand = pass_rand()

        if pwd_rand:
            data = {'domain': domain, 'pwd': creer_pwd_rand()}
        else:
            data = {'domain': domain, 'pwd': creer_pwd()}

        dump(data, file)
        file.close()

    except FileNotFoundError:
        print('Please enter a valid file name!')

    except Exception:
        print('The domain name is used!')


def existed_domain(domain, _file_name):
    file = open(_file_name + '.pwd', 'rb')

    while True:
        try:
            data = load(file)
            if data['domain'] == domain:
                return True

        except EOFError:
            break

    file.close()


# lire tout le fichier existant
# read the whole file
def read_file():
    try:
        file = open(file_name() + '.pwd', 'rb')

        counter = 0
        while True:
            try:
                data = load(file)
                print(data['domain'], ':', data['pwd'])
                counter += 1

            except EOFError:
                if counter == 0:
                    print('File is empty!')
                else:
                    print('End file!')
                break

        file.close()

    except FileNotFoundError:
        print('Please enter a valid file name!')
        read_file()


# choisir le mode de fonctionnement du programme
# choose the running mode
def lire_mode():
    modes = ['1', '2', '3', '4', '5', 'q', 'Q', 'quit']
    while True:
        mode = input('What mode you want? : ')
        if mode in modes:
            break
    return mode


# donner le nom du domaine
# name the domain
def lire_domain():
    while True:
        domain = input('Enter domain : ')
        if domain != '':
            break
    return domain


# choisir si le mot de passe est au hazard ou non
# choose if the password is random or not
def pass_rand():
    while True:
        rand = input('Random password? yes or no? ')
        if rand.lower() in ['yes', 'no']:
            break
    if rand.lower() == 'yes':
        return True
    else:
        return False


# mettre le domaine ou le mot de passe a jour
# update the domain or the password
def dom_or_pwd():
    while True:
        rep = input('Do you want to update the domain or the password or both? domain or pwd or both?\n')
        if rep.lower() in ['domain', 'pwd', 'both']:
            break
        else:
            print('If you want to update the domain type "domain".\n'
                  + 'If you want to update the password type "pwd".\n'
                  + 'If you want to update the domain and the password as well type "both".')
    return rep.lower()


# lire le nouveau domaine
# read the new domain
def lire_n_domain():
    while True:
        domain = input('Enter new domain : ')
        if domain != '':
            break
    return domain


# mettre le fichier a jour - update of the file
def update():
    try:
        _file_name = file_name()
        file = open(_file_name + '.pwd', 'rb')
        tab = []
        rep = dom_or_pwd()

        if rep == 'domain':
            domain = lire_domain()
            n_domain = lire_n_domain()

            while True:
                try:
                    data = load(file)
                    if data['domain'] == domain:
                        n_data = {'domain': n_domain, 'pwd': data['pwd']}
                        tab.append(n_data)
                    else:
                        tab.append(data)
                except EOFError:
                    break

        elif rep == 'pwd':
            domain = lire_domain()

            pwd_rand = pass_rand()
            if pwd_rand:
                n_pwd = creer_pwd_rand()
            else:
                n_pwd = creer_pwd()

            while True:
                try:
                    data = load(file)
                    if data['domain'] == domain:
                        n_data = {'domain': data['domain'], 'pwd': n_pwd}
                        tab.append(n_data)
                    else:
                        tab.append(data)
                except EOFError:
                    break

        else:
            domain = lire_domain()
            n_domain = lire_n_domain()

            pwd_rand = pass_rand()
            if pwd_rand:
                n_pwd = creer_pwd_rand()
            else:
                n_pwd = creer_pwd()

            while True:
                try:
                    data = load(file)
                    if data['domain'] == domain:
                        n_data = {'domain': n_domain, 'pwd': n_pwd}
                        tab.append(n_data)
                    else:
                        tab.append(data)
                except EOFError:
                    break

        file.close()

        file = open(_file_name + '.pwd', 'wb')

        for data in tab:
            dump(data, file)

        file.close()

    except FileNotFoundError:
        print('Please enter a valid file name!')
        update()


# supprimer un domaine - delete domain
def delete():
    _file_name = file_name()
    domain = lire_domain()
    tab = []

    try:
        file = open(_file_name + '.pwd', 'rb')

        while True:
            try:
                data = load(file)
                if data['domain'] == domain:
                    continue
                tab.append(data)

            except EOFError:
                break

        file.close()

        file = open(_file_name + '.pwd', 'wb')

        for data in tab:
            dump(data, file)

        file.close()
    except FileNotFoundError:
        delete()


# le programme principal - the main program
def main():
    modes = [
        'Create a new file',
        'Add to file',
        'Read file',
        'Update file',
        'Delete domain from file',
        'Enter (q or Q or quit) to quit!'
    ]

    lens = []
    for mode in modes:
        lens.append(((len(modes[4]) - len(mode)) // 2) * ' ')

    space = ((len(modes[5]) - len("Password Handler")) // 2) * "*"
    print(f'{space}Password Handler{space}')

    for _ in range(len(modes) - 1):
        print(f'{_ + 1}. {lens[_]}{modes[_]}{lens[_]}')

    print('Enter (q or Q or quit) to quit!')

    while True:
        mode = lire_mode()
        if mode == '1':
            creer_file()
            # ce mode n' est pas complete
            # this mode in not completed

        if mode == '2':
            _file_name = file_name()
            ajout_in_file(_file_name)

        if mode == '3':
            read_file()

        if mode == '4':
            update()

        if mode == '5':
            delete()

        if mode in ['q', 'Q', 'quit']:
            time.sleep(0.5)
            print('Program closed successfully!')
            break


# exécuter le programme - run the program
if __name__ == '__main__':
    main()
