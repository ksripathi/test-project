
# -*- coding: utf-8 -*-
import unittest
from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError
from runtime.persistence.entities import *
#from flask <
#import create_app
from runtime.rest.app import create_app

config = {
    'SQLALCHEMY_DATABASE_URI': ''
}

class TestPersistenceExperiment(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_experiment(self):
        print "test_persistance_experiment"

        asset_type1 = AssetType(asset_type="video")
        asset_type1.save()

        path = "vlabs.ac.in/static/images/logo.png"

        asset = Asset(path=path, asset_type=asset_type1)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = Institute(institute_name=institute_name,
                             institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = Discipline(discipline_name=discipline_name,
                                    discipline_id=discipline_id,
                                    assets=[asset])
        discipline.save()      

        dev_name = Name(name="Mohit Tahiliani")
        dev_name.save()
        email_id = Email(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = Developer(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = HostingInfo(hosting_status=hosting_status,
                               hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        exp_name = "Number Systems"
        exp_id = "EE99777"
        overview = "This is linked list experiment"

        integration_level = 4
        intstatus = IntegrationStatus(integration_level=integration_level)
        intstatus.save()

        exp = Experiment(exp_name=exp_name, exp_id=exp_id, overview=overview,
                          integration_status=intstatus, assets=[asset], 
                         sections=[], developers=[dev], hosting_info=[host],  
                         institute=inst, discipline=discipline)
        exp.save()

        experiment = Experiment.get_by_id(1)
        experiment1 = Experiment.get_by_id(2)
        self.assertEqual(experiment.get("exp_name"), exp_name)
        self.assertEqual(experiment.get("exp_id"), exp_id)
        self.assertEqual(experiment.get("overview"), overview)
        self.assertEqual(experiment.get("institute").get("institute_name"), 
                             inst.get("institute_name"))
        self.assertEqual(experiment.get("discipline").get("discipline_name"), 
                             discipline.get("discipline_name"))
        self.assertEqual(experiment.get("integration_status").\
                             get("integration_level"), 
                             intstatus.get("integration_level"))
        self.assertEqual(experiment.get("assets")[0].get("asset_type").\
                             get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))
        self.assertEqual(experiment1, None)
        self.assertEqual(experiment.get("developers")[0].get("email").\
                             get("email"), email_id.get("email"))
        self.assertEqual(experiment.get("hosting_info")[0].\
                             get("hosting_status"), 
                             host.get("hosting_status"))

class TestPersistenceDiscipline(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_discipline(self):
        print "test_persistance_discipline"

        asset_type1 = AssetType(asset_type="video")
        asset_type1.save()

        path = "vlabs.ac.in/static/images/logo.png"

        asset = Asset(path=path, asset_type=asset_type1)
        asset.save()

        discipline_name = "IIT Delhi"
        discipline_id = "ECE08"
        dis = Discipline(discipline_name=discipline_name,
                             discipline_id=discipline_id, assets=[asset])
        dis.save()

        discipline = Discipline.get_by_id(1)
        self.assertEqual(discipline.get("discipline_name"), discipline_name)
        self.assertEqual(discipline.get("discipline_id"), discipline_id)
        self.assertEqual(discipline.get("assets")[0].get("asset_type").\
                             get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))

class TestPersistentLab(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_lab(self):
        print "test_persistent_lab"


        asset_type1 = AssetType(asset_type="video")
        asset_type1.save()

        path = "vlabs.ac.in/static/images/logo.png"

        asset = Asset(path=path, asset_type=asset_type1)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = Institute(institute_name=institute_name, 
                             institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                    assets=[asset])
        discipline.save()

        integration_level = 4
        intstatus = IntegrationStatus(integration_level=integration_level)
        intstatus.save()

        exp_name = "Number Systems"
        exp_id = "EE99777"
        overview = "This is linked list experiment"

        dev_name = Name(name="Mohit Tahiliani")
        dev_name.save()
        email_id = Email(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = Developer(name=dev_name, email=email_id)
        dev.save()

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = HostingInfo(hosting_status=hosting_status,
                               hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()

        exp_name = "Number Systems"
        exp_id = "EE99777"
        overview = "This is linked list experiment"
        experiment = Experiment(exp_name=exp_name, exp_id=exp_id,
                                    overview=overview, sections=[],
                                    integration_status=intstatus, 
                                    hosting_info=[host], assets=[asset], 
                                    institute=inst, discipline=discipline, 
                                    developers=[dev])
        experiment.save()

        name = "Theory"
        section = Section(name=name)
        section.save()

        lab_name1="Computer Programming"
        lab_id1="CSE01"
        overview1 = "This is data structures lab which deals about array,stack"
        " and ques..etc"
        lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview1,
                       experiments=[experiment], institute=inst,
                       integration_status=intstatus, sections=[section],
                       assets=[asset], discipline=discipline, 
                       developers=[dev], hosting_info=[host])
        lab1.save()

        lab_name2="Data Structures"
        lab_id2="CSE02"
        overview2 = "This is data structures lab which deals about"
        "array,stack and ques..etc"

        lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview2,
                       experiments=[], institute=inst, discipline=discipline, 
                       developers=[], hosting_info=[host], assets=[asset],
                       sections=[section], 
                       integration_status=intstatus)
        lab2.save()

        lab1 = Lab.get_by_id(1)
        lab2 = Lab.get_by_id(2)
        lab3 = Lab.get_by_id(3)

        self.assertEqual(lab1.get("lab_name"), lab_name1)
        self.assertEqual(lab1.get("lab_id"), lab_id1)
        self.assertEqual(lab1.get("overview"), overview1)
        self.assertEqual(lab1.get("institute").get("institute_name"), 
                             inst.get("institute_name"))
        self.assertEqual(lab1.get("discipline").get("discipline_name"), 
                             discipline.get("discipline_name"))
        self.assertEqual(lab1.get("assets")[0].get("asset_type"), 
                             asset.get("asset_type"))
        self.assertEqual(lab1.get("experiments")[0].get("exp_name"), 
                             experiment.get("exp_name"))
        self.assertEqual(lab1.get("sections")[0].get("name"), 
                             section.get("name"))
        self.assertEqual(lab1.get("integration_status").\
                             get("integration_level"), 
                             intstatus.get("integration_level"))

        self.assertEqual(lab1.get("developers")[0].get("email").get("email"), 
                             email_id.get("email"))

        self.assertEqual(lab1.get("hosting_info")[0].get("hosting_status"), 
                             host.get("hosting_status"))

        self.assertEqual(lab2.get("lab_name"), lab_name2)
        self.assertEqual(lab2.get("lab_id"), lab_id2)
        self.assertEqual(lab2.get("overview"), overview2)
        self.assertEqual(lab2.get("institute").get("institute_name"), 
                             inst.get("institute_name"))
        self.assertEqual(lab2.get("discipline").get("discipline_name"), 
                             discipline.get("discipline_name"))
        self.assertEqual(lab2.get("hosting_info")[0].get("hosting_status"), 
                             host.get("hosting_status"))
        self.assertEqual(lab2.get("experiments"), [])

        self.assertEqual(lab2.get("assets")[0].get("asset_type"), 
                             asset.get("asset_type"))
        self.assertEqual(lab2.get("integration_status").\
                             get("integration_level"), 
                             intstatus.get("integration_level"))
        self.assertEqual(lab2.get("developers"), [])

        self.assertEqual(lab3, None)


class TestPersistentSection(TestCase):

    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_section(self):
        print "test_persistent_section"
        name = "Theory"
        section = Section(name=name)
        section.save()
        section1 = Section.get_by_id(1)
        section2 = Section.get_by_id(2)
        self.assertEqual(section1.get("name"), name)
        self.assertEqual(section2,None)

class TestPersistentName(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_persistent_name(self):
        print "test_persistent_name"

        name = "Mohit tahiliani"
        name1 = Name(name=name)
        name1.save()
        
        name1 = Name.get_by_id(1)

        self.assertEqual(name1.get("name"), name)

class TestPersistentEmail(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_email(self):
        print "test_persistent_email"

        email_id = "mohit.tahiliani@gmail.com"
        email1 = Email(email=email_id)
        email1.save()
        
        email1 = Email.get_by_id(1)

        self.assertEqual(email1.get("email"), email_id)

class TestPersistentDeveloper(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_dev(self):
        print "test_persistent_dev"

        dev_name = Name(name="Mohit Tahiliani")
        dev_name.save()
        email_id = Email(email="mohit.tahiliani@gmail.com")
        email_id.save()
        dev = Developer(name=dev_name, email=email_id)
        dev.save()
        
        dev = Developer.get_by_id(1)

        self.assertEqual(dev.get("name").get("name"), dev_name.get("name"))
        self.assertEqual(dev.get("email").get("email"), email_id.get("email"))

class TestPersistenceInstitute(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_institute(self):
        print "test_persistance_institute"

        asset_type1 = AssetType(asset_type="video")
        asset_type1.save()

        path = "vlabs.ac.in/static/images/logo.png"

        asset = Asset(path=path, asset_type=asset_type1)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = Institute(institute_name=institute_name,
                             institute_id=institute_id, assets=[asset])
        inst.save()
        institute = Institute.get_by_id(1)
        institute1 = Institute.get_by_id(2)
        self.assertEqual(institute.get("institute_name"), institute_name)
        self.assertEqual(institute.get("institute_id"), institute_id)   
        self.assertEqual(institute.get("assets")[0].get("asset_type").\
                             get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))    
        self.assertEqual(institute1, None)

class TestPersistenceHostingInfo(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_hosting_info(self):
        print "test_persistent_hosting_info"
        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = HostingInfo(hosting_status=hosting_status, hosted_url=hosted_url, hosted_on=hosted_on)
        host.save()
        hosting_info = HostingInfo.get_by_id(1)
        hosting_info1 = HostingInfo.get_by_id(2)
        self.assertEqual(hosting_info.get("hosting_status"), hosting_status)
        self.assertEqual(hosting_info.get("hosted_url"), hosted_url)
        self.assertEqual(hosting_info.get("hosted_on"), hosted_on)
        self.assertEqual(hosting_info1,None)

class TestPersistentAssetType(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_asset_type(self):
        print "test_persistent_asset_type"

        asset_type1 = AssetType(asset_type="video")
        asset_type1.save()
        
        asset_type1 = AssetType.get_by_id(1)

        self.assertEqual(asset_type1.get("asset_type"),
                             asset_type1.get("asset_type"))

class TestPersistenceAsset(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_asset(self):
        print "test_persistance_asset"

        path = "vlabs.ac.in/static/images/logo.png"

        asset_type1 = AssetType(asset_type="video")
        asset_type1.save()

        asset = Asset(path=path, asset_type=asset_type1)
        asset.save()

        asset = asset.get_by_id(1)
        asset1 = asset.get_by_id(2)
        self.assertEqual(asset.get("path"), path)
        self.assertEqual(asset.get("asset_type").get("asset_type"),
                             asset_type1.get("asset_type"))       
        self.assertEqual(asset1,None)


class TestPersistenceIntegrationStatus(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_integration_status(self):
        print "test_persistance_integration_status"
        integration_level = 4
        intstatus = IntegrationStatus(integration_level=integration_level)
        intstatus.save()
        integration_status = IntegrationStatus.get_by_id(1)
        integration_status1 = IntegrationStatus.get_by_id(2)
        self.assertEqual(integration_status.get("integration_level"),\
                             integration_level)
        self.assertEqual(integration_status1,None)

if __name__ == '__main__':
    unittest.main()
