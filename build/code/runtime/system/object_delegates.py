
# -*- coding: utf-8 -*-
from runtime.objects.entities import *
from runtime.config.config import Config
from runtime.exceptions.custom_exceptions import *
import datetime

#+NAME: class_object_delegate
#+BEGIN_SRC python
class ObjectDelegate():
    def __init__(self):
        self.role_set = []
        self.user_set = []
        self.active_user_set = []
        self.institute_set = []
        self.oc_set = []
        self.nc_set = []
        self.workshop_set = []
        self.artefact_set = []
        self.role_set = self.initialize_role_set()
        self.user_set = self.initialize_user_set()

#+END_SRC


#+NAME: initialize_object_role_set
#+begin_src python
    def initialize_role_set(self):
        Role_admin = Role(name="admin", centre_oc=None, centre_nc=None)
        Role_guest = Role(name="guest", centre_oc=None, centre_nc=None)
        Role_noc = Role(name="noc", centre_oc=None, centre_nc=None)
        Role_reviewer = Role(name="reviewer", centre_oc=None, centre_nc=None)                
        self.role_set = [Role.admin, Role.guest, Role.noc, Role.reviewer]
        return self.role_set

#+end_src


#+NAME: initialize_object_user_set
#+begin_src python

    def initialize_user_set(self):

        admin_user = User(name=Name(name=Config.admin_name),
                          email=Email(email=Config.admin_email),
                          roles=[Role.admin, Role.guest], user_status="active")
        self.user_set = [admin_user]
        return self.user_set

#+end_src

  :PROPERTIES:
  :CUSTOM_ID: test_initialize_object_delegate
  :END: 

    Check if =user= already exists
    This function checks if a user is already in the user-set of the =System=.
#+NAME: user_exists
#+BEGIN_SRC python
    def user_exists(self, user):
        active_users = self.get_active_users()
        if user in active_users:
            return True
        else:
            return False

#+END_SRC

**** Tests
#+NAME: test_user_exists
#+BEGIN_SRC python
    def test_user_exists(self):
         print "test_user_exists"
         user = self.obj_delegate.user_set[0]
         self.assertEqual(self.obj_delegate.user_exists(user), True)

#+END_SRC


    Add a user to the system
    This function adds a user to the user-set maintained by the system.
#+NAME: add_user
#+BEGIN_SRC python
    def add_user(self, user):
        self.user_set.append(user)
        return user

#+END_SRC

**** Tests
#+NAME: test_add_user
#+BEGIN_SRC python
    def test_add_user(self):
        print "test_add_user"
        user = User(name=Name(name="some user"),
                        email=Email(email="tt@kk.com"),
                        roles=[Role.admin], user_status="active")
        user = self.obj_delegate.add_user(user)
        self.assertEqual(self.obj_delegate.user_exists(user), True)

#+END_SRC


#+NAME: update_user
#+BEGIN_SRC python 
    def update_user(self, name, email, user):
        user.set(name=name)
        user.set(email=email)
        return user

#+END_SRC
**** Tests
#+NAME: test_update_user
#+BEGIN_SRC python

    def test_update_user(self):
        print "test_update_user"
        name=Name(name="test")
        email=Email(email="test@gmail.com")
        user = User(name=name, email=email, roles= [Role.guest],
                user_status="active")
        user = self.obj_delegate.add_user(user)
        user_name1=Name(name="alaska")
        user_email1=Email(email="alaska@gmail.com")
        user = self.obj_delegate.update_user(user_name1, user_email1, user)
        self.assertEqual(user.get("name").get("name"), "alaska")
        
#+END_SRC

    def delete_user(self, user):
        user.set(user_status="inactive")
        return user

#+NAME: add_role_to_user
#+BEGIN_SRC python 
    def add_role_to_user(self, user, role):
        user.append_role(role)
        return user
#+END_SRC
**** Tests
#+NAME: test_add_role_to_user
#+BEGIN_SRC python
    def test_add_role_to_user(self):
        print "test_add_role_to_user"
        name = Name(name="test")
        email = Email(email="test@gmail.com")
        user = User(name=name, email=email, roles= [Role.guest],
                user_status="active")
        new_user = self.obj_delegate.add_user(user)
        user_with_new_role = self.obj_delegate.add_role_to_user(new_user, Role.noc)
        self.assertTrue(len(user_with_new_role.get('roles'))==2)
#+END_SRC


    This return the user_set maintained by the system.
#+NAME: get_users
#+BEGIN_SRC python
    def get_users(self):
        return self.get_active_users()

#+END_SRC
**** Tests
#+NAME: test_get_users
#+BEGIN_SRC python
    def test_get_users(self):
         print "test_get_users"
         self.assertEqual(len(self.obj_delegate.get_users()), 1)

#+END_SRC


    Check if =role= already exists
    This function checks if a user is already in the role-set of the =System=.
#+NAME: role_exists
#+BEGIN_SRC python
    def role_exists(self, role):
        if role in self.role_set:
            return True
        else:
            return False

#+END_SRC

**** Tests
#+NAME: test_role_exists
#+BEGIN_SRC python
    def test_role_exists(self):
         print "test_role_exists"
         role = self.obj_delegate.role_set[0]
         self.assertEqual(self.obj_delegate.role_exists(role), True)

#+END_SRC

    def add_role(self, role):
        self.role_set.append(role)
        return role

    def get_roles(self):
        return self.role_set

    def institute_exists(self, institute):
        if institute in self.institute_set:
            return True
        else:
            return False

    def add_institute(self, institute):
        self.institute_set.append(institute)
        return institute

    def update_institute(self, institute, name, address):
        institute.set(name=name)
        institute.set(address=address)
        return institute
    def get_institutes(self):
        return self.institute_set

    def oc_exists(self, oc):
        if oc in self.oc_set:
            return True
        else:
            return False

    def add_occ_role(self, name, new_oc, centre_nc):
        self.role = Role(name=name,centre_oc=new_oc,centre_nc=centre_nc)
        self.role_set.append(self.role)
        return self.role
    def add_ncc_role(self, name, centre_oc, new_nc):
        self.role = Role(name=name,centre_oc=centre_oc,centre_nc=new_nc)
        self.role_set.append(self.role)
        return self.role
    def add_oc(self, institute, spokes, oc_target):
        self.new_oc = OC(institute=institute, spokes=spokes, oc_target = oc_target)
        self.oc_set.append(self.new_oc)
        return self.new_oc
    def get_ocs(self):
        return self.oc_set

    def nc_exists(self, nc):
        if nc in self.nc_set:
            return True
        else:
            return False

    def add_nc(self, institute, oc, nc_target, workshops):
        self.new_nc = NC(institute=institute, hub=oc, nc_target=nc_target,
                         workshops=workshops)
        oc.append_spoke(self.new_nc)
        self.nc_set.append(self.new_nc)
        return self.new_nc
    def get_ncs(self):
        return self.nc_set

    def workshop_exists(self, workshop):
        if workshop in self.workshop_set:
            return True
        else:
            return False

    def add_workshop(self, institute, name, ws_target, artefacts, status, nc):
        new_workshop = Workshop(institute = institute,
                                name = name,
                                ws_target = ws_target,
                                artefacts = artefacts,
                                status = status,
                                nc = nc,
                                a_date = None,
                                a_participants = 0,
                                a_experiments = 0,
                                a_usage = 0)
        self.workshop_set.append(new_workshop)
        return new_workshop

    def cancel_workshop(self, workshop):
        workshop.set(status = Status.cancelled)
        return workshop
    def reschedule_workshop(self, workshop, wstarget):
        workshop.set(status = Status.pending)
        workshop.set(ws_target = wstarget)
        return workshop

    def conduct_workshop(self, workshop):
        workshop.set(status = Status.completed)
        return workshop
    def upload_artefact(self, workshop, new_artefact):
        artefacts = workshop.get("artefacts")
        artefacts.append(new_artefact)
        workshop.set(artefacts = artefacts)
        workshop.set(status = Status.pending_approval)
        return workshop
    def approve_workshop(self, workshop):
        workshop.set(status = Status.approved)
        return workshop
    def reject_workshop(self, workshop):
        workshop.set(status = Status.rejected)
        return workshop
    def delete_artefact(self, workshop, artefact):
        artefact_set = workshop.get("artefacts")
        new_set = filter(lambda art: not art.get("name") ==
                         artefact.get("name"), artefact_set)

        workshop.set(artefacts = new_set)
        workshop.set(status = Status.pending_approval)
        return workshop
    def get_artefacts_of_a_workshop(self, workshop):
        self.artefact_set = workshop.get("artefacts")
        return self.artefact_set     
    def get_artefacts(self):
        return self.artefact_set

    def get_workshops(self):
        return self.workshop_set

    def get_active_users(self): 
        active_user_set = filter(lambda x: x.get("user_status")=="active",
                                self.user_set)
        return active_user_set
