from django.test import TestCase
from django.shortcuts import reverse
from accounts.forms import UserLoginForm, UserRegistrationForm

# ----- FORMS ----- #

class Test_User_Login_Form(TestCase):
    def test_log_in_valid(self):
        form = UserLoginForm(
            {"username": "TestUser", "password": "Password"})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])


class Test_User_Registration_Form(TestCase):
    def test_register_form_valid(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "testemail@gmail.com",
                "password1": "TestPassword", "password2": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_passwords_do_not_match(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "testemail@gmail.com",
                "password1": "TestPassword", "password2": "TestPassword123"})
        self.assertFalse(form.is_valid())
            #     self.assertEqual(
            # form.errors["password2"], [u"Passwords must match!"])

# ----- VIEWS----- #

class Accounts_View_Test(TestCase):
    def test_login_view(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_logout_view(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("index")) 
    
    def test_register_view(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    # def test_profile_view(self):
    #     page = self.client.get("/accounts/profile/")
    #     self.assertEqual(page.status_code, 302)
    #     self.client.post(reverse("profile"))
