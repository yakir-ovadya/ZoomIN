from django.test import RequestFactory, TestCase
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser, User
from .views import *
from .models import *
from .forms import *
# Create your tests here.


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# testing views(we have 2 different types) - 17
class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup(self):
        request = self.factory.get('/signup/')
        request.user = AnonymousUser()
        response = register(request)
        self.assertEqual(response.status_code, 200)

    def test_grades(self):
        request= self.factory.get('grades')
        response=grades(request)
        self.assertEqual(response.status_code,200)

    def test_presence(self):
        request= self.factory.get('presence')
        response=presence(request)
        self.assertEqual(response.status_code,200)

    def test_schedule1(self):
        request= self.factory.get('schedule')
        response=schedule(request)
        self.assertNotEqual(response.status_code, 404)

    def test_schedule2(self):
        request= self.factory.get('schedule')
        response=schedule(request)
        self.assertNotEqual(response.status_code, 302)

    def test_schedule3(self):
        request= self.factory.get('schedule')
        response=schedule(request)
        self.assertEqual(response.status_code, 200)

    def test_usernamerecovery1(self):
        request= self.factory.get('Username_Recovery')
        response=Username_Recovery(request)
        self.assertNotEqual(response.status_code, 404)

    def test_usernamerecovery2(self):
        request= self.factory.get('Username_Recovery')
        response=Username_Recovery(request)
        self.assertNotEqual(response.status_code, 302)

    def test_usernamerecovery3(self):
        request= self.factory.get('Username_Recovery')
        response=Username_Recovery(request)
        self.assertEqual(response.status_code, 200)

    def test_bulletin_board_class(self):
        request= self.factory.get('bulletin_board_class')
        response=Username_Recovery(request)
        self.assertEqual(response.status_code, 200)

    def test_bulletin_board(self):
        request= self.factory.get('bulletin_board')
        response=Username_Recovery(request)
        self.assertNotEqual(response.status_code, 404)

    def test_addBoardSchool(self):
        request = self.factory.get('addBoardSchool')
        response = Username_Recovery(request)
        self.assertNotEqual(response.status_code, 404)

    def test_addBoardClass(self):
        request = self.factory.get('addBoardClass')
        response = Username_Recovery(request)
        self.assertEqual(response.status_code, 200)

    def test_bulletin_Schedule(self):
        request = self.factory.get('bulletin_Schedule')
        response = bulletin_Schedule(request)
        self.assertEqual(response.status_code, 200)

    def test_addTest(self):
        request = self.factory.get('bulletin_Schedule')
        response = bulletin_Schedule(request)
        if response:
            self.assertEqual(response.status_code, 200)
        else:
            self.assertNotEqual(response.status_code, 200)

    def test_editTest(self):
        request = self.factory.get('bulletin_Schedule')
        response = bulletin_Schedule(request)
        if response:
            self.assertNotEqual(response.status_code, 404)
        else:
            self.assertNotEqual(response.status_code, 200)

    def test_addpresence(self):
        request = self.factory.get('presence')
        response = addpresence(request)
        if response:
            self.assertEqual(response.status_code, 200)
        else:
            self.assertNotEqual(response.status_code, 200)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# testing model (we have 2 different types and 4 different classes) - 12
class board_school_models(TestCase):
    def setUp1(self):
        return board_school.objects.create(topic="test", description="this is test",publication_date=timezone.now())

    def test_board_school1(self):
        w = self.setUp1()
        self.assertTrue(isinstance(w, board_school))

    def test_board_class2(self):
        w = self.setUp1()
        self.assertFalse(isinstance(w, board_class))

    def test_schedule_model(self):
        w=self.setUp1()
        self.assertFalse(isinstance(w,schedule_mod))


class board_class_models(TestCase):
    def setUp2(self):
        return board_class.objects.create(topic="test", description="this is test",publication_date=timezone.now())

    def test_board_school2(self):
        w = self.setUp2()
        self.assertFalse(isinstance(w, board_school))

    def test_board_class1(self):
        w = self.setUp2()
        self.assertTrue(isinstance(w, board_class))

    def test_board_class3(self):
        w = self.setUp2()
        self.assertFalse(isinstance(w, schedule_mod))


class Presence_models(TestCase):
    def setUp3(self):
        return Presence_mod.objects.create(First_Name="fn", Last_Name="ln",exist=True, not_exist=False, date=timezone.now(), profession='math', hour=None)

    def test_Presence_mod1(self):
        w = self.setUp3()
        self.assertTrue(isinstance(w, Presence_mod))

    def test_Presence_mod2(self):
        w = self.setUp3()
        self.assertFalse(isinstance(w, board_class))

    def test_Presence_mod3(self):
        w = self.setUp3()
        self.assertFalse(isinstance(w, Test_Schedule))


class Test_Schedule_models(TestCase):
    def setUp4(self):
        return Test_Schedule.objects.create(profession="math", date=timezone.now(),start_time=None, end_time=None)

    def test_Presence_mod1(self):
        w = self.setUp4()
        self.assertTrue(isinstance(w, Test_Schedule))

    def test_Presence_mod2(self):
        w = self.setUp4()
        self.assertFalse(isinstance(w, Presence_mod))

    def test_Presence_mod3(self):
        w = self.setUp4()
        self.assertFalse(isinstance(w, board_school))

#------------------------------------------------------------------------------------------------------------------------------------------------------
# testing forms (we have 2 different types and 2 different classes) - 4
class  board_class_form(TestCase):
    def test_valid_form_board_class1(self):
        w = board_class.objects.create(topic="test", description="this is test", publication_date=timezone.now())
        data = {'topic': w.topic, 'description': w.description,' publication_date': w.publication_date}
        form = board_schoolForm(data=data)
        self.assertTrue(form.is_valid() != True)

    def test_valid_form_board_class2(self):
        w = board_class.objects.create(topic="test", description="this is test", publication_date=timezone.now())
        data = {'topic': w.topic, 'description': w.description,' publication_date': w.publication_date}
        form = board_classForm(data=data)
        self.assertTrue(form.is_valid() == False)

class  board_school_form(TestCase):
    def test_valid_form_board_school1(self):
        w = board_school.objects.create(topic="test", description="this is test", publication_date=timezone.now())
        data = {'topic': w.topic, 'description': w.description,' publication_date': w.publication_date}
        form = board_schoolForm(data=data)
        self.assertTrue(form.is_valid() == False)

    def test_valid_form_board_school2(self):
        w = board_school.objects.create(topic="test", description="this is test", publication_date=timezone.now())
        data = {'topic': w.topic, 'description': w.description,' publication_date': w.publication_date}
        form = board_classForm(data=data)
        self.assertTrue(form.is_valid() != True)

