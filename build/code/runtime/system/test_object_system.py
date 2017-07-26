
## -*- coding: utf-8 -*-
#import unittest
#from unittest import TestCase
#import datetime
#from runtime.system.system import *
#from object_delegates import * 
#
#from system import *
#
##config = {
##   'SQLALCHEMY_DATABASE_URI': ''
##}
#
#class TestSystemConstructor(TestCase):
#    TESTING = True
#    def setUp(self):
#	System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#	admin = filter( lambda x: x.get("email").get("email") ==
#			"app-admin@vlabs.ac.in",
#			System.delegate.user_set)
#	System.user_set = admin
#	System.session_set = []
#	System.delegate.institute_set = []
#	System.delegate.oc_set = []
#	System.delegate.nc_set = []
#
# 
#   
#    def test_system_constructor(self):
#        print "test_system_constructor"
#        self.assertEqual(System.delegate.user_set[0].get("name").get("name"),
#                         Config.admin_name)
#        self.assertEqual(System.delegate.user_set[0].get("email").get("email"),
#                         "app-admin@vlabs.ac.in")
#        self.assertEqual(System.delegate.user_set[0].get('roles')[0].get('name'),
#                         "admin")
#
#    def test_is_session_admin(self):
#        print "test_is_session_admin"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        self.assertEqual(System.is_session_admin(session), True)
#
#    def test_is_session_OC(self):
#        print "test_is_session_OCC"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,
#                          role=Role(name="OCC",centre_oc=None,centre_nc=None))
#        System.session_set.append(session)
#        self.assertEqual(System.is_session_OCC(session), True)
#
#    def test_is_session_NCC(self):
#        print "test_is_session_NCC"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,
#                          role=Role(name="NCC",centre_oc=None,centre_nc=None))
#        System.session_set.append(session)
#        self.assertEqual(System.is_session_NCC(session), True)
#
#    def test_is_session_reviewer(self):
#        print "test_is_session_reviewer"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.reviewer)
#        System.session_set.append(session)
#        self.assertEqual(System.is_session_reviewer(session), True)
#
#    def test_is_session_guest(self):
#        print "test_is_session_guest"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.guest)
#        System.session_set.append(session)
#        self.assertEqual(System.is_session_guest(session), True)
#
#    def test_is_session_noc(self):
#        print "test_is_session_noc"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.noc)
#        System.session_set.append(session)
#        self.assertEqual(System.is_session_noc(session), True)
#
#    def test_session_exists(self):
#        print "test_session_exists"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user, role=Role.admin)
#        System.session_set.append(session)
#        self.assertEqual(System.session_exists(session), True)
#
#class TestSystemArityAndType(TestCase):
#    TESTING = True
#
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.delegate = None
#
#    def test_arity(self):
#        print "test_arity"
#        with self.assertRaises(ArityError):
#            System.arity_check([1,2], 3)
#
#    def test_type_checks(self):
#        print "test_type_checks"
#        args = {"name": Name(name="Jimi Hendrix"),
#                "email": Name(name="Jimi Hendrix")
#                }
#
#        arg_types = {"name": is_name,
#                     "email": is_email
#                     }
#
#        with self.assertRaises(TypeError):
#            System.type_check(args, arg_types)
#
#class TestAddUser(TestCase):
#    TESTING = True
#    def setUp(self):
#	System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#	admin = filter( lambda x: x.get("email").get("email") ==
#			"app-admin@vlabs.ac.in",
#			System.delegate.user_set)
#	System.user_set = admin
#	System.session_set = []
#	System.delegate.institute_set = []
#	System.delegate.oc_set = []
#	System.delegate.nc_set = []
#
#    def test_add_user_by_admin(self):
#	print "test_add_user_by_admin"
#	admin_user=System.delegate.user_set[0]
#	session = Session(user=admin_user,role=Role.admin)
#	System.session_set.append(session)
#
#	user_name=Name(name="me")
#	user_email=Email(email="abc@gmail.com")
#
#	user = User(name=user_name, email= user_email, roles= [Role.guest],
#		    user_status="active")
#
#	u = System.do("add_user", user=user, session=session)
#
#	u = System.delegate.user_set[1]
#	self.assertEqual(u.get("name").get("name"),"me")
#
#    def test_add_user_noc_by_admin(self):
#	print "test_add_user_by_noc"
#	admin_user=System.delegate.user_set[0]
#	session = Session(user=admin_user,role=Role.admin)
#	System.session_set.append(session)
#
#	name = Name(name="nocuser")
#	email= Email(email="abc@gmail.com")
#	user = User(name=name, email= email, roles= [Role.guest],
#		    user_status="active")
#
#	noc_user= System.do("add_user", user=user, session=session)
#
#	session_noc = Session(user=noc_user,role=Role.noc)
#	System.session_set.append(session_noc)
#
#	u=System.delegate.user_set[1]
#	self.assertEqual(u.get("name").get("name"),"nocuser")
#
#    def test_add_user_by_noc(self):
#	print "test_add_user_by_noc"
#	admin_user=System.delegate.user_set[0]
#	session = Session(user=admin_user,role=Role.admin)
#	System.session_set.append(session)
#
#	name = Name(name="nocuser")
#	email= Email(email="abc@gmail.com") 
#	user = User(name=name, email= email, roles= [Role.guest],
#		    user_status="active")
#
#	noc_user=System.do("add_user", user=user, session=session)
#
#	session_noc = Session(user=noc_user, role=Role.noc)
#	System.session_set.append(session_noc)
#
#        inst = Institute(name = "IIT", address = "Delhi")
#	institute = System.do("create_institute", institute=inst,
#			       session=session)
#	oc = System.do("create_oc",institute=institute, session=session,
#			spokes=[], oc_target = None)
#
#	name1 = Name(name="ocuser")
#	email1 = Email(email="mary@gmail.com")       
#        user = User(name=name1, email= email1, roles= [Role.guest],
#		    user_status="active")
#	oc_user = System.do("add_user", user=user, session=session_noc)
#
#	oc_role = filter(lambda x:x.get('name') == "OCC" and
#			 x.get('centre_oc').get("institute").get("name") ==
#			 institute.get("name"), System.delegate.role_set)
#	if oc_role:
#	    oc_user.append_role(oc_role[0])
#
#	u=System.delegate.user_set[2]
#	self.assertEqual(u.get("name").get("name"),"ocuser")
#class TestUpdateUser(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.delegate.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_update_user_by_admin(self):
#        print "test_update_user_by_admin"
#        admin_user = System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#
#        user_name=Name(name="me")
#        user_email=Email(email="abc@gmail.com")
#
#        user = User(name=user_name, email= user_email, roles= [Role.guest],
#                    user_status="active")
#
#        other_user= System.do("add_user", user=user,
#                               session=session)
#
#        user = System.do("update_user", name=Name(name="john"), user=other_user,
#                   session=session)
#
#        self.assertEqual(user.get("name").get("name"), "john")
#
#    def test_update_user_by_occ(self):
#        print "test_update_user_by_occ"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#
#        inst = Institute(name = "IIT", address = "Delhi")
#        institute = System.do("create_institute", institute=inst,
#                               session=session)
#        oc = System.do("create_oc",institute=institute,session=session,
#                        spokes=[], oc_target = None)
#
#        name=Name(name="useroc")
#        email=Email(email="useroc@gmail.com")       
#        user = User(name=name, email=email, roles= [Role.guest],
#                    user_status="active")
#        oc_user=System.do("add_user", user=user, session=session)
#
#        oc_role = filter(lambda x:x.get('name') == "OCC" and
#                         x.get('centre_oc').get("institute").get("name") ==
#                         institute.get("name"), System.delegate.role_set)
#        if oc_role:
#            oc_user.append_role(oc_role[0])
#        #create nc
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#
#        name1=Name(name="usernc")
#        email1=Email(email="usernc@gmail.com")
#        user = User(name=name1, email=email1, roles= [Role.guest],
#                    user_status="active")
#        nc_user= System.do("add_user", user=user,
#                            session=session)
#
#        nc_role = filter(lambda x:x.get('name') == "NCC" and
#                         x.get('centre_nc').get("institute").get("name") ==
#                         institute.get("name"), System.delegate.role_set)
#        if nc_role:
#            nc_user.append_role(nc_role[0])
#
#       
#        oc_session = Session(user=oc_user,role=oc_role[0])
#        System.session_set.append(oc_session)
#
#        length = len(System.delegate.user_set)
#        System.do("update_user", name=Name(name="jack"), user=nc_user,
#                   session=oc_session)
#        new_length = len(System.delegate.user_set)
#
#        self.assertEqual(nc_user.get("name").get("name"), "jack")       
#
#
#    def test_update_user_by_noc(self):
#        print "test_update_user_by_noc"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#       
#        inst = Institute(name = "IIT", address = "Madras")
#        institute = System.do("create_institute",institute=inst,
#                               session=session)
#        oc = System.do("create_oc",institute = institute, session = session,
#                        spokes = [], oc_target = None)
#       
#        name=Name(name="useroc")
#        email=Email(email="useroc@gmail.com")
#        user = User(name=name, email=email, roles= [Role.guest],
#                    user_status="active")
#        oc_user= System.do("add_user", user=user, session=session)
#
#        oc_role = filter(lambda x:x.get('name') == "OCC" and
#                         x.get('centre_oc').get("institute").get("name") ==
#                         institute.get("name"), System.delegate.role_set)
#        if oc_role:
#            oc_user.append_role(oc_role[0])
#
#        name1=Name(name="usernoc")
#        email1=Email(email="usernoc@gmail.com")
#        user = User(name=name1, email=email1, roles= [Role.guest],
#                    user_status="active")
#        noc_user=System.do("add_user", user=user,
#                            session=session)
#
#        noc_user.append_role(Role.noc)
#       
#
#        noc_session = Session(user=noc_user,role=Role.noc)
#        System.session_set.append(noc_session)
#
#        length = len(System.delegate.user_set)
#        System.do("update_user", name=Name(name="jack"), user=oc_user,
#                   session=noc_session)
#        new_length = len(System.delegate.user_set)
#
#        self.assertEqual(oc_user.get("name").get("name"), "jack")       
#
#class TestDeleteUser(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.delegate.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_delete_admin_user(self):
#        print "test_delete_user"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#
#        user_name=Name(name="me")
#        user_email=Email(email="abc@gmail.com")
#
#        user = User(name=user_name, email= user_email, roles= [Role.guest],
#                    user_status="active")
#
#
#        other_admin_user= System.do("add_user", user=user,
#                                    session=session)
#
#        other_admin_user.append_role(Role.admin)
#        length = len(System.delegate.user_set)
#        System.do("delete_user", user=other_admin_user, session=session)
#        self.assertEqual(other_admin_user.get("user_status"),"inactive")
#
#
#    def test_delete_user_by_occ(self):
#        print "test_delete_user_by_occ"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#
#        inst = Institute(name = "IIT", address = "Delhi")
#        institute = System.do("create_institute", institute=inst,
#                               session=session)
#        oc = System.do("create_oc",institute=institute,session=session,
#                        spokes=[], oc_target = None)
#       
#        name = Name(name="maryoc")
#        email = Email(email="mary@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#        oc_user= System.do("add_user", user=user, session=session)
#        
#        
#        oc_role = filter(lambda x:x.get('name') == "OCC" and
#                         x.get('centre_oc').get("institute").get("name") ==
#                         institute.get("name"), System.delegate.role_set)
#        if oc_role:
#            oc_user.append_role(oc_role[0])
#
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#
#        name1 = Name(name="xyznc")
#        email1 = Email(email="xyz@gmail.com")
#        user = User(name=name1, email= email1, roles= [Role.guest],
#                    user_status="active")
#        nc_user = System.do("add_user", user=user,
#                             session=session)
#
#        nc_role = filter(lambda x:x.get('name') == "NCC" and
#                         x.get('centre_nc').get("institute").get("name") ==
#                         institute.get("name"), System.delegate.role_set)
#        if nc_role:
#            nc_user.append_role(nc_role[0])
#
#
#        oc_session = Session(user=oc_user,role=oc_role[0])
#        System.session_set.append(oc_session)
#
#        length = len(System.delegate.user_set)
#        System.do("delete_user", user=nc_user, session=oc_session)
#       
#        self.assertEqual(nc_user.get("user_status"),"inactive")
#
#    def test_delete_user_by_noc(self):
#        print "test_delete_user_by_noc"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#
#        inst = Institute(name = "IIT", address = "Delhi")
#        institute = System.do("create_institute", institute=inst,
#                               session=session)
#
#        oc = System.do("create_oc",institute=institute,session=session,
#                        spokes=[], oc_target = None)
#       
#        name = Name(name="maryoc")
#        email = Email(email="mary@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#        oc_user= System.do("add_user", user=user, session=session)
#        
#        
#        oc_role = filter(lambda x:x.get('name') == "OCC" and
#                         x.get('centre_oc').get("institute").get("name") ==
#                         institute.get("name"), System.delegate.role_set)
#        if oc_role:
#            oc_user.append_role(oc_role[0])
#
#        name1=Name(name="xyznc")
#        email1=Email(email="xyz@gmail.com")
#        user = User(name=name1, email= email1, roles= [Role.guest],
#                    user_status="active")
#        noc_user = System.do("add_user", user=user,
#                              session=session)
#
#        noc_user.append_role(Role.noc)
#
#       
#        noc_session = Session(user=noc_user,role=Role.noc)
#        System.session_set.append(noc_session)
#
#        length = len(System.delegate.user_set)
#        System.do("delete_user", user=oc_user, session=noc_session)
#        
#        self.assertEqual(oc_user.get("user_status"),"inactive")
#
#class Testlogin(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.delegate.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#    def test_login(self):
#        print "test_login"
#        login_user=System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        System.do("login",user=login_user,role=login_role)
#        session=System.session_set[0]
#        self.assertEqual(session.get("user").get("name").get("name"),"admin")
#        self.assertEqual(session.get("user").get('roles')[0].get('name'),
#                         "admin")
#class Testlogout(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#    def test_logout(self):
#        print "test_logout"
#        login_user=System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        sess = System.do("login",user=login_user,role=login_role)
#        self.assertEqual(len(System.session_set),1)
#        System.do("logout",session=sess)
#        self.assertEqual(System.session_set,[])
#class TestCreateInstitute(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_create_institute(self):
#        print "test_create_institute"
#        login_user=System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        sess = System.do("login",user=login_user,role=login_role)
#        inst = Institute(name = "IIT", address = "Delhi")
#        institute = System.do("create_institute", institute=inst, session=sess)
#        self.assertEqual(institute,System.delegate.institute_set[0])
#
#
#class TestCreateOC(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.delegate.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_create_oc(self):
#        print "test_create_oc"
#        login_user=System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        sess = System.do("login",user=login_user,role=login_role)
#        inst = Institute(name = "IIT", address = "Delhi")
#        institute = System.do("create_institute", institute=inst, session=sess)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=sess, oc_target = None)
#        self.assertEqual(oc.get('institute'),institute)
#        #self.assertRaises(StateError,System.do,"create_oc",institute=institute,session=sess)
#
#class TestCreateNC(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.delegate.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_create_nc(self):
#        print "test_create_nc"
#        login_user=System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        sess = System.do("login",user=login_user,role=login_role)
#        inst = Institute(name = "IIT", address = "Delhi")
#        institute = System.do("create_institute", institute = inst, session=sess)
#        oc = System.do("create_oc",institute=institute,spokes=[],session=sess,
#                        oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=sess,
#                        nc_target = None, workshops = [])
#        self.assertEqual(nc.get('institute'),institute)
#        self.assertEqual(oc.get('spokes')[0],nc)
#
#class TestAddRole(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_add_role(self):
#        print "test_add_role"
#        admin_user = System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#
#        user_name=Name(name="me")
#        user_email=Email(email="abc@gmail.com")
#
#        user = User(name=user_name, email= user_email, roles= [Role.guest],
#                    user_status="active")
#
#        other_user= System.do("add_user", user=user,
#                               session=session)
#
#        us = System.do("add_role", user=other_user, role=Role.noc, session=session)
#        self.assertTrue(len(us.get('roles'))==2)
#
#class TestUpdateInstitute(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.delegate.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#
#    def test_update_institute(self):
#        print "test_update_institute"
#        login_user = System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute=inst, session=session)
#        inst = System.do("update_institute",name="NITK",institute=institute,
#                   session=session)
#        self.assertEqual(inst.get("name"),"NITK")
#
#class TestCreateWorkshop(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_create_workshop(self):
#        print "test_create_workshop"
#        login_user = System.delegate.user_set[0]
#        login_role = System.delegate.role_set[0]
#        sess = System.do("login",user=login_user,role=login_role)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute",institute=inst1, session=sess)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = sess)
#        oc = System.do("create_oc",institute=institute,spokes=[],session=sess,
#                        oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=sess,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date,
#                             oc_target = oc_target, wstargets = [])
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target )
#        session = Session(user=login_user,role=Role.admin)
#        System.session_set.append(session)
#        ws_status = Status.pending
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user", user=user,
#                             session = sess)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc, centre_nc = nc))
#        System.session_set.append(nc_session)
#
#        new_workshop = System.do("create_workshop",
#                                 institute = workshop_institute,
#                                 name = Name(name = "Lab Workshop"),
#                                 ws_target = wstarget,
#                                 status = ws_status,
#                                 artefacts = [],
#                                 nc = nc,
#                                 session = nc_session)
#
#        self.assertEqual(new_workshop.get('institute'),workshop_institute)
#class TestCancelWorkshop(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_cancel_workshop(self):
#        print "test_cancel_workshop"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1, session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date,
#                             oc_target = oc_target, wstargets = [])
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        
#        ws_status = Status.pending
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user",user=user,
#                            session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc, centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                 institute = workshop_institute,
#                                 name = Name(name = "Lab Workshop"),
#                                 ws_target = wstarget, status = ws_status,
#                                 artefacts = [], nc = nc, session = nc_session) 
#        
#        workshop = System.do("cancel_workshop", workshop = new_workshop,
#                  session = nc_session)
#        self.assertEqual(workshop.get("status").get("name"),
#                         Status.cancelled.get("name"))
##        self.assertEqual(nc.get("workshops")[0].get("status").get("name"),
##                         Status.cancelled.get("name"))
#        
#class TestRescheduleWorkshop(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_reschedule_workshop(self):
#        print "test_reschedule_workshop"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1,
#                               session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date,
#                             oc_target = oc_target, wstargets = [])
#        
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        ws_status = Status.pending
#
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user",user=user,
#                             session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc, centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                 institute = workshop_institute,
#                                 name = Name(name = "Lab Workshop"),
#                                 ws_target = wstarget, status = ws_status,
#                                 artefacts = [], nc = nc, session = nc_session) 
#        
#        System.do("cancel_workshop", workshop = new_workshop,
#                   session = nc_session)
#        
#        new_target_date = datetime.datetime.strptime("05-07-2016", "%d-%m-%Y").date()
#        new_wstarget = WSTarget(usage = 3000, participants = 200, experiments = 20,
#                                date = new_target_date, nc_target = nc_target)
#
#        System.do("reschedule_workshop", workshop = new_workshop,
#                   session = nc_session, wstarget = new_wstarget)
#
#        self.assertEqual(new_workshop.get("status").get("name"),
#                         Status.pending.get("name"))
##        self.assertEqual(nc.get("workshops")[0].get("status").get("name"),
##                         Status.pending.get("name"))
#        self.assertEqual(new_workshop.get("ws_target").get("date"),
#                         new_target_date)
#        
#class TestConductWorkshop(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in", 
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_conduct_workshop(self):
#        print "test_conduct_workshop"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1,
#                               session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date, wstargets = [],
#                             oc_target = oc_target)
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        
#        ws_status = Status.pending
#
#
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#
#        nc_user = System.do("add_user",user=user,
#                             session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc,
#                             centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                  institute = workshop_institute,
#                                  name = Name(name = "Lab Workshop"),
#                                  ws_target = wstarget, status = ws_status,
#                                  artefacts = [], nc = nc,
#                                  session = nc_session) 
#        
#        System.do("conduct_workshop", workshop = new_workshop,
#                   session = nc_session)
#        self.assertEqual(new_workshop.get("status").get("name"),
#                         Status.completed.get("name"))
##        self.assertEqual(nc.get("workshops")[0].get("status").get("name"),
##                         Status.completed.get("name"))
#        
#
#class TestUploadArtefact(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_upload_artefact(self):
#        print "test_upload_artefact"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1,
#                               session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date, wstargets = [],
#                             oc_target = oc_target)
#        
#        
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        
#        ws_status = Status.pending
#
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user",user=user,
#                            session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc,
#                             centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                 institute = workshop_institute,
#                                 name = Name(name = "Lab Workshop"),
#                                 ws_target = wstarget, status = ws_status,
#                                 artefacts = [], nc = nc, session = nc_session) 
#        
#        System.do("conduct_workshop", workshop = new_workshop,
#                   session = nc_session)
#        
#
#        new_artefact = Artefact(name = "Photo", path = "/main/photos",
#                                a_type = Type.photo)
#
#        System.do("upload_artefact", workshop = new_workshop,
#                  session = nc_session, artefact = new_artefact)
#        
#        self.assertEqual(new_workshop.get("artefacts")[0].get("name"),
#                         new_artefact.get("name"))
#        self.assertEqual(new_workshop.get("status").get("name") ,
#                         Status.pending_approval.get("name"))
#        
#
#class TestApproveWorkshop(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter(lambda x: x.get("email").get("email") ==
#                       "app-admin@vlabs.ac.in",
#                       System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_approve_workshop(self):
#        print "test_approve_workshop"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1,
#                               session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date,
#                             oc_target = oc_target, wstargets = [])
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        
#        ws_status = Status.pending
#
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user", user=user,
#                             session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc,
#                             centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        name1=Name(name="ocuser")
#        email1=Email(email="ocuser@gmail.com")
#
#        user1 = User(name=name1, email= email1, roles= [Role.guest],
#                    user_status="active")
#        
#        oc_user = System.do("add_user",user=user1,
#                             session = session)
#        oc_user.set(roles=[Role(name = "OCC", centre_oc = oc, centre_nc = None)])
#
#        oc_session = Session(user = oc_user,
#                             role = Role(name = "OCC", centre_oc = oc,
#                             centre_nc = None))
#        System.session_set.append(oc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                 institute = workshop_institute,
#                                 name = Name(name = "Lab Workshop"),
#                                 ws_target = wstarget, status = ws_status,
#                                 artefacts = [], nc = nc, session = nc_session) 
#
#        System.do("conduct_workshop", workshop = new_workshop,
#                  session = nc_session)
#        new_artefact = Artefact(name = "Photo", 
#                                path = "/main/photos", 
#                                a_type = Type.photo)
#
#        System.do("upload_artefact", workshop = new_workshop,
#                  session = nc_session, artefact = new_artefact)
#        
#        System.do("approve_workshop", workshop = new_workshop,
#                   session = oc_session)
#
#        self.assertEqual(new_workshop.get("status").get("name"),
#                         Status.approved.get("name"))
#        
#        
#
#class TestRejectWorkshop(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_reject_workshop(self):
#        print "test_reject_workshop"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1,
#                               session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                        session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date,
#                             oc_target = oc_target, wstargets = [])
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        
#        ws_status = Status.pending
#
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user",user=user,
#                             session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc, centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        name1 = Name(name="ocuser")
#        email1 = Email(email="ocuser@gmail.com")
#
#        user1 = User(name=name1, email= email1, roles= [Role.guest],
#                    user_status="active")
#
#        oc_user = System.do("add_user",user=user1,
#                             session = session)
#        oc_user.set(roles=[Role(name = "OCC", centre_oc = oc, centre_nc = None)])
#        oc_session = Session(user = oc_user,
#                             role = Role(name = "OCC", centre_oc = oc, centre_nc = None))
#        System.session_set.append(oc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                  institute = workshop_institute,
#                                  name = Name(name = "Lab Workshop"),
#                                  ws_target = wstarget, status = ws_status,
#                                  artefacts = [], nc = nc,
#                                  session = nc_session) 
#        System.do("conduct_workshop", workshop = new_workshop,
#                   session = nc_session)
#        new_artefact = Artefact(name = "Photo", path = "/main/photos",
#                                a_type = Type.photo)
#
#        System.do("upload_artefact", workshop = new_workshop,
#                   session = nc_session, artefact = new_artefact)
#        
#        System.do("reject_workshop", workshop = new_workshop,
#                   session = oc_session)
#        self.assertEqual(new_workshop.get("status").get("name"),
#                         Status.rejected.get("name"))
#        
#        
#
#class TestDeleteArtefact(TestCase):
#    TESTING = True
#    def setUp(self):
#        System.initialize_system(ObjectDelegate)
#
#    def tearDown(self):
#        admin = filter( lambda x: x.get("email").get("email") ==
#                        "app-admin@vlabs.ac.in",
#                        System.delegate.user_set)
#        System.user_set = admin
#        System.session_set = []
#        System.delegate.institute_set = []
#        System.delegate.oc_set = []
#        System.delegate.nc_set = []
#        System.delegate.workshop_set = []
#
#    def test_delete_artefact(self):
#        print "test_delete_artefact"
#        admin_user=System.delegate.user_set[0]
#        session = Session(user=admin_user,role=Role.admin)
#        System.session_set.append(session)
#        inst1 = Institute(name = "IIIT", address = "Hyderabad")
#        institute = System.do("create_institute", institute = inst1,
#                               session=session)
#        inst2 = Institute(name = "NITK", address = "Surathkal")
#        workshop_institute = System.do("create_institute", institute = inst2,
#                                        session = session)
#        oc = System.do("create_oc",institute=institute,spokes=[],
#                       session=session, oc_target = None)
#        nc = System.do("create_nc",institute=institute,hub=oc,session=session,
#                        nc_target = None, workshops = [])
#        target_date = datetime.datetime.strptime("30-06-2016", "%d-%m-%Y").date()
#        oc_target = OCTarget(usage = 400, date = target_date, nctargets = [])
#        nc_target = NCTarget(usage = 200, date = target_date,
#                             oc_target = oc_target, wstargets = [])
#        wstarget = WSTarget(usage = 4000, participants = 200, experiments = 20,
#                            date = target_date, nc_target = nc_target)
#        
#        ws_status = Status.pending
#
#        name = Name(name="ncuser")
#        email=Email(email="ncuser@gmail.com")
#        user = User(name=name, email= email, roles= [Role.guest],
#                    user_status="active")
#
#        nc_user = System.do("add_user", user=user,
#                            session = session)
#        nc_user.set(roles=[Role(name = "NCC", centre_oc = oc, centre_nc = nc)])
#        nc_session = Session(user = nc_user,
#                             role = Role(name = "NCC", centre_oc = oc, centre_nc = nc))
#        System.session_set.append(nc_session)
#        
#        new_workshop = System.do("create_workshop",
#                                 institute = workshop_institute,
#                                 name = Name(name = "Lab Workshop"),
#                                 ws_target = wstarget, status = ws_status,
#                                 artefacts = [], nc = nc, session = nc_session) 
#        
#        System.do("conduct_workshop", workshop = new_workshop,
#                  session = nc_session)
#        
#
#        new_artefact = Artefact(name = "Photo", path = "/main/photos",
#                                a_type = Type.photo)
#
#        System.do("upload_artefact", workshop = new_workshop,
#                  session = nc_session, artefact = new_artefact)
#        
#        System.do("delete_artefact", workshop = new_workshop,
#                  session = nc_session, artefact = new_artefact)
#        self.assertEqual(len(new_workshop.get("artefacts")), 0)
#        self.assertEqual(new_workshop.get("status").get("name") ,
#                         Status.pending_approval.get("name"))
#        
#

#if __name__ == '__main__':
#    unittest.main()
#
