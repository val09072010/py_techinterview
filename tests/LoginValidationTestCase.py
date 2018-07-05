#!/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import os
import unittest
import o3_inputvalidator.InputValidatorsFunc as InputValidator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class LoginValidationTestCase(unittest.TestCase):
    valids = ['a', 'foo-bar', 'foo.bar', 'joe2cool', 'joe.doe-cool4you', 'end-up-with5', 'bc']
    invalids = ['wdf-54@#9adsfgd7', 'firыt', 'ё1', 'duiygffuЭ', '2cool', 'wrong_char$', 'wow!', 'this-is-too-long-to-fit-the-rule', 'end-up-with-', '']

    def test_regex_with_valids(self):
        for login in self.valids:
            self.assertTrue(InputValidator.validate_login_regex_way(login))

    def test_regex_with_invalids(self):
        for login in self.invalids:
            self.assertFalse(InputValidator.validate_login_regex_way(login))

    def test_weird_with_valids(self):
        for login in self.valids:
            self.assertTrue(InputValidator.validate_login_weird_way(login))

    def test_weird_with_invalids(self):
        for login in self.invalids:
            self.assertFalse(InputValidator.validate_login_weird_way(login))

    def test_errormodel_with_valids(self):
        for login in self.valids:
            mdl = InputValidator.validate_login_error_model_way(login)
            self.assertFalse(len(mdl))

    def test_errormodel_with_invalids(self):
        for login in self.invalids:
            mdl = InputValidator.validate_login_error_model_way(login)
            self.assertTrue(len(mdl))


if __name__ == '__main__':
    unittest.main()
