#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import re

MAX_LEN = 20


def validate_login_regex_way(login, log_max=MAX_LEN):
    """
        Вариант №1 --- RegEx
    """
    if login:
        log_len = len(login)
        if log_len == 1:
            return login.isalpha()
        elif log_len < log_max:
            return bool(re.search(r'^[a-zA-Z][a-zA-Z0-9.-]*[a-zA-Z0-9]$', login))
    return False


def validate_login_weird_way(login, log_max=MAX_LEN):
    """
        Вариант №2 --- ASCII char codes and lambda functions
    """
    if login and len(login) <= log_max:
        if len(login) == 1:
            return login.isalpha() and ord(login) < 123
        codes = map((lambda char: ord(char)), login[1:-1])
        res = list(filter((lambda code: code != 45 and code != 46 and (code not in range(48, 58)) and (code not in range(65, 91)) and (code not in range(97, 123))), codes))
        return len(res) == 0 and (login[-1].isalnum() and ord(login[-1]) < 123) and (login[0].isalpha() and ord(login[0]) < 123)
    return False


def validate_login_error_model_way(login, log_max=MAX_LEN):
    """
        Вариант №2 --- error model
    """
    error_model = {}
    log_len = len(login)

    if log_len < 1 or log_len > log_max:
        error_model['length'] = "Wrong length. Login should be 1 to %d chars long" % log_max

    if (login and not login[0].isalpha()) or (login and ord(login[0]) > 123):
        error_model['first'] = 'Wrong first char. Char should be a Latin char'

    if (login and not login[-1].isalnum()) or (login and ord(login[-1]) > 123):
        error_model['last'] = 'Wrong last char. Char should be a Latin char or Number'

    if log_len > 2 and not re.search(r'^[a-zA-Z][a-zA-Z0-9.-]*[a-zA-Z0-9]$', login[1:-1]):
        error_model['content'] = "Wrong content. Login must consists of Latins, digits, '.' and '-'"

    if len(error_model) > 0:
        error_model['value'] = login

    return error_model


def main():
    valids = ['a', 'foo-bar', 'foo.bar', 'joe2cool',
              'joe.doe-cool4you', 'end-up-with5', 'bc']
    invalids = ['2cool', 'wrong_char$', 'wow!', 'this-is-too-long-to-fit-the-rule',
                'end-up-with-', 'name-ру', 'ё1', '', 'wdf-54@#9adsfgd7']

    print("======================== Option 1 ========================")
    for login in valids:
        if not validate_login_regex_way(login):
            print("FAIL: valid login {0} unidentified".format(login))

    for login in invalids:
        if validate_login_regex_way(login):
            print("FAIL: invalid login {0} accepted".format(login))

    print("======================== Option 2 ========================")
    for login in valids:
        if not validate_login_weird_way(login):
            print("FAIL: valid login {0} unidentified".format(login))

    for login in invalids:
        if validate_login_weird_way(login):
            print("FAIL: invalid login {0} accepted".format(login))

    print("======================== Option 3 ========================")
    for login in valids:
        mdl = validate_login_error_model_way(login)
        if len(mdl) > 0:
            print("FAIL: valid login {0} unidentified".format(login))
            print(mdl)

    for login in invalids:
        mdl = validate_login_error_model_way(login)
        print(mdl)
        if len(mdl) == 0:
            print("FAIL: invalid login {0} accepted".format(login))


if __name__ == '__main__':
    main()
