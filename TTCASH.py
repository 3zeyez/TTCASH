# libs importation
import random as rd
import time


# num tel generator
def generate():
    num = str(rd.randint(0000000, 9999999))
    num = f'9{"0" * (7 - len(num))}{num}'
    # print(f'{num[:2]} {num[2:5]} {num[5:]}')
    # return f'{num[:2]} {num[2:5]} {num[5:]}'
    return num


# get the user answer
def get_answer():
    while True:
        rep = '9' + input('Give your answer : \n9')
        if rep.isdigit() and len(rep) == 8:
            return rep
        else:
            print('The phone number support just digits!')
            print('The length of the phone number should equal to 8!')
            print('Please enter a valid answer!')


# # check if the num has any right digit
def check(num, org):
    if num == org:
        return True
    return False


def extraire(ch, org, nb):
    extrait = ''
    for _ in range(len(ch)):
        if org[_] == nb:
            extrait += ch[_]
    return extrait


def test(num, org):
    num = num[1:]
    org = org[1:]
    ch = ''
    for _ in range(len(num)):
        if num[_] == org[_]:
            ch += 'T'
        else:
            ch += 'F'

    ch1 = ''
    for _ in range(len(num)):
        if ch[_] == 'F' and num[_] in org and extraire(ch, org, num[_]).count('F') > 0:
            ch1 += 'O'
        else:
            ch1 += ch[_]
    return ch1


def main():
    print('=' * 68)
    print(f'{"=" * 31}TTCASH{"=" * 31}')
    print('Game rules :')
    print('You have just 5 trial to guess the phone number 9*******.')
    print('T means the given digit in that position is valid.     - T is True.')
    print('F means the given digit in that position is not valid  - F is False.')
    print('O means the given digit is not in the right position.  - O is Other')
    print(f'{"=" * 31}TTCASH{"=" * 31}')
    print('=' * 68)

    tel = generate()
    for _ in range(1, 6):
        print(f'Trial N°{_}:')
        ans = get_answer()
        end_game = check(ans, tel)
        if end_game:
            print('You win!')
            print(f'{"=" * 31}TTCASH{"=" * 31}')
            print('=' * 68)
            break
        else:
            print(f' {test(ans, tel)}')
        if _ == 5:
            print('You lose!')
            print(f'The phone number is {tel}!')
            print(f'{"=" * 31}TTCASH{"=" * 31}')
            print('=' * 68)


if __name__ == '__main__':
    main()
    time.sleep(30)
