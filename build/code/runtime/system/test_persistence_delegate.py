
# -*- coding: utf-8 -*-
import unittest
from flask_testing import TestCase
from runtime.rest.app import create_app
from runtime.system.persistence_delegate import *


config = {
         'SQLALCHEMY_DATABASE_URI': ''
         }
class TestPersistenceDelegate(TestCase):
    TESTING = True

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()
        self.persistence_delegate = PersistenceDelegate()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.persistence_delegate = None


    def test_get_lab(self):
         print "test_get_lab"
         lab_name1 = "Computer Programming"
         lab_id1 = "CSE01"
         overview = "overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                       institute=inst, discipline=discipline, 
                       hosting_info=[host], assets=[asset],
                       experiments=[], developers=[dev], sections=[section], 
                       integration_status=integration_status)

         lab.save()

         lab_obj = self.persistence_delegate.get_lab(lab_name=
                                                lab.get("lab_name"))
         self.assertEqual(lab_obj.get("lab_name"), lab.get("lab_name"))
         self.assertEqual(lab_obj.get("lab_id"), lab.get("lab_id"))

    def test_get_lab(self):
         print "test_get_lab"
         lab_name1 = "Computer Programming"
         lab_id1 = "CSE01"
         overview = "overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                       institute=inst, discipline=discipline, 
                       hosting_info=[host], assets=[asset],
                       experiments=[], developers=[dev], sections=[section], 
                       integration_status=integration_status)

         lab.save()

         lab_obj = self.persistence_delegate.get_lab(lab_name=
                                                lab.get("lab_name"))
         self.assertEqual(lab_obj.get("lab_name"), lab.get("lab_name"))
         self.assertEqual(lab_obj.get("lab_id"), lab.get("lab_id"))

    def test_get_section(self):
         print "test_get_section"
         name = "Theory"
         section = Section(name=name)
         section.save()

         section_obj = self.persistence_delegate.get_section(name=
                                                section.get("name"))
         self.assertEqual(section_obj.get("name"),
                              section.get("name"))

    def test_get_experiment(self):
         print "test_get_experiment"

         hosting_status = "hosted"
         hosted_url = "http://cse14-iiith.vlabs.ac.in"
         hosted_on = "cloud"
         host = HostingInfo(hosting_status=hosting_status,
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         dev_name = Name(name="Mohit Tahiliani")
         dev_name.save()
         email_id = Email(email="mohit.tahiliani@gmail.com")
         email_id.save()
         dev = Developer(name=dev_name, email=email_id)
         dev.save()

         exp_name = "Number Systems"
         exp_id = "EE99777"
         overview = "overview"

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

         exp = Experiment(exp_name=exp_name, exp_id=exp_id,
                              overview=overview, sections=[],
                              institute=inst, discipline=discipline, 
                              integration_status=integration_status,
                              assets=[asset], developers=[dev],
                              hosting_info=[host])
         exp.save()
         exp_obj = self.persistence_delegate.get_experiment(exp_name=
                                                exp.get("exp_name"))
         self.assertEqual(exp_obj.get("exp_name"),
                              exp.get("exp_name"))

    def test_get_institute(self):
         print "test_get_institute"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Delhi"
         institute_id = "IITD"
         inst = Institute(institute_name=institute_name, institute_id=institute_id,
                              assets=[asset]) 
         inst.save()
         inst_obj = self.persistence_delegate.get_institute(institute_name=
                                                inst.get("institute_name"))

         inst_obj1 = self.persistence_delegate.get_institute(institute_id=
                                                inst.get("institute_id"))

         self.assertEqual(inst_obj.get("institute_name"), inst.get("institute_name"))
         self.assertEqual(inst_obj1.get("institute_id"), inst.get("institute_id"))

    def test_get_discipline(self):
         print "test_get_discipline"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         discipline_name = "IIT Delhi"
         discipline_id = "EEE08"
         dis = Discipline(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
         dis.save()
         dis_obj = self.persistence_delegate.get_discipline(discipline_name=discipline_name)
         dis_obj1 = self.persistence_delegate.get_discipline(discipline_id=discipline_id)

         self.assertEqual(dis_obj.get("discipline_name"), discipline_name)
         self.assertEqual(dis_obj1.get("discipline_id"), discipline_id)

    def test_get_hosting_info(self):
         print "test_get_hosting_info"

         hosting_status = "hosted"
         hosted_url = "http://cse14-iiith.vlabs.ac.in"
         hosted_on = "cloud"
         host = HostingInfo(hosting_status=hosting_status,
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()
         host_obj = self.persistence_delegate.get_hosting_info(hosting_status=
                                                host.get("hosting_status"))

         host_obj1 = self.persistence_delegate.get_hosting_info(hosted_url=
                                                host.get("hosted_url"))

         host_obj2 = self.persistence_delegate.get_hosting_info(hosted_on=
                                                host.get("hosted_on"))

         self.assertEqual(host_obj.get("hosting_status"),
                              host.get("hosting_status"))
         self.assertEqual(host_obj1.get("hosted_url"), host.
                              get("hosted_url"))
         self.assertEqual(host_obj2.get("hosted_on"), host.
                              get("hosted_on"))

    def test_get_asset(self):
         print "test_get_asset"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/static/images/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()
         asset_obj = self.persistence_delegate.get_asset(asset_type=
                                                asset.get("asset_type"))
         self.assertEqual(asset_obj.get("asset_type"),
                              asset.get("asset_type"))

    def test_get_integration_status(self):
         print "test_get_integration_status"

         integration_level = 4
         intstatus = IntegrationStatus(integration_level=integration_level)
         intstatus.save()
         intstatus_obj = self.persistence_delegate.get_integration_status\
         (integration_level=intstatus.get("integration_level"))

         self.assertEqual(intstatus_obj.get("integration_level"),
                              intstatus.get("integration_level"))


    def test_get_labs_with_same_overview(self):
         print "test_get_labs_with_same_overview"
         lab_name1="Computer Programming"
         lab_id1="CSE01"
         overview="overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                        institute=inst, discipline=discipline, 
                        hosting_info=[host], assets=[asset],
                        experiments=[], developers=[dev], sections=[section], 
                        integration_status=integration_status)

         lab1.save()

         lab_name2="Data Structures"
         lab_id2="CSE02"


         lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview, \
                        institute=inst, discipline=discipline, assets=[asset],\
                        experiments=[], integration_status=integration_status,
                        developers=[dev], hosting_info=[host], sections=[section])

         lab2.save()

         labs_list = self.persistence_delegate.get_labs(overview=overview)

         self.assertEqual(labs_list[0].get("overview"), overview)
         self.assertEqual(labs_list[1].get("overview"), overview)

    def test_get_lab_with_given_lab_id(self):
         print "test_get_lab_with_given_lab_id"
         lab_name1="Computer Programming"
         lab_id1="CSE01"
         overview="overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                        institute=inst, discipline=discipline,
                        hosting_info=[host], assets=[asset],
                        experiments=[], developers=[dev], sections=[section],
                        integration_status=integration_status)

         lab1.save()

         lab_name2="Data Structures"
         lab_id2="CSE02"

         lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview, \
                        institute=inst, discipline=discipline, assets=[asset],\
                        experiments=[], integration_status=integration_status,\
                        developers=[dev], sections=[section], hosting_info=[host])

         lab2.save()

         labs_list = self.persistence_delegate.get_labs(lab_id=lab_id1)

         self.assertEqual(labs_list[0].get("lab_id"), lab_id1)

    def test_get_lab_with_given_lab_id_and_lab_name(self):
         print "test_get_lab_with_given_lab_id_and_labname"
         lab_name1="Computer Programming"
         lab_id1="CSE01"
         overview="overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "computer science"
         discipline_id = "cse"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                        institute=inst, discipline=discipline, 
                        hosting_info=[host], assets=[asset],
                        experiments=[], developers=[dev], sections=[section], 
                        integration_status=integration_status)
         lab1.save()

         lab_name2="Data Structures"
         lab_id2="CSE02"

         lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview, \
                        institute=inst, discipline=discipline, assets=[asset],\
                        experiments=[], integration_status=integration_status,
                        developers=[dev], sections=[section], hosting_info=[host])
         lab2.save()

         labs_list = self.persistence_delegate.get_labs(lab_id=lab_id1,
                                                            lab_name=lab_name1)

         self.assertEqual(labs_list[0].get("lab_id"), lab_id1)

    def test_get_lab_with_given_institute(self):
         print "test_get_lab_with_given_institute"

         lab_name1="Computer Programming"
         lab_id1="CSE01"
         overview="overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                        institute=inst, discipline=discipline, 
                        hosting_info=[host], assets=[asset],
                        experiments=[], developers=[dev], sections=[section], 
                        integration_status=integration_status)
         lab1.save()

         lab_name2="Data Structures"
         lab_id2="CSE02"

         lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview, \
                        institute=inst, discipline=discipline, assets=[asset],\
                        experiments=[], integration_status=integration_status,
                        developers=[dev], sections=[section], hosting_info=[host])
         lab2.save()

         labs_list = self.persistence_delegate.get_labs(institute=inst)

         self.assertEqual(labs_list[0].get("institute").get("institute_id"),
                              lab1.get("institute").get("institute_id"))

    def test_get_institutes(self):
         print "test_get_institutes"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Delhi"
         institute_id = "IITD"
         inst = Institute(institute_name=institute_name, institute_id=institute_id,
                              assets=[asset])                             
         inst.save()
         inst_obj = self.persistence_delegate.get_institute(institute_name=
                                                inst.get("institute_name"))

         insts_list = self.persistence_delegate.get_institutes(institute_id=
                                                inst.get("institute_id"),
                                                institute_name=
                                                inst.get("institute_name"))

         self.assertEqual(insts_list[0].get("institute_name"),
                              inst.get("institute_name"))
         self.assertEqual(insts_list[0].get("institute_id"), inst.get("institute_id"))

    def test_get_assets(self):
         print "test_get_assets"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/static/images/logo.png"
         asset = Asset(path=path, asset_type=asset_type)     
         asset.save()
         asset_obj = self.persistence_delegate.get_asset(asset_type=
                                                asset.get("asset_type"))

         assets_list = self.persistence_delegate.get_assets(path=
                                                asset.get("path"),
                                                asset_type=
                                                asset.get("asset_type"))

         self.assertEqual(assets_list[0].get("asset_type"),
                              asset.get("asset_type"))
         self.assertEqual(assets_list[0].get("path"), asset.get("path"))


    def test_lab_exists(self):
        print "test_lab_exists"
        lab_name1="Computer Programming"
        lab_id1="CSE01"
        overview1 = "overview"

        asset_type = AssetType(asset_type="Image")
        asset_type.save()
        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = Institute(institute_name=institute_name,
                             institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = Discipline(discipline_name=discipline_name,
                                    discipline_id=discipline_id,\
                                    assets=[asset])
        discipline.save()
        
        integration_level = 4
        integration_status = IntegrationStatus(integration_level=\
                                                   integration_level)
        integration_status.save()
         
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
                               hosted_url=hosted_url, 
                               hosted_on=hosted_on)
        host.save()

        name = "Theory"
        section = Section(name=name)
        section.save()


        lab = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview1,
                      institute=inst, discipline=discipline, assets=[asset],
                      experiments=[], integration_status=integration_status,
                      developers=[dev], sections=[section],hosting_info=[host])

        lab1 = self.persistence_delegate.add_lab(lab)

        lab_name2="Data Structures"
        lab_id2="CSE02"
        overview2 = "overview"

        lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview2,
                       integration_status=integration_status, sections=[section],               
                       institute=inst, discipline=discipline, assets=[asset],
                       experiments=[], developers=[dev], hosting_info=[host])

        self.assertEqual(self.persistence_delegate.lab_exists(lab1),
                            True)
        self.assertEqual(self.persistence_delegate.lab_exists(lab2),
                            False)

    def test_experiment_exists(self):
        print "test_experiment_exists"

        asset_type = AssetType(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)
        asset.save()

        institute_name = "IIT Kanpur"
        institute_id = "IITK"
        inst = Institute(institute_name=institute_name,
                             institute_id=institute_id, assets=[asset])
        inst.save()

        discipline_name = "IIT Kanpur"
        discipline_id = "IITK"
        discipline = Discipline(discipline_name=discipline_name,
                                    discipline_id=discipline_id,\
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

        exp_name1 = "Number Systems"
        exp_id1 = "EE99777"
        overview1 = "overview"

        integration_level = 4
        integration_status = IntegrationStatus(integration_level=\
                                                   integration_level)
        integration_status.save()

        experiment1 = Experiment(exp_name=exp_name1, exp_id=exp_id1,
                                 overview=overview1, sections=[],
                                 institute=inst, discipline=discipline, 
                                 integration_status=integration_status,
                                 assets=[asset], developers=[dev],
                                 hosting_info=[host])

        exp1 = self.persistence_delegate.add_experiment(experiment1)

        exp_name2 = "Transformations"
        exp_id2 = "EE98747"
        overview2 = "overview"
        experiment2 = Experiment(exp_name=exp_name2, exp_id=exp_id2, \
                                overview=overview2, sections=[],
                                institute=inst, discipline=discipline, 
                                integration_status=integration_status,
                                assets=[asset], developers=[dev],
                                hosting_info=[host])
        self.assertEqual(self.persistence_delegate.experiment_exists\
                             (experiment1), True)
        self.assertEqual(self.persistence_delegate.experiment_exists\
                             (experiment2), False)

    def test_section_exists(self):
        print "test_section_exists"
        name1 = "Theory"
        section1 = Section(name=name1)
        self.persistence_delegate.add_section(section1)
        name2 = "Assessment"
        section2 = Section(name=name2)
        self.assertEqual(self.persistence_delegate.section_exists(section1),
                            True)
        self.assertEqual(self.persistence_delegate.section_exists(section2),
                            False)

    def test_name_exists(self):
        print "test_name_exists"
        name1 = "Prof. Dharmaraj"
        name2 = Name(name=name1)
        self.persistence_delegate.add_name(name2)
        name3 = "Prof. Raja"
        name4 = Name(name=name3)
        self.assertEqual(self.persistence_delegate.name_exists(name2),
                            True)
        self.assertEqual(self.persistence_delegate.name_exists(name4),
                            False)

    def test_email_exists(self):
        print "test_email_exists"
        email1 = "abc@gmail.com"
        email2 = Email(email=email1)
        self.persistence_delegate.add_email(email2)
        email3 = "xyz@gmail.com"
        email4 = Email(email=email3)
        self.assertEqual(self.persistence_delegate.email_exists(email2), True)
        self.assertEqual(self.persistence_delegate.email_exists(email4), False)

    def test_developer_exists(self):
        print "test_developer_exists"

        dev_name1 = Name(name="Prof. Dharmaraj")
        dev_name1.save()
        email_id1 = Email(email="abc@gmail.com")
        email_id1.save()
        developer1 = Developer(name=dev_name1, email=email_id1)
        developer1.save()

        dev_name2 = Name(name="Prof. Raja")
        dev_name2.save()
        email_id2 = Email(email="xyz@gmail.com")
        email_id2.save()
        developer2 = Developer(name=dev_name2, email=email_id2)

        self.assertEqual(self.persistence_delegate.\
                             developer_exists(developer1), True)
        self.assertEqual(self.persistence_delegate.developer_exists\
                             (developer2), False)
    def test_institute_exists(self):
        print "test_institute_exists"

        asset_type = AssetType(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)
        asset.save()

        institute_name1 = "IIT Kanpur"
        institute_id1 = "IITK"
        institute1 = Institute(institute_name=institute_name1,
                                   institute_id=institute_id1,
                                   assets=[asset]) 
        inst1 = self.persistence_delegate.add_institute(institute1)

        institute_name2 = "IIT Kharagpur"
        institute_id2 = "IITKgp"
        institute2 = Institute(institute_name=institute_name2,
                                   institute_id=institute_id2,
                                   assets=[asset]) 
        
        self.assertEqual(self.persistence_delegate.institute_exists\
                             (institute1), True)
        self.assertEqual(self.persistence_delegate.institute_exists\
                             (institute2), False)

  
    def test_discipline_exists(self):
        print "test_discipline_exists"

        asset_type = AssetType(asset_type="Image")
        asset_type.save()

        path = "vlabs.ac.in/images/static/logo.png"
        asset = Asset(asset_type=asset_type, path=path)
        asset.save()

        discipline_name1="IIT Delhi"
        discipline_id1="EEE08"
        dis = Discipline(discipline_name=discipline_name1,
                             discipline_id=discipline_id1,
                             assets=[asset])

        dis1 = self.persistence_delegate.add_discipline(dis)

        discipline_name2="IIT Delhi"
        discipline_id2="EEE09"
        dis2 = Discipline(discipline_name=discipline_name2,
                              discipline_id=discipline_id2,
                              assets=[asset])

        self.assertEqual(self.persistence_delegate.discipline_exists(dis1),
                            True)
        self.assertEqual(self.persistence_delegate.discipline_exists(dis2),
                            False)
     


    def test_hosting_info_exists(self):
        print "test_hosting_info_exists"
        hosting_status1 = "hosted"
        hosted_url1 = "http://cse14-iiith.vlabs.ac.in"
        hosted_on1 = "cloud"
        hosting_info1 = HostingInfo(hosting_status=hosting_status1,\
                                        hosted_url=hosted_url1,\
                                        hosted_on=hosted_on1)
        host1 = self.persistence_delegate.add_hosting_info(hosting_info1)

        hosting_status2 = "not hosted"
        hosted_url2 = "http://iitkgp.vlab.co.in/"
        hosted_on2 = "server"
        hosting_info2 = HostingInfo(hosting_status=hosting_status2,\
                                        hosted_url=hosted_url2,\
                                        hosted_on=hosted_on2)
        
        self.assertEqual(self.persistence_delegate.hosting_info_exists\
                             (hosting_info1), True)
        self.assertEqual(self.persistence_delegate.hosting_info_exists\
                             (hosting_info2), False)

    def test_asset_exists(self):
        print "test_asset_exists"       

        asset_type1 = AssetType(asset_type="Image")
        asset_type1.save()

        path1 = "vlabs.ac.in/static/images/logo.png"
        asset1 = Asset(asset_type=asset_type1, path=path1)
        asst1 = self.persistence_delegate.add_asset(asset1)

        asset_type2 = AssetType(asset_type="Icon")
        asset_type2.save()

        path2 = "vlabs.ac.in/static/images/icon.png"
        asset2 = Asset(asset_type=asset_type2, path=path2)

        self.assertEqual(self.persistence_delegate.asset_exists\
                             (asst1), True)
        self.assertEqual(self.persistence_delegate.asset_exists\
                             (asset2), False)

    def test_integration_status_exists(self):
        print "test_integration_status_exists"
        integration_level1 = 4
        integration_status1 = IntegrationStatus(integration_level=\
                                                    integration_level1)
        intstatus1 = self.persistence_delegate.add_integration_status\
        (integration_status1)

        integration_level2 = 2
        integration_status2 = IntegrationStatus(integration_level=\
                                                    integration_level2)
        
        self.assertEqual(self.persistence_delegate.integration_status_exists\
                             (integration_status1), True)
        self.assertEqual(self.persistence_delegate.integration_status_exists\
                             (integration_status2), False)

    def test_add_lab(self):
         print "test_add_lab"

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=\
                                                    integration_level)
         integration_status.save()

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name,
                              institute_id=institute_id,\
                              assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name,
                                     discipline_id=discipline_id,\
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
         host = HostingInfo(hosting_status=hosting_status,\
                                hosted_url=hosted_url, hosted_on=hosted_on)
         host.save()

         exp_name = "Number Systems"
         exp_id = "EE99777"
         overview = "exp"
         experiment = Experiment(exp_name=exp_name, exp_id=exp_id, \
                                  overview=overview, institute=inst, 
                                  discipline=discipline,
                                  integration_status=integration_status, 
                                  sections=[], assets=[asset],
                                  developers=[dev], hosting_info=[host])
         experiment.save()

         lab_name1="Computer Programming"
         lab_id1="CSE01"
         overview="lab"

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, \
                        institute=inst, discipline=discipline,\
                        assets=[asset], overview=overview,\
                        experiments=[experiment], sections=[section], \
                        integration_status=integration_status,\
                        developers=[dev], hosting_info=[host])

         lab1 = self.persistence_delegate.add_lab(lab1)
        
         lab_name2="Data Structures"
         lab_id2="CSE02"
         overview="lab overview"

         lab2 = Lab(lab_name=lab_name2, lab_id=lab_id2, overview=overview, 
                        institute=inst, discipline=discipline, assets=[asset],
                        experiments=[], integration_status=integration_status,
                        developers=[dev], sections=[section], hosting_info=[host])

         self.assertEqual(self.persistence_delegate.lab_exists(lab1),
                          True)
         self.assertEqual(self.persistence_delegate.lab_exists(lab2),
                          False)

    def test_add_section(self):
         print "test_add_section"
         name = "Theory"
         section = Section(name=name)
         section = self.persistence_delegate.add_section(section)
         section = section.get_by_id(1)
         self.assertEqual(section.get("name"), name)

    def test_add_experiment(self):
         print "test_add_experiment"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()
         
         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()
         
         exp_name1 = "Number Systems"
         exp_id1 = "EE99777"
         overview1 = "overview"
         experiment1 = Experiment(exp_name=exp_name1, exp_id=exp_id1, 
                                      overview=overview1, institute=inst, 
                                      discipline=discipline, 
                                      integration_status=integration_status, 
                                      sections=[], assets=[asset],
                                      developers=[dev], hosting_info=[host])
         experiment1 = self.persistence_delegate.add_experiment(experiment1)
         experiment1.save()
         
         exp_name2="Transformations"
         exp_id2="EE98747"
         overview2="overview"
         experiment2 = Experiment(exp_name=exp_name2, exp_id=exp_id2,
                                      overview=overview2, sections=[],
                                      institute=inst, discipline=discipline, 
                                      integration_status=integration_status,
                                      assets=[asset], developers=[dev], 
                                      hosting_info=[host])    
         experiment = Experiment.get_by_id(1)

         self.assertEqual(self.persistence_delegate.
                              experiment_exists(experiment1),
                          True)
         self.assertEqual(self.persistence_delegate.
                              experiment_exists(experiment2),
                          False)
        
    def test_add_institute(self):
         print "test_add_institute"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save() 

         institute_name1 = "IIT Kanpur"
         institute_id1 = "IITK"
         institute1 = Institute(institute_name=institute_name1,
                                    institute_id=institute_id1,
                                    assets=[asset])  
         institute1 = self.persistence_delegate.add_institute(institute1)
         
         institute_name2= "IIT Kharagpur"
         institute_id2= "IITKgp"
         institute2 = Institute(institute_name=institute_name2,
                                    institute_id=institute_id2,
                                    assets=[asset]) 
         
         institute = Institute.get_by_id(1)

         self.assertEqual(self.persistence_delegate.institute_exists\
                              (institute1), True)
         self.assertEqual(self.persistence_delegate.institute_exists\
                              (institute2), False)
        

    def test_add_discipline(self):
         print "test_add_discipline"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         discipline_name = "IIT Delhi"
         discipline_id = "EEE08"
         discipline = Discipline(discipline_name=discipline_name,
                                     discipline_id=discipline_id,
                                     assets=[asset])
         discipline = self.persistence_delegate.add_discipline(discipline)

         discipline = discipline.get_by_id(1)

         self.assertEqual(discipline.get("discipline_name"), discipline_name)
         self.assertEqual(discipline.get("discipline_id"), discipline_id)

    def test_add_hosting_info(self):
         print "test_add_hosting_info"
         hosting_status1 = "hosted"
         hosted_url1 = "http://cse14-iiith.vlabs.ac.in"
         hosted_on1 = "cloud"
         hosting_info1 = HostingInfo(hosting_status=hosting_status1,\
                                         hosted_url=hosted_url1,\
                                         hosted_on=hosted_on1)
         hosting_info1 = self.persistence_delegate.add_hosting_info(hosting_info1)
         
         hosting_status2 = "not hosted"
         hosted_url2 = "http://iitkgp.vlab.co.in/"
         hosted_on2 = "server"
         hosting_info2 = HostingInfo(hosting_status=hosting_status2,\
                                         hosted_url=hosted_url2,\
                                         hosted_on=hosted_on2)

         hosting_info = HostingInfo.get_by_id(1)

         self.assertEqual(self.persistence_delegate.hosting_info_exists\
                             (hosting_info1), True)
         self.assertEqual(self.persistence_delegate.hosting_info_exists\
                             (hosting_info2), False)
        
    def test_add_asset(self):
         print "test_add_asset"

         asset_type1 = AssetType(asset_type="Image")
         asset_type1.save()

         path1 = "vlabs.ac.in/static/images/logo.png"
         asset1 = Asset(asset_type=asset_type1, path=path1)
         asset1 = self.persistence_delegate.add_asset(asset1)
         
         asset_type2 = AssetType(asset_type="Video")

         path2 = "vlabs.ac.in/static/images/icon.png"
         asset2 = Asset(asset_type=asset_type2, path=path2)
         
         asset = Asset.get_by_id(1)

         self.assertEqual(self.persistence_delegate.asset_exists(asset1),
                          True)
         self.assertEqual(self.persistence_delegate.asset_exists(asset2),
                          False)
#    def test_add_asset_type(self):
#         print "test_add_asset_type"
#
#         asset_type1 = AssetType(asset_type="Image")
#         asset_type1 = self.persistence_delegate.add_asset_type(asset_type1)
#         
#         asset_type2 = AssetType(asset_type="Video")
#         
#         asset_type1 = AssetType.get_by_id(1)
#
#         self.assertEqual(self.persistence_delegate.asset_type_exists(asset_type1),
#                          True)
#         self.assertEqual(self.persistence_delegate.asset_type_exists(asset_type2),
#                          False)
    def test_add_integration_status(self):
         print "test_add_integration_status"
         integration_level1 = 4
         integration_status1 = IntegrationStatus(integration_level= integration_level1)
         integration_status1 = self.persistence_delegate.add_integration_status(integration_status1)
         
         integration_level2= 2
         integration_status2 = IntegrationStatus(integration_level= integration_level2)
         
         integration_status = IntegrationStatus.get_by_id(1)

         self.assertEqual(self.persistence_delegate.integration_status_exists\
                              (integration_status1), True)
         self.assertEqual(self.persistence_delegate.integration_status_exists\
                              (integration_status2), False)
        

    def test_delete_lab(self):
         print "test_delete_lab"
         lab_name = "Data Structures"
         lab_id = "cse01"
         overview = "overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id,
                              assets=[asset])
         inst.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)                    
         integration_status.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab = Lab(lab_name=lab_name, lab_id=lab_id, overview=overview, 
                       institute=inst, discipline=discipline,
                       hosting_info=[host],  assets=[asset],
                       experiments=[], developers=[dev], sections=[section],
                       integration_status=integration_status)

         lab1 = self.persistence_delegate.add_lab(lab)

         lab_name1 = "Computer Programming"
         lab_id1 = "cse02"
         overview = "overview"

         lab1 = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview,
                        institute=inst, discipline=discipline, assets=[asset], 
                        experiments=[], integration_status=integration_status,
                        developers=[dev], hosting_info=[host], sections=[section])

         lab2 = self.persistence_delegate.add_lab(lab1)

         self.persistence_delegate.delete_lab("cse01")

         self.assertEqual(len(Lab.get_all()), 1)

    def test_delete_section(self):
         print "test_delete_section"
         name = "theory"
         section = Section(name=name)
         section1 = self.persistence_delegate.add_section(section)
 
         name1 = "Procedure"
         section1 = Section(name=name1)
         section2 = self.persistence_delegate.add_section(section1)

         self.persistence_delegate.delete_section(1)

         self.assertEqual(len(Section.get_all()), 1)

    def test_delete_experiment(self):
         print "test_delete_experiment"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()
         
         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()
        
         exp_name = "arrays"
         exp_id = "cse01" 
         overview = "overview"
         exp = Experiment(exp_name=exp_name, exp_id=exp_id, \
                              overview=overview, sections=[],
                              institute=inst, discipline=discipline,
                              integration_status=integration_status,
                              assets=[asset], developers=[dev],
                              hosting_info=[host])
         exp1 = self.persistence_delegate.add_experiment(exp)

         exp_name1 = "linked list"
         exp_id1 = "cse02"
         overview = "overview"
         exp1 = Experiment(exp_name=exp_name1, exp_id=exp_id1, \
                               overview=overview, sections=[],
                               institute=inst, discipline=discipline,
                               integration_status=integration_status,
                               assets=[asset], developers=[dev],
                               hosting_info=[host])
         exp2 = self.persistence_delegate.add_experiment(exp1)

         self.persistence_delegate.delete_experiment(exp_id)

         self.assertEqual(len(Experiment.get_all()), 1)

    def test_delete_institute(self):
         print "test_delete_institute"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Delhi"
         institute_id = "IITD"
         institute = Institute(institute_name=institute_name, institute_id=institute_id,
                                   assets=[asset])                    
         institute1 = self.persistence_delegate.add_institute(institute)

         institute_name1 = "IIT Kharagpur"
         institute_id1 = "IITKgp"
         institute1 = Institute(institute_name=institute_name1, institute_id=institute_id1,
                                    assets=[asset]) 
         institute2 = self.persistence_delegate.add_institute(institute1)

         self.persistence_delegate.delete_institute("IITD")

         self.assertEqual(len(Institute.get_all()), 1)

    def test_delete_discipline(self):
         print "test_delete_discipline"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         discipline_name = "IIT Delhi"
         discipline_id = "EEE08"
         dis = Discipline(discipline_name=discipline_name, discipline_id=discipline_id, assets=[asset])
         dis1 = self.persistence_delegate.add_discipline(dis)

         discipline_name1 = "IIT Kanpur"
         discipline_id1 = "EEE10"
         dis1 = Discipline (discipline_name=discipline_name1, discipline_id=discipline_id1, assets=[asset])
         dis2 = self.persistence_delegate.add_discipline(dis1)

         self.persistence_delegate.delete_discipline("EEE08")

         self.assertEqual(len(Discipline.get_all()), 1)

    def test_delete_hosting_info(self):
         print "test_delete_hosting_info"
         hosting_status = "hosted"
         hosted_url = "http://cse14-iiith.vlabs.ac.in"
         hosted_on = "cloud"
         hosting_info = HostingInfo(hosting_status=hosting_status,
                                        hosted_url=hosted_url,
                                        hosted_on=hosted_on)
         hosting_info = self.persistence_delegate.add_hosting_info(hosting_info)

         hosting_status1 = "not hosted"
         hosted_url1 = "http://iitkgp.vlab.co.in/"
         hosted_on1 = "server"
         hosting_info1 = HostingInfo(hosting_status=hosting_status1,
                                         hosted_url=hosted_url1,
                                         hosted_on=hosted_on1)
         hosting_info2 = self.persistence_delegate.add_hosting_info(
             hosting_info1)

         self.persistence_delegate.delete_hosting_info(
             "http://cse14-iiith.vlabs.ac.in")

         self.assertEqual(len(HostingInfo.get_all()), 1)

    def test_delete_asset(self):
         print "test_delete_asset"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/static/images/logo.png"
         asset = Asset(asset_type=asset_type, path=path)

         asset1 = self.persistence_delegate.add_asset(asset)

         asset_type1 = AssetType(asset_type="Icon")
         asset_type1.save()

         path1 = "vlabs.ac.in/static/images/icon.png"
         asset1 = Asset(asset_type=asset_type1, path=path1)

         asset2 = self.persistence_delegate.add_asset(asset1)

         self.persistence_delegate.delete_asset(path)

         self.assertEqual(len(Asset.get_all()), 1)
    def test_delete_integration_status(self):
         print "test_delete_integration_status"
         integration_level = 4
         integration_status = IntegrationStatus(integration_level=\
                                                    integration_level)         
         integration_status1 = self.persistence_delegate.add_integration_status\
         (integration_status)

         integration_level1 = 2
         integration_status1 = IntegrationStatus(integration_level=\
                                                     integration_level1)
         integration_status2 = self.persistence_delegate.\
           add_integration_status(integration_status1)

         self.persistence_delegate.delete_integration_status(integration_level)

         self.assertEqual(len(IntegrationStatus.get_all()), 1)


    def test_update_lab(self):
         print "test_update_lab"
         lab_name = "Data Structures"
         lab_id = "cse01"
         overview = "overview lab"
         experiments = []

         asset_type = AssetType(asset_type="Logo")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name,
                              institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "Electronics & Communications"
         discipline_id = "ECE"
         discipline = Discipline(discipline_name=discipline_name,
                                     discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()
      
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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()


         exp_name = "Data Structures"
         exp_id = "cse01"
         overview = "overview"
        
         exp = Experiment(exp_name=exp_name, exp_id=exp_id, \
                              overview=overview, sections=[],
                              institute=inst, discipline=discipline, 
                              integration_status=integration_status,
                              assets=[asset], developers=[dev],
                              hosting_info=[host])

         exp1 = self.persistence_delegate.add_experiment(exp)

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab = Lab(lab_name=lab_name, lab_id=lab_id, overview=overview, 
                       institute=inst, discipline=discipline, 
                       assets=[asset], hosting_info=[host], sections=[section],
                       experiments=[exp1], developers=[dev], 
                       integration_status=integration_status) 

         lab1 = self.persistence_delegate.add_lab(lab)
         lab_name1 = "Computer Programming"
         overview1 = "overview"

         institute_name1 = "IIT Kharagpur"
         institute_id1 = "IITKgp"
         inst1 = Institute(institute_name=institute_name1,
                               institute_id=institute_id1,
                               assets=[asset])
         inst1.save()

         discipline_name1 = "Computer Science & Engineering"
         discipline_id1 = "CSE"
         discipline1 = Discipline(discipline_name=discipline_name1,
                                      discipline_id=discipline_id1,
                                      assets=[asset])
         discipline1.save()

         integration_level1 = 2
         integration_status1 = IntegrationStatus(integration_level=\
                                                     integration_level1)
         integration_status1.save()

         hosting_status1 = "hosted"
         hosted_url1 = "http://cse13-iiith.vlabs.ac.in"
         hosted_on1 = "cloud"
         host1 = HostingInfo(hosting_status=hosting_status1,
                                 hosted_url=hosted_url1,
                                 hosted_on=hosted_on1)
         host1.save()

         dev_name1 = Name(name="Tahiliani")
         dev_name1.save()
         email_id1 = Email(email="tahiliani@gmail.com")
         email_id1.save()
         dev1 = Developer(name=dev_name1, email=email_id1)
         dev1.save()

         asset_type1 = AssetType(asset_type="Image")
         asset_type1.save()

         path1 = "vlabs.ac.in/images/static/image.png"
         asset1 = Asset(asset_type=asset_type1, path=path1)
         asset1.save()

         exp_name1 = "Computer Programming"
         exp_id1 = "cse02"
         overview1 = "computer overview"
        
         exp1 = Experiment(exp_name=exp_name1, exp_id=exp_id1, \
                              overview=overview1, sections=[],
                              institute=inst1, discipline=discipline1, 
                              integration_status=integration_status,
                              assets=[asset1], developers=[dev1],
                              hosting_info=[host1])

         exp2 = self.persistence_delegate.add_experiment(exp)

         lab2 = self.persistence_delegate.update_lab\
           (lab1, lab_name1, overview1, inst1, discipline1, [section],
                integration_status1, [host1], [dev1], [asset1], [exp2]),

         lab2 = Lab.get_by_id(1)

         self.assertEqual(lab2.get("lab_id"), lab_id)
         self.assertEqual(lab2.get("lab_name"), lab_name1)
         self.assertEqual(lab2.get("overview"), overview1)
         self.assertEqual(lab2.get("institute").get("institute_id"), 
                              inst1.get("institute_id"))
         self.assertEqual(lab2.get("discipline").get("discipline_id"), 
                              discipline1.get("discipline_id"))
         self.assertEqual(lab2.get("integration_status").
                              get("integration_level"), 
                              integration_status1.get("integration_level"))

         self.assertEqual(lab2.get("hosting_info")[0].get("hosted_url"), 
                              hosted_url1)
         self.assertEqual(lab2.get("developers")[0].get("email").get("email"), 
                              email_id1.get("email"))
         self.assertEqual(lab2.get("assets")[0].get("path"),
                              asset1.get("path"))
         self.assertEqual(lab2.get("experiments")[0].get("exp_id"),
                              exp2.get("exp_id"))


    def test_update_experiment(self):
         print "test_update_experiment"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name,
                              institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "computer science"
         discipline_id = "cse"
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
                                hosted_url=hosted_url, 
                                hosted_on=hosted_on)
         host.save()

         exp_name = "Data Structures"
         exp_id = "cse01"
         overview = "overview"

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

         name = "Theory"
         section = Section(name=name)
         section.save()
        
         exp = Experiment(exp_name=exp_name, exp_id=exp_id, \
                              overview=overview, sections=[section],
                              institute=inst, discipline=discipline, 
                              integration_status=integration_status,
                              assets=[asset], developers=[dev],
                              hosting_info=[host] )
         exp1 = self.persistence_delegate.add_experiment(exp)

         exp_name1 = "Computer Programming"
         overview1 = "overveiw exp"

         asset_type1 = AssetType(asset_type="Video")
         asset_type1.save()

         path1 = "vlabs.ac.in/images/video/logo.png"
         asset1 = Asset(asset_type=asset_type1, path=path1)
         asset1.save()

         institute_name1 = "IIT Kharagpur"
         institute_id1 = "IITKgp"
         inst1 = Institute(institute_name=institute_name1, institute_id=institute_id1,
                               assets=[asset1])
         inst1.save()

         discipline_name1 = "Electronics and Communication"
         discipline_id1 = "ece"
         discipline1 = Discipline(discipline_name=discipline_name1, discipline_id=discipline_id1,
                                      assets=[asset1])
         discipline1.save()

         dev_name1 = Name(name="Palavi Pawar")
         dev_name1.save()
         email_id1 = Email(email="pallavipawar@gmail.com")
         email_id1.save()
         dev1 = Developer(name=dev_name1, email=email_id1)
         dev1.save()

         integration_level1 = 3
         integration_status1 = IntegrationStatus(integration_level=
                                                     integration_level1)
         integration_status1.save()

         hosting_status1 = "hosted"
         hosted_url1 = "http://cse13-iiith.vlabs.ac.in"
         hosted_on1 = "cloud"
         host1 = HostingInfo(hosting_status=hosting_status1,
                                 hosted_url=hosted_url1,
                                 hosted_on=hosted_on1)
         host1.save()
         
         name1 = "Procedure"
         section1 = Section(name=name1)
         section1.save()

         exp2 = self.persistence_delegate.update_experiment(exp1, exp_name1,
                                         overview1, inst1, discipline1,
                                         integration_status1, [host1], 
                                         [dev1], [asset1], [section1])
         exp2 = Experiment.get_by_id(1)

         self.assertEqual(exp2.get("exp_name"), exp_name1)
         self.assertEqual(exp2.get("overview"), overview1)
         self.assertEqual(exp2.get("exp_id"), exp_id)
         self.assertEqual(exp2.get("institute").get("institute_id"), 
                              inst1.get("institute_id"))
         self.assertEqual(exp2.get("discipline").get("discipline_id"), 
                              discipline1.get("discipline_id"))
         self.assertEqual(exp2.get("integration_status").
                              get("integration_level"), 
                              integration_status1.get("integration_level"))
         self.assertEqual(exp2.get("hosting_info")[0].get("hosted_url"), 
                              hosted_url1)
         self.assertEqual(exp2.get("developers")[0].get("email").get("email"), 
                              email_id1.get("email"))
         self.assertEqual(exp2.get("assets")[0].get("path"),
                              asset1.get("path"))
         self.assertEqual(exp2.get("sections")[0].get("name"),
                              section1.get("name"))


    def test_update_section(self):
         print "test_update_section"
         name = "Theory"
         section = Section(name=name)
         section1 = self.persistence_delegate.add_section(section)
         name1 = "Procedure"         
         section2 = self.persistence_delegate.update_section\
           (section1, name1)
         section2 = Section.get_by_id(1)
         self.assertEqual(section2.get("name"), name1)

    def test_update_institute(self):
         print "test_update_institute"

         asset_type = AssetType(asset_type="Logo")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Delhi"
         institute_id = "IITD"
         institute = Institute(institute_name=institute_name, institute_id=institute_id,
                                   assets=[asset])
         institute1 = self.persistence_delegate.add_institute(institute)

         asset_type1 = AssetType(asset_type="Image")
         asset_type1.save()

         path1 = "vlabs.ac.in/images/static/image.png"
         asset1 = Asset(asset_type=asset_type1, path=path1)
         asset1.save()

         institute_name1 = "IIT Kanpur"
         institute2 = self.persistence_delegate.update_institute\
           (institute1, institute_name1, [asset1]),

         institute = Institute.get_by_id(1)

         self.assertEqual(institute.get("institute_name"), institute_name1)
         self.assertEqual(institute.get("institute_id"), institute_id)
         self.assertEqual(institute.get("assets")[0].get("path"),
                              asset1.get("path"))

    def test_update_discipline(self):
         print "test_update_discipline"

         asset_type = AssetType(asset_type="Logo")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         discipline_name = "IIT Delhi"
         discipline_id = "EEE08"
         dis = Discipline(discipline_name=discipline_name,
                              discipline_id=discipline_id, assets=[asset])
         dis1 = self.persistence_delegate.add_discipline(dis)

         asset_type1 = AssetType(asset_type="Image")
         asset_type1.save()
         path1 = "vlabs.ac.in/images/static/image.png"
         asset1 = Asset(asset_type=asset_type1, path=path1)
         asset1.save()

         discipline_name1 = "IIT Bombay"
         discipline_id1 = "EEE09"
         dis2 = self.persistence_delegate.update_discipline\
           (dis1, discipline_name1, [asset1]),
         dis2 = Discipline.get_by_id(1)
         self.assertEqual(dis2.get("discipline_name"), discipline_name1)
         self.assertEqual(dis2.get("discipline_id"), discipline_id)
         self.assertEqual(dis2.get("assets")[0].get("path"),
                              asset1.get("path"))

    def test_update_hosting_info(self):
         print "test_update_hosting_info"
         hosting_status = "hosted"
         hosted_url = "http://cse14-iiith.vlabs.ac.in"
         hosted_on = "cloud"
         hosting_info = HostingInfo(hosting_status=hosting_status,
                                        hosted_url=hosted_url,
                                        hosted_on=hosted_on)
         hosting_info1 = self.persistence_delegate.add_hosting_info(
             hosting_info)

         hosting_status1 = "not hosted"
         hosted_on1 = "server"
         hosting_info2 = self.persistence_delegate.update_hosting_info\
           (hosting_info1, hosting_status1, hosted_on1),

         hosting_info = HostingInfo.get_by_id(1)

         self.assertEqual(hosting_info.get("hosting_status"), hosting_status1)
         self.assertEqual(hosting_info.get("hosted_url"), hosted_url)
         self.assertEqual(hosting_info.get("hosted_on"), hosted_on1)

    def test_update_asset(self):
         print "test_update_asset"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/static/images/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asst1 = self.persistence_delegate.add_asset(asset)

         asset_type1 = AssetType(asset_type="Video")
         asset_type1.save()

         path1 = "vlabs.ac.in/static/images/icon.png"
         asst2 = self.persistence_delegate.update_asset\
           (asst1, asset_type1),
         asst2 = Asset.get_by_id(1)
         self.assertEqual(asst2.get("asset_type").get("asset_type"),
                              asset_type1.get("asset_type"))
         self.assertEqual(asst2.get("path"), path)


    def test_get_lab_by_id(self):
         print "test_persistence_get_lab_by_id"

         lab_name1="Computer Programming"
         lab_id1="CSE01"
         overview="overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab = Lab(lab_name=lab_name1, lab_id=lab_id1, overview=overview, 
                       institute=inst, discipline=discipline, 
                       hosting_info=[host], assets=[asset],
                       experiments=[], developers=[dev],sections=[section], 
                       integration_status=integration_status)
         lab.save()

         lab_obj = self.persistence_delegate.get_lab_by_id(1)
         self.assertEqual(lab_obj.get("lab_id"),
                              lab_id1)
         self.assertEqual(lab_obj.get("lab_name"), lab_name1)

    def test_get_experiment_by_id(self):
         print "test_persistence_get_experiment_by_id"

         hosting_status = "hosted"
         hosted_url = "http://cse14-iiith.vlabs.ac.in"
         hosted_on = "cloud"
         host = HostingInfo(hosting_status=hosting_status,
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         dev_name = Name(name="Mohit Tahiliani")
         dev_name.save()
         email_id = Email(email="mohit.tahiliani@gmail.com")
         email_id.save()
         dev = Developer(name=dev_name, email=email_id)
         dev.save()

         exp_name = "Number Systems"
         exp_id = "EE99777"
         overview = "overview"

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()
        
         exp = Experiment(exp_name=exp_name, exp_id=exp_id,
                              overview=overview, sections=[],
                         institute=inst, discipline=discipline, 
                              integration_status=integration_status,
                              assets=[asset], developers=[dev],
                              hosting_info=[host])
         exp.save()

         exp_obj = self.persistence_delegate.get_experiment_by_id(1)
         self.assertEqual(exp_obj.get("exp_id"),
                              exp_id)
         self.assertEqual(exp_obj.get("exp_name"), exp_name)

    def test_get_institute_by_id(self):
         print "test_persistence_get_institute_by_id"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id,
                              assets=[asset])      
         inst.save()

         inst_obj = self.persistence_delegate.get_institute_by_id(1)
         self.assertEqual(inst_obj.get("institute_id"), institute_id)
         self.assertEqual(inst_obj.get("institute_name"), institute_name)

    def test_get_discipline_by_id(self):
         print "test_persistence_get_discipline_by_id"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         discipline_name = "IIT Delhi"
         discipline_id = "EEE08"
         dis = Discipline(discipline_name=discipline_name,
                              discipline_id=discipline_id, assets=[asset])
         dis.save()

         dis_obj = self.persistence_delegate.get_discipline_by_id(1)
         self.assertEqual(dis_obj.get("discipline_id"), discipline_id)
         self.assertEqual(dis_obj.get("discipline_name"), discipline_name)



    def test_add_saved_experiments_to_lab(self):
         print "test_add_experiments_to_lab_in_persistence_delegate"

         lab_name="Data Structures"
         lab_id="CSE02"
         overview = "overview"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()


         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()

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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         name = "Theory"
         section = Section(name=name)
         section.save()

         lab = Lab(lab_name=lab_name, lab_id=lab_id, overview=overview,
                       institute=inst, discipline=discipline,
                       hosting_info=[host], assets=[asset],
                       experiments=[], developers=[dev], sections=[section],
                       integration_status=integration_status)

         lab.save()

         exp_name = "Number Systems"
         exp_id = "EE99777"
         overview = "overview"
         experiment = Experiment(exp_name=exp_name, exp_id=exp_id, \
                                     overview=overview, sections=[],
                                     institute=inst, discipline=discipline, 
                                     integration_status=integration_status,
                                     assets=[asset], developers=[dev],
                                     hosting_info=[host])
         experiment.save()
        
         lab1 = Lab.get_by_id(1)

         lab1 = self.persistence_delegate.add_experiments_to_lab(lab1.id, \
                                                             [experiment])
        
         self.assertEqual(len(lab1.get("experiments")), 1)
         self.assertEqual(lab1.get("experiments")[0].get("exp_id"), exp_id)
         self.assertEqual(lab1.get("experiments")[0].get("exp_name"),\
                                                      exp_name)

#    def test_add_saved_assets_to_lab(self):
#         print "test_add_assets_to_lab_in_persistence_delegate"
#
#         lab_name="Data Structures"
#         lab_id="CSE02"
#         overview = "overview"
#
#         asset_type = AssetType(asset_type="Image")
#         asset_type.save()
#
#         path = "vlabs.ac.in/images/static/logo.png"
#         asset = Asset(asset_type=asset_type, path=path)
#         asset.save()
#
#         institute_name = "IIT Kanpur"
#         institute_id = "IITK"
#         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
#         inst.save()
#
#         discipline_name = "IIT Kanpur"
#         discipline_id = "IITK"
#         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
#                                     assets=[asset])
#         discipline.save()
#
#         integration_level = 4
#         integration_status = IntegrationStatus(integration_level=
#                                                    integration_level)
#         integration_status.save()
#
#         dev_name = Name(name="Mohit Tahiliani")
#         dev_name.save()
#         email_id = Email(email="mohit.tahiliani@gmail.com")
#         email_id.save()
#         dev = Developer(name=dev_name, email=email_id)
#         dev.save()
#
#         hosting_status = "hosted"
#         hosted_url = "http://cse14-iiith.vlabs.ac.in"
#         hosted_on = "cloud"
#         host = HostingInfo(hosting_status=hosting_status,
#                                hosted_url=hosted_url,
#                                hosted_on=hosted_on)
#         host.save()
#
#         name = "Theory"
#         section = Section(name=name)
#         section.save()
#
#         lab = Lab(lab_name=lab_name, lab_id=lab_id, overview=overview,
#                       institute=inst, discipline=discipline,
#                       hosting_info=[host], assets=[asset],
#                       experiments=[], developers=[dev], sections=[section],
#                       integration_status=integration_status)
#
#         lab.save()
#
#         exp_name = "Number Systems"
#         exp_id = "EE99777"
#         overview = "overview"
#         experiment = Experiment(exp_name=exp_name, exp_id=exp_id, \
#                                     overview=overview, 
#                                     integration_status=integration_status, 
#                                     sections=[], assets=[asset],
#                                     developers=[dev], hosting_info=[host], 
#                                     institute=inst, discipline=discipline)
#         experiment.save()
#        
#         lab1 = Lab.get_by_id(1)
#
#         lab1 = self.persistence_delegate.add_assets_to_lab(lab, \
#                                                             [asset])
#        
#         self.assertEqual(len(lab1.get("assets")), 1)
#         self.assertEqual(lab1.get("assets")[0].get("path"), path)
#         self.assertEqual(lab1.get("assets")[0].get("asset_type"),\
#                                                      asset_type)
#
    def test_add_saved_sections_to_experiment(self):
         print "test_add_sections_to_experiment_in_persistence_delegate"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
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
                                hosted_url=hosted_url,
                                hosted_on=hosted_on)
         host.save()

         integration_level = 4
         integration_status = IntegrationStatus(integration_level=
                                                    integration_level)
         integration_status.save()
         
         exp_name = "Number Systems"
         exp_id = "EE99777"
         overview = "overview"
         exp = Experiment(exp_name=exp_name, exp_id=exp_id, \
                           overview=overview, institute=inst,
                           discipline=discipline, 
                           integration_status=integration_status, 
                           sections=[], assets=[asset],
                           developers=[dev], hosting_info=[host])
         exp.save()
        
         section1 = Section(name='Theory')
         section1.save()
         section2 = Section(name='Procedure')
         section2.save()

         exp1 = self.persistence_delegate.add_sections_to_experiment\
                                     (exp, [section1, section2])
        
         self.assertEqual(len(exp1.get("sections")), 2)
         self.assertEqual(exp1.get("sections")[0].get("name"), 'Theory')
         self.assertEqual(exp1.get("sections")[1].get("name"), 'Procedure')

#    def test_add_saved_labs_to_institute(self):
#         print "test_add_labs_to_institute_in_persistence_delegate"
#
#         asset_type = AssetType(asset_type="Image")
#         asset_type.save()
#
#         path = "vlabs.ac.in/images/static/logo.png"
#         asset = Asset(asset_type=asset_type, path=path)
#         asset.save()
#        
#         lab_name = "Data Structures"
#         lab_id = "cse05"
#         overview = "overview"
#
#         institute_name = "IIT Kanpur"
#         institute_id = "IITK"
#         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
#         inst.save()
#
#         discipline_name = "IIT Kanpur"
#         discipline_id = "IITK"
#         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
#                                     assets=[asset])
#         discipline.save()
#
#         integration_level = 4
#         integration_status = IntegrationStatus(integration_level=
#                                                    integration_level)
#         integration_status.save()
#
#         dev_name = Name(name="Mohit Tahiliani")
#         dev_name.save()
#         email_id = Email(email="mohit.tahiliani@gmail.com")
#         email_id.save()
#         dev = Developer(name=dev_name, email=email_id)
#         dev.save()
#
#         hosting_status = "hosted"
#         hosted_url = "http://cse14-iiith.vlabs.ac.in"
#         hosted_on = "cloud"
#         host = HostingInfo(hosting_status=hosting_status,
#                                hosted_url=hosted_url,
#                                hosted_on=hosted_on)
#         host.save()
#
#         name = "Theory"
#         section = Section(name=name)
#         section.save()
#
#         lab = Lab(lab_name=lab_name, lab_id=lab_id, overview=overview, 
#                       institute=inst, discipline=discipline,sections=[section],
#                       hosting_info=[host],  assets=[], experiments=[],
#                       developers=[dev], integration_status=integration_status)
#
#         lab.save()
#         
#         institute1 = Lab.get_by_id(1)
#
#         institute1 = self.persistence_delegate.add_labs_to_institute(
#             institute1.id, [lab])
#        
#         self.assertEqual(len(institute1.get("labs")), 1)
#         self.assertEqual(institute1.get("labs")[0].get("lab_id"), lab_id)
#         self.assertEqual(institute1.get("labs")[0].get("lab_name"),\
#                                                      lab_name)
#

    def test_add_name(self):
         print "test_add_name"
         name = "Prof. S. Dharmaraja"
         name = Name(name=name)
         name = self.persistence_delegate.add_name(name)
         name = name.get_by_id(1)
         self.assertEqual(name.get("name"), name.get("name"))

    def test_add_email(self):
         print "test_add_email"
         email = "dharmar@maths.iitd.ac.in"
         email = Email(email=email)
         email = self.persistence_delegate.add_email(email)
         email = email.get_by_id(1)
         self.assertEqual(email.get("email"), email.get("email"))

    def test_add_developer(self):
         print "test_add_developer"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
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

         dev_name = Name(name="Prof. S. Dharmaraja")
         dev_name.save()
         email = Email(email="dharmar@maths.iitd.ac.in")
         email.save()
         dev = Developer(name=dev_name, email=email)
         dev = self.persistence_delegate.add_developer(dev)
        
         self.assertEqual(self.persistence_delegate.developer_exists(dev),
                          True)

    def test_add_developer_without_saving_name(self):
         print "test_add_developer_without_saving_name"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
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

         dev_name = Name(name="Prof. S. Dharmaraja")
         email = Email(email="dharmar@maths.iitd.ac.in")
         email.save()
         dev = Developer(name=dev_name, email=email)
         dev = self.persistence_delegate.add_developer(dev)
        
         self.assertEqual(self.persistence_delegate.developer_exists(dev),
                          True)

    def test_add_developer_without_saving_email(self):
         print "test_add_developer_without_saving_email"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
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

         dev_name = Name(name="Prof. S. Dharmaraja")
         dev_name.save()
         email = Email(email="dharmar@maths.iitd.ac.in")
         dev = Developer(name=dev_name, email=email)
         dev = self.persistence_delegate.add_developer(dev)
        
         self.assertEqual(self.persistence_delegate.developer_exists(dev),
                          True)


    def test_update_developer(self):
         print "test_update_developer"

         dev_name = Name(name="Prof. S. Dharmaraja")
         dev_name.save()
         email_id = Email(email="dharmar@maths.iitd.ac.in")
         email_id.save()
         dev = Developer(name=dev_name, email=email_id)
         dev1 = self.persistence_delegate.add_developer(dev)

         dev_name1 = Name(name="Prof. S. raja")
         dev_name1.save()

         dev2 = self.persistence_delegate.update_developer(dev1, dev_name1)

         self.assertEqual(dev1.get("name").get("name"), dev_name1.get("name"))


    def test_delete_name(self):
         print "test_delete_name"
         name = "Prof. Dharmaraj"
         name = Name(name=name)
         name.save()

         name1 = "Prof. Yamraj"
         name2 = Name(name=name1)
         name2.save()

         self.persistence_delegate.delete_name(1)

         self.assertEqual(len(Name.get_all()), 1)

    def test_delete_email(self):
         email = Email(email="abc@gmail.com")
         email1 = self.persistence_delegate.add_email(email)

         email1 = Email(email="xyz@gmail.com")
         email2 = self.persistence_delegate.add_email(email1)

         self.persistence_delegate.delete_email(email)

         self.assertEqual(len(Email.get_all()), 1)

    def test_delete_developer(self):
         print "test_delete_developer"

         dev_name = Name(name="Prof. S. Dharmaraja")
         dev_name.save()

         email_id = Email(email="dharmar@maths.iitd.ac.in")
         email_id.save()

         dev = Developer(name=dev_name, email=email_id)
         dev1 = self.persistence_delegate.add_developer(dev)

         dev_name1 = Name(name="Prof. S. Yamraja")
         dev_name1.save()
         email_id1 = Email(email="yamraja@maths.iitd.ac.in")
         email_id1.save()

         dev2 = Developer(name=dev_name1, email=email_id1)
         dev3 = self.persistence_delegate.add_developer(dev2)

         self.persistence_delegate.delete_developer(dev3.get("email"))

         self.assertEqual(len(Developer.get_all()), 1)
         self.assertEqual(len(Email.get_all()), 1)



    def test_get_name(self):
         print "test_get_name"
         name = "Prof. Dharamaraja"
         name = Name(name=name)
         name.save()

         name_obj = self.persistence_delegate.get_name(name=
                                                name.get("name"))
         self.assertEqual(name_obj.get("name"),
                              name.get("name"))

    def test_get_email(self):
         print "test_get_email"
         email = "abc@gmail.com"
         email = Email(email=email)
         email.save()

         email_obj = self.persistence_delegate.get_email(email=
                                                email.get("email"))
         self.assertEqual(email_obj.get("email"),
                              email.get("email"))

    def test_get_developer(self):
         print "test_get_developer"

         asset_type = AssetType(asset_type="Image")
         asset_type.save()

         path = "vlabs.ac.in/images/static/logo.png"
         asset = Asset(asset_type=asset_type, path=path)
         asset.save()

         institute_name = "IIT Kanpur"
         institute_id = "IITK"
         inst = Institute(institute_name=institute_name, institute_id=institute_id, assets=[asset])
         inst.save()

         discipline_name = "IIT Kanpur"
         discipline_id = "IITK"
         discipline = Discipline(discipline_name=discipline_name, discipline_id=discipline_id,
                                     assets=[asset])
         discipline.save()
        
         dev_name = Name(name="Prof. S. Dharmaraja")
         dev_name.save()
         email_id = Email(email="dharmar@maths.iitd.ac.in")
         email_id.save()
         dev = Developer(name=dev_name, email=email_id)
         dev.save()

         dev_obj = self.persistence_delegate.get_developer(email=dev.
                                                               get("email"))
         self.assertEqual(dev_obj.get("email").get("email"), email_id.
                              get("email"))

    def test_update_name(self):
         print "test_update_name"
         n_name = "Prof. Dharamraj"
         name = Name(name=n_name)
         name1 = self.persistence_delegate.add_name(name)
         n_name1 = "Prof. Dharam"         
         name2 = self.persistence_delegate.update_name\
           (name1, n_name1)
         name2 = Name.get_by_id(1)
         self.assertEqual(name2.get("name"), n_name1)

if __name__ == '__main__':
    unittest.main()
