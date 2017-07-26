
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from entities import *

class TestSession(TestCase):
    TESTING = True

    def test_object_session(self):
        print "test_object_session"
        key = "dkjhfkjdhfkjadhfkjhdafkjh"
        session = Session(key=key)
        self.assertEqual(session.get("key"), key)

class TestLab(TestCase):
    TESTING = True
    def test_object_lab(self):
        print "test_object_lab"
        exp_name = "Number Systems"
        exp_id = "EE99777"
        overview = "This is array exp"

        asset_type = AssetType(asset_type="Image")
        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)

        institute_name = "IIIT Hyderabad"
        institute_id = "IIIT-H"
        inst = Institute(institute_name=institute_name,
                             institute_id=institute_id, assets=[asset])

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = Discipline(discipline_name=discipline_name,
                                    discipline_id=discipline_id,
                                    assets=[asset])

        integration_level = 4
        integration_status = IntegrationStatus(integration_level=\
                                                   integration_level)

        dev_name = Name(name="Mohit Tahiliani")
        email_id = Email(email="mohit.tahiliani@gmail.com")
        dev = Developer(name=dev_name, email=email_id)

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = HostingInfo(hosting_status=hosting_status,
                               hosted_url=hosted_url, hosted_on=hosted_on)

        experiment = Experiment(exp_name=exp_name, exp_id=exp_id, \
                                overview=overview, sections=[],
                                institute=inst, discipline=discipline,
                                integration_status=integration_status,
                                assets=[asset], developers=[dev],
                                hosting_info=[host])

        lab_name = "Computer Programming"
        lab_id = "CSE01"
        overview = "This is data structures lab which deals about array,stack"
        "and ques..etc"
        lab = Lab(lab_name=lab_name, lab_id=lab_id, overview=overview,
                      institute=inst, discipline=discipline, assets=[asset],
                      integration_status=integration_status, developers=[dev],
                      hosting_info=[host], sections=[],
                      experiments=[experiment])

        self.assertEqual(lab.get("lab_name"), lab_name)
        self.assertEqual(lab.get("lab_id"), lab_id)
        self.assertEqual(lab.get("overview"), overview)
        self.assertEqual(lab.get("institute").get("institute_name"), 
                             inst.get("institute_name"))
        self.assertEqual(lab.get("discipline").get("discipline_name"), 
                             discipline.get("discipline_name"))
        self.assertEqual(lab.get("assets")[0].get("asset_type").\
                             get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))
        self.assertEqual(lab.get("integration_status").\
                             get("integration_level"), integration_status.\
                             get("integration_level"))
        self.assertEqual(lab.get("experiments")[0].get("exp_name"), 
                             experiment.get("exp_name"))
        self.assertEqual(lab.get("developers")[0].get("email").get("email"),
                             email_id.get("email"))
        self.assertEqual(lab.get("sections"), [])
        self.assertEqual(lab.get("hosting_info")[0].get("hosting_status"), 
                             host.get("hosting_status"))

class TestExperiment(TestCase):
    TESTING = True

    def test_object_experiment(self):
        print "test_object_experiment"

        asset_type = AssetType(asset_type="Image")
        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)

        institute_name = "IIIT Hyderabad"
        institute_id = "IIIT-H"
        inst = Institute(institute_name=institute_name,
                             institute_id=institute_id, assets=[asset])

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = Discipline(discipline_name=discipline_name,
                                    discipline_id=discipline_id,
                                    assets=[asset])  

        exp_name = "Number Systems"
        exp_id = "EE99777"
        overview = "This is linked list experiment"

        integration_level = 4
        integration_status = IntegrationStatus(integration_level=\
                                                   integration_level)

        dev_name = Name(name="Mohit Tahiliani")
        email_id = Email(email="mohit.tahiliani@gmail.com")
        dev = Developer(name=dev_name, email=email_id)

        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        host = HostingInfo(hosting_status=hosting_status,
                               hosted_url=hosted_url, hosted_on=hosted_on)

        experiment = Experiment(exp_name=exp_name, exp_id=exp_id, 
                                institute=inst, discipline=discipline,     
                                overview=overview,
                                integration_status=integration_status, 
                                sections=[], assets=[asset],
                                developers=[dev], hosting_info=[host])

        self.assertEqual(experiment.get("exp_name"), exp_name)
        self.assertEqual(experiment.get("overview"), overview)
        self.assertEqual(experiment.get("integration_status").\
                             get("integration_level"), \
                             integration_status.get("integration_level"))
        self.assertEqual(experiment.get("assets")[0].get("asset_type")\
                             .get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))       
        self.assertEqual(experiment.get("exp_id"), exp_id)
        self.assertEqual(experiment.get("sections"), [])
        self.assertEqual(experiment.get("institute").get("institute_name"), 
                             inst.get("institute_name"))
        self.assertEqual(experiment.get("discipline").get("discipline_name"), 
                             discipline.get("discipline_name"))
        self.assertEqual(experiment.get("developers")[0].get("email").\
                             get("email"), email_id.get("email"))
        self.assertEqual(experiment.get("hosting_info")[0].\
                             get("hosting_status"), host.get("hosting_status"))

class TestDiscipline(TestCase):
    TESTING = True
    def test_object_discipline(self):
        print "test_object_discipline"

        asset_type = AssetType(asset_type="Image")
        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)

        discipline_name = "IIT Delhi"
        discipline_id = "ECE08"
        discipline = Discipline(discipline_name=discipline_name,
                                    discipline_id=discipline_id,
                                    assets=[asset])

        self.assertEqual(discipline.get("discipline_name"), discipline_name)
        self.assertEqual(discipline.get("discipline_id"), discipline_id)
        self.assertEqual(discipline.get("assets")[0].get("asset_type").\
                             get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))

class TestSection(TestCase):
    TESTING = True
    def test_object_section(self):
        print "test_object_section"
        name = "Theory"
        section = Section(name="Theory")

        self.assertEqual(section.get("name"), name)

class TestName(TestCase):
    TESTING = True

    def test_object_name(self):
        print "test_object_name"
        name1=Name(name="Jimi Hendrix")
        self.assertEqual(is_name(Name(name="Jimi Hendrix")), True)
        self.assertEqual(name1.get("name"), "Jimi Hendrix")
        self.assertRaises(TypeError, Name, name="Jimi 123 Hendrix")

class TestEmail(TestCase):
    TESTING = True

    def test_instantiate_email(self):
        print "test_instantiate_email"
        self.assertEqual(is_email(Email(email="jimi@gnu.org")), True)
        self.assertEqual(Email(email="jimi@gnu.org").get("email"),
                         "jimi@gnu.org")
        self.assertRaises(TypeError, Name, name="jimi@@gnu.org")

    def test_object_email(self):
        print "test_object_email"
        email1 = Email(email="abc@gmail.com")

        self.assertEqual(email1 == email1, True)

        email2 = Email(email="xyz@gmail.com")
        self.assertEqual(email1 == email2, False)

class TestDev(TestCase):
    TESTING = True
    def test_object_dev(self):
        print "test_object_dev"

        dev_name = Name(name="Mohit Tahiliani")
        email_id = Email(email="mohit.tahiliani@gmail.com")
        dev = Developer(name=dev_name, email=email_id)

        self.assertEqual(dev.get("name").get("name"), dev_name.get("name"))
        self.assertEqual(dev.get("email").get("email"), email_id.get("email"))

class TestInstitute(TestCase):
    TESTING = True
    def test_object_institute(self):
        print "test_object_institute"

        asset_type = AssetType(asset_type="Image")
        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)

        institute_name = "IIIT Hyderabad"
        institute_id = "IIIT-H"
        institute = Institute(institute_name=institute_name,
                                  institute_id=institute_id,
                                  assets=[asset])
                                              
        self.assertEqual(institute.get("institute_name"), institute_name)
        self.assertEqual(institute.get("institute_id"), institute_id)
        self.assertEqual(institute.get("assets")[0].get("asset_type")\
                             .get("asset_type"), 
                             asset.get("asset_type").get("asset_type"))
       
class TestAssetType(TestCase):
    TESTING = True

    def test_instantiate_asset_type(self):
        print "test_instantiate_asset_type"
        self.assertEqual(is_asset_type(AssetType(asset_type="image")),
                             True)
        self.assertEqual(AssetType(asset_type="image").get("asset_type"),
                         "image")
        self.assertRaises(TypeError, AssetType, asset_type=123)

    def test_object_asset_type(self):
        print "test_object_asset_type"
        asset_type1 = AssetType(asset_type="video")
        self.assertEqual(asset_type1 == asset_type1, True)

        asset_type2 = AssetType(asset_type="image")
        self.assertEqual(asset_type1 == asset_type2, False)

class TestAsset(TestCase):
    TESTING = True
    def test_object_asset(self):
        print "test_object_asset"

        path = "vlabs.ac.in/static/images/logo.png"
        asset_type1 = AssetType(asset_type="video")

        asset = Asset(path=path, asset_type=asset_type1)
                                              
        self.assertEqual(asset.get("path"), path)
        self.assertEqual(asset.get("asset_type").get("asset_type"),
                             asset_type1.get("asset_type"))
    
class TestHostingInfo(TestCase):
    TESTING = True
    def test_object_hosting_info(self):
        print "test_object_hosting_info"
        hosting_status = "hosted"
        hosted_url = "http://cse14-iiith.vlabs.ac.in"
        hosted_on = "cloud"
        hosting_info = HostingInfo(hosting_status=hosting_status,
                                       hosted_url=hosted_url,
                                       hosted_on=hosted_on)
                                              
        self.assertEqual(hosting_info.get("hosting_status"), hosting_status)
        self.assertEqual(hosting_info.get("hosted_url"), hosted_url)
        self.assertEqual(hosting_info.get("hosted_on"), hosted_on)
       
class TestIntegrationStatus(TestCase):
    TESTING = True

    def test_object_integration_status(self):
        print "test_object_integration_status"
        integration_level = 4
        integration_status = IntegrationStatus(integration_level=integration_level)

        self.assertEqual(integration_status.get("integration_level"), integration_level)

if __name__ == '__main__':
    unittest.main()
