
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import unittest
from flask_testing import TestCase
from runtime.rest.app import create_app
from runtime.system.system import *
from runtime.config.system_config import KEY
from runtime.utils.class_persistence_template import db

config = {
         'SQLALCHEMY_DATABASE_URI': ''
         }

def populate_db():
    pass
class TestAddLab(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_lab(self):
        print "test_add_lab_in_system_persistence"

        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']
        lab_cls = System.delegate.entities['lab']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        experiment_cls = System.delegate.entities['experiment']
        integration_status_cls = System.delegate.entities['integration_status']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                    overview=overview, sections=[],
                                    institute=inst, discipline=discipline,
                                        integration_status=integration_status, 
                                        assets=[asset], 
                                        developers=[dev], hosting_info=[host])
        experiment.save()
                                
        lab_name1="Computer Programming"
        lab_id1="CSE01"
        key = KEY
        overview = "overview"
        session = session_cls(key=key)
        name = "Theory"
        section = section_cls(name=name)
        section.save()

        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1,        
                          institute=inst, discipline=discipline, assets=[asset],                
                          overview=overview,  integration_status=integration_status, 
                          experiments=[experiment], sections=[section], developers=[dev], hosting_info=[host])

        lab1 = System.do("add_lab", lab=lab, session=session)
        new_lab = lab_cls.get_by_id(1)
        self.assertEqual(new_lab.get("lab_name"), lab_name1)
        self.assertEqual(new_lab.get("lab_id"), lab_id1)
            
class TestDeleteLab(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_lab(self):
        
        print "test_delete_lab_in_system_persistence"
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']
        lab_cls = System.delegate.entities['lab']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        experiment_cls = System.delegate.entities['experiment']
        integration_status_cls = System.delegate.entities['integration_status']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                    overview=overview, sections=[],
                                    institute=inst, discipline=discipline,
                                    integration_status=integration_status,
                                    assets=[asset], 
                                    developers=[dev], hosting_info=[host])

        experiment.save()

        lab_name1="Computer Programming"
        lab_id1="CSE01"
        key = KEY
        overview = "overview"
        session = session_cls(key=key)
        name="Theory"
        section = section_cls(name=name)
        section.save()

        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1, 
                      institute=inst, discipline=discipline, assets=[asset],
                      overview=overview, integration_status=integration_status, 
                      experiments=[experiment], developers=[dev],
                      hosting_info=[host], sections=[section])
        lab.save()
        lab_id = System.do("delete_lab", lab_id = lab_id1,
                                  session=session)

        self.assertEqual(lab_id, lab_id1)
            
class TestDeleteExperiment(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_exp(self):
        
        print "test_delete_exp_in_system_persistence"
        session_cls = System.delegate.entities['session']
        experiment_cls = System.delegate.entities['experiment']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']
        asset_type_cls = System.delegate.entities['asset_type']

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        key = KEY
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                        overview=overview, sections=[],
                                    institute=inst, discipline=discipline,
                                        integration_status=integration_status,
                                        assets=[asset],
                                        developers=[dev], hosting_info=[host])
        experiment.save()
        session = session_cls(key=key)
        exp_id1 = System.do("delete_experiment", exp_id = exp_id,
                                  session=session)

        self.assertEqual(exp_id1, exp_id)
            
class TestDeleteInstitute(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_institute(self):
        
        print "test_delete_institute_in_system_persistence"
        session_cls = System.delegate.entities['session']
        institute_cls = System.delegate.entities['institute']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name= "IIT Kanpur"
        institute_id= "IITK"
        key = KEY
        session = session_cls(key=key)
        institute = institute_cls(institute_id=institute_id, institute_name=institute_name, assets=[asset])
                         
        institute.save()
        institute = System.do("delete_institute", institute_id = institute_id,
                                  session=session)

        self.assertEqual(institute, institute_id)
            
class TestDeleteDiscipline(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_discipline(self):
        
        print "test_delete_discipline_in_system_persistence"
        session_cls = System.delegate.entities['session']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        
        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        discipline_name = "arrays"
        discipline_id = "cse02"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()
        key = KEY
        session = session_cls(key=key)

        discipline_id1 = System.do("delete_discipline", discipline_id = discipline_id,
                                  session=session)

        self.assertEqual(discipline_id, discipline_id1)
            
class TestDeleteHosting_Info(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_hosting_info(self):
        
        print "test_delete_hosting_info_in_system_persistence"
        session_cls = System.delegate.entities['session']
        hosting_info_cls = System.delegate.entities['hosting_info']

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        key = KEY
        session = session_cls(key=key)
        hosting_info = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
                         
        hosting_info.save()
        hosting_info = System.do("delete_hosting_info", hosted_url = hosted_url,
                                  session=session)

        self.assertEqual(hosting_info, hosted_url)
            
class TestAddExperiment(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_experiment(self):
        print "test_add_experiment_in_system_persistence"
        session_cls = System.delegate.entities['session']
        experiment_cls = System.delegate.entities['experiment']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                        overview=overview, sections=[],
                                        institute=inst, discipline=discipline,
                                        integration_status=integration_status,
                                        assets=[asset],
                                        developers=[dev], hosting_info=[host])

        key = KEY
        session = session_cls(key=key)
        experiment = System.do("add_experiment", experiment=experiment, \
                                session=session)
        experiment1 = experiment_cls.get_by_id(1)
        self.assertEqual(experiment1.get("exp_name"), exp_name)
            
class TestAddInstitute(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_institute(self):
        print "test_add_institute_in_system_persistence"
        session_cls = System.delegate.entities['session']
        institute_cls = System.delegate.entities['institute']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        institute = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
                                       
        key = KEY
        session = session_cls(key=key)
        institute = System.do("add_institute", institute=institute, \
                                session=session)
        institute1 = institute_cls.get_by_id(1)
        self.assertEqual(institute1.get("institute_name"), institute_name)
class TestAddDiscipline(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_discipline(self):
        print "test_add_discipline_in_system_persistence"
        session_cls = System.delegate.entities['session']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        discipline_name = "arrays"
        discipline_id = "cse02"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])

        key = KEY
        session = session_cls(key=key)
        discipline = System.do("add_discipline", discipline=discipline, session=session)
        discipline1 = discipline_cls.get_by_id(1)
        self.assertEqual(discipline1.get("discipline_name"), discipline_name)
            
class TestAddSection(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_section(self):
        
        print "test_add_section_in_system_persistence"
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']

        section = section_cls(name="Theory")
        session = session_cls(key=KEY)
        section = System.do("add_section", section=section, session=session)
        new_section = section_cls.get_by_id(1)
        self.assertEqual(new_section.get("name"), "Theory")
            
class TestAddName(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_name(self):
        
        print "test_add_name_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']

        name = name_cls(name="Prof. S. Dharmaraja")
        session = session_cls(key=KEY)
        name = System.do("add_name", name=name, session=session)
        new_name = name_cls.get_by_id(1)
        self.assertEqual(new_name.get("name"), "Prof. S. Dharmaraja")
            
class TestAddEmail(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_email(self):

        print "test_add_email_in_system_persistence"
        session_cls = System.delegate.entities['session']
        email_cls = System.delegate.entities['email']

        email = email_cls(email="dharmar@maths.iitd.ac.in")
        session = session_cls(key=KEY)
        email = System.do("add_email", email=email, session=session)
        new_email = email_cls.get_by_id(1)
        self.assertEqual(new_email.get("email"), "dharmar@maths.iitd.ac.in")

class TestAddDeveloper(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_developer(self):
        print "test_add_developer_in_system_persistence"
        session_cls = System.delegate.entities['session']
        developer_cls = System.delegate.entities['developer']
        email_cls = System.delegate.entities['email']
        name_cls = System.delegate.entities['name']

        name = name_cls(name="Prof. S. Dharmaraja")
        name.save()
        email = email_cls(email="dharmar@maths.iitd.ac.in")
        email.save()

        developer = developer_cls(name=name, email=email)
        key = KEY
        session = session_cls(key=key)

        developer = System.do("add_developer", developer=developer, session=session)

        self.assertEqual(developer.get("name").get("name"), name.get("name"))

class TestAddIntegration_Status(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_integration_status(self):
        print "test_add_integration_status_in_system_persistence"
        session_cls = System.delegate.entities['session']
        integration_status_cls = System.delegate.entities['integration_status']
        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
                                       
        key = KEY
        session = session_cls(key=key)
        integration_status = System.do("add_integration_status", integration_status=integration_status, \
                                session=session)
        integration_status1 = integration_status_cls.get_by_id(1)
        self.assertEqual(integration_status1.get("integration_level"), integration_level)
class TestUpdateLabt(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_lab(self):
        
        print "test_update_lab_in_system_persistence"
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']
        exp_cls = System.delegate.entities['experiment']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']
        institute_cls = System.delegate.entities['institute']
        experiment_cls = System.delegate.entities['experiment']
        discipline_cls = System.delegate.entities['discipline']
        lab_cls = System.delegate.entities['lab']

        session = session_cls(key=KEY)

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                     overview=overview, sections=[],
                                     institute=inst, discipline=discipline,
                                     integration_status=integration_status, 
                                     assets=[asset],
                                     developers=[dev], hosting_info=[host])
        experiment.save()

        lab_name = "Computer Programming"
        lab_id = "CSE01"
        overview = "overview"
        name = "Theory"
        section = section_cls(name=name)
        section.save()
        lab = lab_cls(lab_id=lab_id, lab_name=lab_name,        
                          institute=inst, discipline=discipline,
                          assets=[asset], overview=overview, 
                          integration_status=integration_status, 
                          experiments=[experiment], developers=[dev], 
                          hosting_info=[host], sections=[section])
        lab.save()

        lab_name1 = "two dimentional arrays"
        overview1 = "exp overview"

        asset_type1 = asset_type_cls(asset_type="Video")
        asset_type1.save()

        path1 = "vlabs.ac.in/images/video/icon.png"
        asset1 = asset_cls(asset_type=asset_type1, path=path1)
        asset1.save()

        institute_name1 = "IIT Kharagpur"
        institute_id1 = "IITKgp"
        inst1 = institute_cls(institute_name=institute_name1, institute_id=institute_id1, assets=[asset])
        inst1.save()

        discipline_name1 = "Computer Science & Engineering"
        discipline_id1 = "CSE02"
        discipline1 = discipline_cls(discipline_name=discipline_name1, discipline_id=discipline_id1, assets=[asset])
        discipline1.save()

        integration_level1 = 2
        integration_status1 = integration_status_cls(integration_level=integration_level1)
        integration_status1.save()

        dev_name1 = name_cls(name="pallavi pawar")
        dev_name1.save()
        email_id1 = email_cls(email="pallavi.pawar@gmail.com")
        email_id1.save()
        dev1 = developer_cls(name=dev_name1, email=email_id1)
        dev1.save()

        hosting_status1 = "hosted"
        hosted_url1 = "http://cse13-iiith.vlabs.ac.in"
        hosted_on1 = "cloud"
        host1 = hosting_info_cls(hosting_status=hosting_status1,
                                hosted_url=hosted_url1, hosted_on=hosted_on1)
        host1.save()

        exp_name1 = "Computer Programming"
        overview1 = "overveiw exp"
        exp_id1 = "cse03"
        experiment1 = experiment_cls(exp_name=exp_name1, exp_id=exp_id1,
                                     overview=overview1, sections=[],
                                     institute=inst1, discipline=discipline1,
                                     integration_status=integration_status1, 
                                     assets=[asset1],
                                     developers=[dev1], hosting_info=[host1])
        experiment1.save()
             
        dev_name1 = name_cls(name="Tahiliani")
        dev_name1.save()
        email_id1 = email_cls(email="tahiliani@gmail.com")
        email_id1.save()
        dev1 = developer_cls(name=dev_name1, email=email_id1)
        dev1.save()
 
        lab1 = System.do("update_lab", lab=lab, lab_name=lab_name1,
                             overview=overview1, institute=inst1,
                             discipline=discipline1, hosting_info=[host1],
                             integration_status=integration_status1,
                             session=session, developers=[dev1], 
                             assets=[asset1], sections=[section], experiments=[experiment1])

        new_lab = lab_cls.get_by_id(1)

        self.assertEqual(new_lab.get("lab_name"), lab_name1)
        self.assertEqual(new_lab.get("overview"), overview1)
        self.assertEqual(new_lab.get("lab_id"), lab_id)
        self.assertEqual(new_lab.get("institute").get("institute_id"), institute_id1)
        self.assertEqual(new_lab.get("discipline").get("discipline_id"), discipline_id1)
        self.assertEqual(new_lab.get("integration_status").
                             get("integration_level"), integration_level1)
        self.assertEqual(new_lab.get("hosting_info")[0].get("hosted_url"), 
                              hosted_url1)
        self.assertEqual(new_lab.get("developers")[0].get("email").get("email"), 
                              email_id1.get("email"))
        self.assertEqual(new_lab.get("assets")[0].get("path"), 
                              path1)
        self.assertEqual(new_lab.get("experiments")[0].get("exp_id"), 
                              experiment1.get("exp_id"))
                    
class TestUpdateExperiment(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_exp(self):
        
        print "test_update_exp_in_system_persistence"
        session_cls = System.delegate.entities['session']
        exp_cls = System.delegate.entities['experiment']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']
        institute_cls = System.delegate.entities['institute']
        experiment_cls = System.delegate.entities['experiment']
        discipline_cls = System.delegate.entities['discipline']
        lab_cls = System.delegate.entities['lab']
        section_cls = System.delegate.entities['section']

        session = session_cls(key=KEY)

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id,\
                                 assets=[asset])
        inst.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=\
                                                        integration_level)
        integration_status.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status,
                                    hosted_url=hosted_url,
                                    hosted_on=hosted_on)
        host.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name,
                                        discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        name = "Theory"
        section = section_cls(name=name)
        section.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                     overview=overview, sections=[section],
                                     institute=inst, discipline=discipline,
                                     integration_status=integration_status, 
                                     assets=[asset],developers=[dev],
                                     hosting_info=[host])
        experiment.save()

        exp_name1 = "Computer Programming"
        overview1 = "overveiw exp"

        asset_type1 = asset_type_cls(asset_type="Video")
        asset_type1.save()

        path1 = "vlabs.ac.in/images/video/icon.png"
        asset1 = asset_cls(asset_type=asset_type1, path=path1)
        asset1.save()
        
        institute_name1 = "IIT Kharagpur"
        institute_id1 = "IITKgp"
        inst1 = institute_cls(institute_name=institute_name1, institute_id=institute_id1,
                                  assets=[asset1])
        inst1.save()
        
        discipline_name1 = "electronics and communication"
        discipline_id1 = "ece"
        discipline1 = discipline_cls(discipline_name=discipline_name1,
                                         discipline_id=discipline_id1, assets=[asset1])
        discipline1.save()
        
        dev_name1 = name_cls(name="Palavi Pawar")
        dev_name1.save()
        email_id1 = email_cls(email="pallavipawar@gmail.com")
        email_id1.save()
        dev1 = developer_cls(name=dev_name1, email=email_id1)
        dev1.save()
        
        integration_level1 = 3
        integration_status1 = integration_status_cls(integration_level=\
                                                         integration_level1)
        integration_status1.save()

        hosting_status1 = "hosted"
        hosted_url1 = "http://cse13-iiith.vlabs.ac.in"
        hosted_on1 = "cloud"
        host1 = hosting_info_cls(hosting_status=hosting_status1,
                                hosted_url=hosted_url1,
                                     hosted_on=hosted_on1)
        host1.save()

        key = KEY
        session = session_cls(key=key)

        name1 = "Procedure"
        section1 = section_cls(name=name1)
        section1.save()
        
        exp2 = System.do("update_experiment", exp_name=exp_name1,
                            overview=overview1, institute=inst1, 
                            session=session, discipline=discipline1,
                            integration_status=integration_status1, 
                            sections=[section1], 
                            hosting_info=[host1], experiment=experiment, 
                            developers=[dev1], assets=[asset1])
        exp2 = exp_cls.get_by_id(1)
        
        self.assertEqual(exp2.get("exp_name"), exp_name1)
        self.assertEqual(exp2.get("overview"), overview1)
        self.assertEqual(exp2.get("exp_id"), exp_id)
        self.assertEqual(exp2.get("institute").get("institute_id"), 
                                    inst1.get("institute_id"))
        self.assertEqual(exp2.get("discipline").get("discipline_id"), 
                                    discipline1.get("discipline_id"))
        self.assertEqual(exp2.get("integration_status").\
                             get("integration_level"),
                             integration_status1.get("integration_level"))
        self.assertEqual(exp2.get("hosting_info")[0].get("hosted_url"), 
                              hosted_url1)
        self.assertEqual(exp2.get("developers")[0].get("email").get("email"), 
                              email_id1.get("email"))
        self.assertEqual(exp2.get("assets")[0].get("path"), path1)
        self.assertEqual(exp2.get("sections")[0].get("name"), name1)
   
            
class TestUpdateDeveloper(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_developer(self):

        print "test_update_exp_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        dev_cls = System.delegate.entities['developer']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        session = session_cls(key=KEY)

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()     

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Prof. Dharmaraja")
        dev_name.save()
        email_id = email_cls(email="raja@gmail.com")
        email_id.save()
        developer = dev_cls(name=dev_name, email=email_id)
        developer.save()

        institute_name1 = "IIT Kharagpur"
        institute_id1 = "IITKgp"
        inst1 = institute_cls(institute_name=institute_name1, institute_id=institute_id1, assets=[asset])
        inst1.save()

        discipline_name1 = "Computer Science & Engineering"
        discipline_id1 = "CSE02"
        discipline1 = discipline_cls(discipline_name=discipline_name1, discipline_id=discipline_id1, assets=[asset])
        discipline1.save()

        dev_name2 = name_cls(name="Prof. Raja")
        dev_name2.save()

        dev1 = System.do("update_developer", developer=developer,
                         name=dev_name2, session=session)

        new_dev = dev_cls.get_by_id(1)

        self.assertEqual(new_dev.get("name").get("name"),
                             dev_name2.get('name'))

class TestDeleteName(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_name(self):
        print "test_delete_name_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']

        name = "Prof. Dharmaraj"
        key = KEY
        session = session_cls(key=key)
        name1 = name_cls(name=name)
        name1.save()

        name2 = "Prof. Raja"
        name3 = name_cls(name=name2)
        name3.save()
        name4 = System.do("delete_name", n_id=1, session=session)

        self.assertEqual(len(name_cls.get_all()), 1)

class TestDeleteEmail(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_email(self):

        print "test_delete_email_in_system_persistence"
        session_cls = System.delegate.entities['session']
        email_cls = System.delegate.entities['email']

        email = "abc@gmail.com"
        key = KEY
        session = session_cls(key=key)
        email1 = email_cls(email=email)

        email1.save()
        email2 = System.do("delete_email", email = email1, session=session)

        self.assertEqual(email1.get("email"), email2.get("email"))
class TestDeleteDeveloper(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_developer(self):

        print "test_delete_name_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Prof. Dharmaraj")
        dev_name.save()

        email_id = email_cls(email="abc@gmail.com")
        email_id.save()

        key = KEY
        session = session_cls(key=key)
        developer = developer_cls(name=dev_name, email=email_id)
        developer.save()

        email = System.do("delete_developer", email=email_id, session=session)

        self.assertEqual(email.get("email"), email_id.get("email"))

class TestDeleteIntegration_Status(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_integration_status(self):
        
        print "test_delete_integration_status_in_system_persistence"
        session_cls = System.delegate.entities['session']
        integration_status_cls = System.delegate.entities['integration_status']

        integration_level= 4
        key = KEY
        session = session_cls(key=key)
        integration_status = integration_status_cls(integration_level=integration_level)
                         
        integration_status.save()
        integration_status = System.do("delete_integration_status", integration_level = integration_level,
                                  session=session)

        self.assertEqual(integration_status, integration_level)
            
class TestAddHosting_Info(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_hosting_info(self):
        print "test_add_hosting_info_in_system_persistence"
        session_cls = System.delegate.entities['session']
        hosting_info_cls = System.delegate.entities['hosting_info']
        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        hosting_info = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
                                       
        key = KEY
        session = session_cls(key=key)
        hosting_info = System.do("add_hosting_info", hosting_info=hosting_info, \
                                session=session)
        hosting_info1 = hosting_info_cls.get_by_id(1)
        self.assertEqual(hosting_info1.get("hosting_status"), hosting_status)
        self.assertEqual(hosting_info1.get("hosted_on"), hosted_on)

class TestUpdateInstitute(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_institute(self):

        print "test_update_institute_in_system_persistence"
        session_cls = System.delegate.entities['session']
        institute_cls = System.delegate.entities['institute']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type1 = asset_type_cls(asset_type="Image")
        asset_type1.save()

        path1 = "vlabs.ac.in/images/static/logo.png"
        asset1 = asset_cls(asset_type=asset_type1, path=path1)
        asset1.save()

        institute_name1="IIT Kanpur"
        institute_id1="IITK"
        key = KEY
        session = session_cls(key=key)
        institute = institute_cls(institute_id=institute_id1, institute_name=institute_name1, assets=[asset1])

        institute.save()

        asset_type1 = asset_type_cls(asset_type="Video")
        asset_type1.save()

        path1 = "vlabs.ac.in/images/video/icon.png"
        asset1 = asset_cls(asset_type=asset_type1, path=path1)
        asset1.save()

        institute_name2="IIT Kharagpur"

        institute1 = System.do("update_institute", institute_name=institute_name2,
                                 institute=institute, assets=[asset1], session=session)

        new_institute = institute_cls.get_by_id(1)

        self.assertEqual(new_institute.get("institute_name"), institute_name2)
        self.assertEqual(new_institute.get("assets")[0].get("path"),
                              asset1.get("path"))

class TestUpdateDisciplilne(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_discipline(self):

        print "test_update_discipline_in_system_persistence"
        session_cls = System.delegate.entities['session']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
    
        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        discipline_name = "arrays"
        discipline_id = "cse02"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()
        key = KEY
        session = session_cls(key=key)

        asset_type1 = asset_type_cls(asset_type="Video")
        asset_type1.save()
        path1 = "vlabs.ac.in/images/video/icon.png"
        asset1 = asset_cls(asset_type=asset_type1, path=path1)
        asset1.save()

        discipline_name1 = "lists"

        discipline1 = System.do("update_discipline", discipline_name=discipline_name1,
                                  discipline=discipline, assets=[asset1], session=session)

        self.assertEqual(discipline1.get("discipline_name"), discipline_name1)
        self.assertEqual(discipline1.get("assets")[0].get("path"),
                              asset1.get("path"))

class TestUpdateHosting_Info(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_hosting_info(self):

        print "test_update_hosting_info_in_system_persistence"
        session_cls = System.delegate.entities['session']
        hosting_info_cls = System.delegate.entities['hosting_info']

        hosting_status1 = "hosted"
        hosted_url1 = "http://cse14-iiith.vlabs.ac.in"
        hosted_on1 = "cloud"
        key = KEY
        session = session_cls(key=key)
        hosting_info = hosting_info_cls(hosting_status=hosting_status1, hosted_url=hosted_url1, hosted_on=hosted_on1)

        hosting_info.save()

        hosting_status2 ="not hosted"
        hosted_on2 = "server"
        hosting_info1 = System.do("update_hosting_info", hosting_status=hosting_status2, hosted_on=hosted_on2,
                                 hosting_info=hosting_info, session=session)

        new_hosting_info = hosting_info_cls.get_by_id(1)

        self.assertEqual(new_hosting_info.get("hosting_status"), hosting_status2)
        self.assertEqual(new_hosting_info.get("hosted_on"), hosted_on2)

class TestAddSectionsToExperiment(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_sections_to_experiment(self):
        print "test_add_sections_to_experiment_in_system_persistence"
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']
        experiment_cls = System.delegate.entities['experiment']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()
     
        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                    overview=overview, sections=[],
                                    institute=inst, discipline=discipline,
                                    integration_status=integration_status, 
                                    assets=[asset],
                                    developers=[dev], hosting_info=[host])

        key = KEY
        session = session_cls(key=key)
        experiment = System.do("add_experiment", experiment=experiment, \
                                session=session)
        experiment1 = experiment_cls.get_by_id(1)

        section1 = section_cls(name="Theory")
        section1.save()

        section2 = section_cls(name="Aim")
        section2.save()
        
        experiment = System.do("add_sections_to_experiment", 
                                experiment=experiment,
                                sections=[section1, section2],
                                session=session)

        self.assertEqual(experiment1.get("exp_name"), exp_name)
        self.assertEqual(experiment1.get("sections")[0].get("name"), "Theory")
        self.assertEqual(experiment1.get("sections")[1].get("name"), "Aim")            

class TestGetLab(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_lab(self):

        print "test_get_lab_in_system_persistence"
        lab_cls = System.delegate.entities['lab']
        institute_cls = System.delegate.entities['institute']
        integration_status_cls = System.delegate.entities['integration_status']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        section_cls = System.delegate.entities['section']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']
        asset_type_cls = System.delegate.entities['asset_type']

        lab_name1="Computer Programming"
        lab_id1="CSE01"
        overview = "overview"

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status,
                                   hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        name="Theory"
        section = section_cls(name=name)
        section.save()

        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1,
                          institute=inst, discipline=discipline, assets=[asset],
                          overview=overview, experiments=[], developers=[dev], 
                          hosting_info=[host], sections=[section], integration_status=integration_status)

        lab.save()

        lab1 = System.do("get_lab", lab_id=lab_id1)


        self.assertEqual(lab1.get("lab_name"), lab_name1)
        self.assertEqual(lab1.get("lab_id"), lab_id1)
            
class TestGetName(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_name(self):

        print "test_get_name_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']

        name1="Prof. Dharmaraj"
        key = KEY
        session = session_cls(key=key)
        name = name_cls(name=name1)

        name.save()

        name2 = System.do("get_name", name=name, session=session)

        self.assertEqual(name2.get("name"), name1)
class TestGetEmail(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_email(self):

        print "test_get_email_in_system_persistence"
        session_cls = System.delegate.entities['session']
        email_cls = System.delegate.entities['email']

        email1="abc@gmail.com"
        key = KEY
        session = session_cls(key=key)
        email = email_cls(email=email1)

        email.save()

        email2 = System.do("get_email", email=email, session=session)

        self.assertEqual(email2.get("email"), email1)

class TestGetDeveloper(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_developer(self):

        print "test_get_developer_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        dev_cls = System.delegate.entities['developer']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name1 = name_cls(name="Prof. Dharmaraj")
        dev_name1.save()
        email_id1 = email_cls(email="abc@gmail.com")
        email_id1.save()
        key = KEY
        session = session_cls(key=key)
        developer = dev_cls(name=dev_name1, email=email_id1)
        developer.save()
        developer1 = System.do("get_developer", email=email_id1)

        self.assertEqual(developer1.get("name"), dev_name1)
        self.assertEqual(developer1.get("email"), email_id1)

class TestGetInstitute(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_institute(self):

        print "test_get_institute_in_system_persistence"
        session_cls = System.delegate.entities['session']
        institute_cls = System.delegate.entities['institute']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        
        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name1= "IIT Kanpur"
        institute_id1= "IITK"
        institute = institute_cls(institute_id=institute_id1, institute_name=institute_name1, assets=[asset])
        institute.save()

        institute1 = System.do("get_institute", institute_id=institute_id1)

        self.assertEqual(institute1.get("institute_name"), institute_name1)
        self.assertEqual(institute1.get("institute_id"), institute_id1)
            
class TestGetExp(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_exp(self):

        print "test_get_exp_in_system_persistence"
        exp_cls = System.delegate.entities['experiment']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']
        experiment_cls = System.delegate.entities['experiment']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        exp_name = "arrays"
        exp_id = "cse02"
        overview = "overview"
        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
                                    overview=overview, sections=[],
                                    institute=inst, discipline=discipline,
                                    integration_status=integration_status, 
                                    assets=[asset],
                                    developers=[dev], hosting_info=[host])

        experiment.save()

        experiment1 = System.do("get_experiment", exp_id=exp_id)

        self.assertEqual(experiment1.get("exp_name"), exp_name)
        self.assertEqual(experiment1.get("exp_id"), exp_id)
            
class TestGetDiscipline(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_discipline(self):

        print "test_get_discipline_in_system_persistence"
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        discipline_name = "arrays"
        discipline_id = "cse02"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        exp1 = System.do("get_discipline", discipline_id=discipline_id)

        self.assertEqual(exp1.get("discipline_name"), discipline_name)
        self.assertEqual(exp1.get("discipline_id"), discipline_id)
            
class TestGetHosting_Info(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_hosting_info(self):

        print "test_get_hosting_info_in_system_persistence"
        session_cls = System.delegate.entities['session']
        hosting_info_cls = System.delegate.entities['hosting_info']

        hosting_status1 = "hosted"
        hosted_url1 = "http://cse14-iiith.vlabs.ac.in"
        hosted_on1 = "cloud"
        hosting_info = hosting_info_cls(hosting_status=hosting_status1, hosted_url=hosted_url1, hosted_on=hosted_on1)
        hosting_info.save()

        hosting_info1 = System.do("get_hosting_info", hosted_url=hosted_url1)

        self.assertEqual(hosting_info1.get("hosting_status"), hosting_status1)
        self.assertEqual(hosting_info1.get("hosted_url"), hosted_url1)
        self.assertEqual(hosting_info1.get("hosted_on"), hosted_on1)
            
class TestGetIntegration_Status(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_integration_status(self):

        print "test_get_integration_status_in_system_persistence"
        session_cls = System.delegate.entities['session']
        integration_status_cls = System.delegate.entities['integration_status']

        integration_level1= 4
        integration_status = integration_status_cls(integration_level=integration_level1)
        integration_status.save()

        integration_status1 = System.do("get_integration_status", integration_level=integration_level1)

        self.assertEqual(integration_status1.get("integration_level"), integration_level1)
            
class TestUpdateAsset(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_asset(self):
        print "test_update_asset_in_system_persistence"
        session_cls = System.delegate.entities['session']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        key = KEY
        session = session_cls(key=key)
        asset_type1 = asset_type_cls(asset_type="Icon")
        asset_type1.save()

        path1 = "vlabs.ac.in/static/images/icon.png"
        asset = asset_cls(asset_type=asset_type1, path=path1)
        asset.save()

        asset_type2 = asset_type_cls(asset_type="Video")

        asset1 = System.do("update_asset", asset_type=asset_type2,
                             asset=asset, session=session)

        new_asset = asset_cls.get_by_id(1)

        self.assertEqual(new_asset.get("asset_type"), asset_type2)
        
#class TestAddAssetsToLab(TestCase):
#    TESTING = True
#
#    def create_app(self):
#        app = create_app(config)
#        return app
#
#    def setUp(self):
#        db.create_all()
#
#    def tearDown(self):
#        db.session.remove()
#        db.drop_all()
#
#    def test_add_assets_to_lab(self):
#        print "test_add_assets_to_lab_in_system_persistence"
#
#        session_cls = System.delegate.entities['session']
#        section_cls = System.delegate.entities['section']
#        lab_cls = System.delegate.entities['lab']
#        institute_cls = System.delegate.entities['institute']
#        discipline_cls = System.delegate.entities['discipline']
#        asset_cls = System.delegate.entities['asset']
#        asset_type_cls = System.delegate.entities['asset_type']
#        experiment_cls = System.delegate.entities['experiment']
#        integration_status_cls = System.delegate.entities['integration_status']
#               
#        integration_level = 4
#        integration_status = integration_status_cls(integration_level=integration_level)
#        integration_status.save()
#
#        asset_type = asset_type_cls(asset_type="Image")
#        asset_type.save()
#
#        path = "vlabs.ac.in/images/static/logo.png"
#        asset = asset_cls(asset_type=asset_type, path=path)
#        asset.save()
#
#        institute_name = "IIT Kanpur"
#        institute_id = "IITK"
#        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
#        inst.save()
#
#        discipline_name = "IIT Kanpur"
#        discipline_id = "IITK"
#        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
#        discipline.save()
#
#        exp_name = "arrays"
#        exp_id = "cse02"
#        overview = "overview"
#        experiment = experiment_cls(exp_name=exp_name, exp_id=exp_id,
#                                        overview=overview, sections=[],
#                                    institute=inst, discipline=discipline)
#        experiment.save()
#                                
#        lab_name1="Computer Programming"
#        lab_id1="CSE01"
#        key = KEY
#        overview = "overview"
#        session = session_cls(key=key)
#        name="Theory"
#        section = section_cls(name=name)
#        section.save()
#        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1,        
#                          institute=inst, discipline=discipline, assets=[asset],                
#                          overview=overview, sections=[section], integration_status=integration_status, 
#                          experiments=[experiment])
#        lab.save()
#
#        asset1 = asset_cls(asset_type="Image", path="vlabs.ac.in/static/images/icon.png")
#        asset1.save()
#
#        asset2 = asset_cls(asset_type="Video", path="vlabs.ac.in/static/images/logo.png")
#        asset2.save()
#        
#        lab1 = System.do("add_assets_to_lab", 
#                                lab=lab,
#                                assets=[asset1, asset2],
#                                session=session)
#
#        self.assertEqual(lab1.get("lab_name"), lab_name1)
#        self.assertEqual(lab1.get("assets")[0].get("asset_type"), "Image")
#        self.assertEqual(lab1.get("assets")[1].get("asset_type"), "Video")            
#
class TestGetAsset(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_asset(self):
    
        print "test_get_asset_in_system_persistence"
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        session_cls = System.delegate.entities['session']

        asset_type = asset_type_cls(asset_type="Video")
        asset_type.save()

        path = "vlabs.ac.in/static/images/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        asset1 = System.do("get_asset", path=path)

        self.assertEqual(asset1.get("asset_type"), asset_type)
        self.assertEqual(asset1.get("path"), path)
            
class TestDeleteAsset(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_asst(self):
        
        print "test_delete_asst_in_system_persistence"
        session_cls = System.delegate.entities['session']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in.static/images/logo.png"
        key = KEY
        asset = asset_cls(asset_type=asset_type, path=path)

        asset.save()
        session = session_cls(key=key)
        asset = System.do("delete_asset", path=path,
                                  session=session)

        self.assertEqual(asset, path)
            
class TestAddAsset(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_asset(self):
        print "test_add_asset_in_system_persistence"
        session_cls = System.delegate.entities['session']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/static/images/logo.png"
        asset = asset_cls(path=path, asset_type=asset_type)
        key = KEY
        session = session_cls(key=key)
        asset = System.do("add_asset", asset=asset, \
                                session=session)
        asset1 = asset_cls.get_by_id(1)
        self.assertEqual(asset1.get("asset_type"), asset_type)
            
class TestGetLabByInstitute(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_institute(self):

        print "test_get_labs_by_institute_in_system_persistence"
        lab_cls = System.delegate.entities['lab']
        section_cls = System.delegate.entities['section']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']
        asset_type_cls = System.delegate.entities['asset_type']

        lab_name1="Computer Programming"
        lab_id1="CSE01"
        overview = "overview"

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        discipline_name = "Computer Science"
        discipline_id = "CS"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()
        name = "Theory"
        section = section_cls(name=name)
        section.save()
        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1,
                          institute=inst, discipline=discipline, sections=[section], assets=[asset],
                          overview=overview, experiments=[], integration_status=integration_status, 
                          hosting_info=[host], developers=[dev])

        lab.save()

        labs = System.do("get_labs_by_institute", institute=inst)

        self.assertEqual(labs[0].get("institute").get("institute_name"), institute_name)
            
class TestGetLabByLabName(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_lab_name(self):

        print "test_get_labs_by_lab_name_in_system_persistence"
        lab_cls = System.delegate.entities['lab']
        section_cls = System.delegate.entities['section']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']

        lab_name1="Computer Programming"
        lab_id1="CSE01"
        overview = "overview"

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        discipline_name = "computer science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status,
                                   hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()
        name = "Theory"
        section = section_cls(name=name)
        section.save()
        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1, 
                          integration_status=integration_status,
                          institute=inst, discipline=discipline, sections=[section],
                          hosting_info=[host], assets=[asset],
                          overview=overview, experiments=[], developers=[dev])


        lab.save()

        labs = System.do("get_labs_by_lab_name", lab_name=lab_name1)

        self.assertEqual(labs[0].get("lab_name"), lab_name1)
            
class TestGetLabByDiscipline(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_discipline(self):

        print "test_get_labs_by_discipline_in_system_persistence"
        lab_cls = System.delegate.entities['lab']
        section_cls = System.delegate.entities['section']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        integration_status_cls = System.delegate.entities['integration_status']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        hosting_info_cls = System.delegate.entities['hosting_info']

        lab_name1="Computer Programming"
        lab_id1="CSE01"
        overview = "overview"

        asset_type = asset_type_cls(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = asset_cls(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = institute_cls(institute_name=institute_name, institute_id=institute_id, assets=[asset])
        inst.save()

        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
        integration_status.save()

        discipline_name = "Computer Science"
        discipline_id = "cse"
        discipline = discipline_cls(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
        discipline.save()

        dev_name = name_cls(name="Mohit Tahiliani")
        dev_name.save()
        email_id = email_cls(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = developer_cls(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = hosting_info_cls(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()
        name="Theory"
        section=section_cls(name=name)
        section.save()
        lab = lab_cls(lab_id=lab_id1, lab_name=lab_name1,
                          institute=inst, discipline=discipline, sections=[section],
                          hosting_info=[host], assets=[asset],
                          overview=overview, experiments=[], developers=[dev], 
                          integration_status=integration_status)


        lab.save()

        labs = System.do("get_labs_by_discipline", discipline=discipline)

        self.assertEqual(labs[0].get("discipline").get("discipline_name"), discipline_name)
            
class TestGetIntegration_StatusByIL(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_integration_status_by_IL(self):
        print "test_get_integration_status_by_IL_in_system_persistence"
        session_cls = System.delegate.entities['session']
        integration_status_cls = System.delegate.entities['integration_status']
        integration_level = 4
        integration_status = integration_status_cls(integration_level=integration_level)
                                       
        key = KEY
        session = session_cls(key=key)
        integration_status = System.do("add_integration_status", integration_status=integration_status, \
                                session=session)

        integration_status = System.do("get_integration_status_by_IL", 
                                        integration_level=integration_level)

        self.assertEqual(integration_status.get("integration_level"), integration_level)
            
class TestUpdateName(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_name(self):
        
        print "test_update_name_in_system_persistence"
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']

            
class TestDeleteSection(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_section(self):
        print "test_delete_section_in_system_persistence"
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']

        name = "theory"
        key = KEY
        session = session_cls(key=key)
        section1 = section_cls(name=name)
        section1.save()

        name1 = "procedure"
        section2 = section_cls(name=name1)
        section2.save()
        section3 = System.do("delete_section", s_id=1, session=session)

        self.assertEqual(len(section_cls.get_all()), 1)

if __name__ == '__main__':
    unittest.main()
