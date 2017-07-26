
# -*- coding: utf-8 -*-
import unittest
from flask_testing import TestCase
from runtime.rest.app import create_app
from sqlalchemy.exc import IntegrityError
from runtime.utils.class_persistence_template import db
from runtime.system.system_interface import *
from runtime.config.system_config import KEY
from flask import current_app
config = {
         'SQLALCHEMY_DATABASE_URI': ''
         }


#class TestAddLab(TestCase):
#   TESTING = True
#   def create_app(self):
#       app = create_app(config)
#       return app
#
#   def setUp(self):
#       db.create_all()
#
#   def tearDown(self):
#       db.session.remove()
#       db.drop_all()
#
#   def test_add_lab_in_system_interface(self):
#       print "test_add_lab_in_system_interface"
#
#       data_dict = {
#		   'key' : KEY,
#		   'integration_level': 4
#		   }
#
#       integration_status = SystemInterface.add_integration_status(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'asset_type': 'Image',
#		   'path': 'vlabs.ac.in/images/static/logo.png'
#		  }
#
#       asset = SystemInterface.add_asset(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'hosting_status': 'hosted',
#		   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
#		   'hosted_on': 'cloud'
#		  }
#
#       hosting_info = SystemInterface.add_hosting_info(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'institute_name': 'IIT Kanpur',
#		   'institute_id': 'IITK',
#		   		    "assets": [
#			{
#			  "asset_type": "image",
#			  "path": "vlabs.ac.in/images/static/logo.png"
#			}
#		      ]
#
#		   }
#
#       institute = SystemInterface.add_institute(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'discipline_name': 'computer science',
#		   'discipline_id': 'CSE',
#		   		    "assets": [
#			{
#			  "asset_type": "image",
#			  "path": "vlabs.ac.in/images/static/logo.png"
#			}
#		      ]
#
#		  }
#
#       discipline = SystemInterface.add_discipline(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'name': 'Prof. Dharamaja',
#		   'email': 'abc@gmail.com',
#		   'institute_id': 'IITK',
#		   'discipline_id': 'CSE'
#		  }
#
#       developer = SystemInterface.add_developer(data_dict)
#
#
#       data_dict = {
#		   "key": KEY,
#                   "experiment": {
#                     "id": "exp123",
#                     "name": "arrays",
#                     "discipline_id": "CSE",
#                     "institute_id": "IITK",
#                     "developers": [
#                       {
#                         "name": "Dinesh Malviya",
#                         "email": "xyz@gmail.com"
#                       },
#                       {
#                         "name": "Ashish Ahuja",
#                         "email": "abc@gmail.com"
#                       }
#                     ],
#                     "hosting_info": [
#                       {
#                         "hosting_status": "hosted",
#                         "hosted_on": "cloud",
#                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
#                       },
#                       {
#                         "hosting_status": "hosted",
#                         "hosted_on": "college-cloud",
#                         "hosted_url": "http://cse14-iiith.ac.in"
#                       }
#                     ],
#                     "integration_level": 4,
#                     "overview": "This experiments describes about parallel and distributed processing",
#                     "assets": [
#                       {
#                         "asset_type": "image",
#                         "path": "vlabs.ac.in/images/static/logo.png"
#                       },
#                       {
#                         "asset_type": "video",
#                         "path": "vlabs.ac.in/video/abc.mkv"
#                       }
#                     ],
#                     "sections": [
#                       "Introduction",
#                       "Objective",
#                       "Tutorial",
#                       "Illustration",
#                       "Experiment",
#                       "Observations",
#                       "Assignment",
#                       "References"
#                     ]
#                   }
#                 }
#
#
#       experiment = SystemInterface.add_experiment(data_dict)
#
#
#       data_dict = {
#		   "key" : KEY,
#                   "lab": {
#                     "id": "cse02",
#                     "name": "Computer Programming",
#                     "overview": "overview",
#                     "discipline_id": "CSE",
#                     "institute_id": "IITK",
#                     "developers": [
#                       {
#                         "name": "Dinesh Malviya",
#                         "email": "xyz@gmail.com"
#                       },
#                       {
#                         "name": "Ashish Ahuja",
#                         "email": "abc@gmail.com"
#                       }
#                     ],
#                     "hosting_info": [
#                       {
#                         "hosting_status": "hosted",
#                         "hosted_on": "cloud",
#                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
#                       },
#                       {
#                         "hosting_status": "hosted",
#                         "hosted_on": "college-cloud",
#                         "hosted_url": "http://cse14-iiith.ac.in"
#                       }
#                     ],
#                     "integration_level": 4,
#                     "assets": [
#                       {
#                         "asset_type": "image",
#                         "path": "vlabs.ac.in/images/static/logo.png"
#                       },
#                       {
#                         "asset_type": "video",
#                         "path": "vlabs.ac.in/video/abc.mkv"
#                       }
#                     ],
#                     "experiments": [
#                           "exp123"
#                         ],
#                     "sections": [
#                       {
#                         "name": "Procedure"
#                       }
#                     ]
#                   }
#                 }
#
#       lab = SystemInterface.add_lab(data_dict)
#       lab_cls = System.delegate.entities['lab']
#       lab = lab_cls.get_all()[0]
#
#       self.assertEqual(lab.get("lab_name"), data_dict['lab']['name'])
#       self.assertEqual(lab.get("lab_id"), data_dict['lab']['id'])
#       self.assertEqual(lab.get("institute").get("institute_id"),
#			    data_dict['lab']['institute_id'])
#       self.assertEqual(lab.get("integration_status").get("integration_level"),
#			    data_dict['lab']['integration_level'])
#       self.assertEqual(lab.get("discipline").get("discipline_id"),
#			    data_dict['lab']['discipline_id'])
#       self.assertEqual(lab.get("assets")[0].get("path"),
#			    'vlabs.ac.in/images/static/logo.png')
#       self.assertEqual(lab.get("hosting_info")[0].get("hosted_url"),
#			    'http://cse14-iiith.vlabs.ac.in')
#       self.assertEqual(lab.get("experiments")[0].get("exp_name"), 'arrays')
#       self.assertEqual(lab.get("experiments")[0].get("exp_id"), 'exp123')
#       self.assertEqual(lab.get("developers")[0].get("email").get("email"),
#                            'xyz@gmail.com')
#       self.assertEqual(lab.get("developers")[1].get("email").get("email"),
#                            'abc@gmail.com')
#       self.assertEqual(lab.get("sections")[0].get("name"),
#			    'Procedure')
#
#   def test_add_lab_raises_type_error_in_system_interface(self):
#       print "test_add_lab_raises_type_error_in_system_interface"
#
#       data_dict = {
#		   'key' : KEY,
#		   'integration_level': 4
#		   }
#
#       integration_status = SystemInterface.add_integration_status(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'asset_type': 'Image',
#		   'path': 'vlabs.ac.in/images/static/logo.png'
#		  }
#
#       asset = SystemInterface.add_asset(data_dict)
#
#       data_dict = {
#		   'hosting_status': 'hosted',
#		   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
#		   'hosted_on': 'cloud',
#		   'key' : KEY
#		  }
#
#       hosting_info = SystemInterface.add_hosting_info(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'institute_name': 'IIT Kanpur',
#		   'institute_id': 'IITK',
#		   		    "assets": [
#			{
#			  "asset_type": "image",
#			  "path": "vlabs.ac.in/images/static/logo.png"
#			}
#		      ]
#
#		   }
#
#       institute = SystemInterface.add_institute(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'discipline_name': 'computer science',
#		   'discipline_id': 'CSE',
#		   		    "assets": [
#			{
#			  "asset_type": "image",
#			  "path": "vlabs.ac.in/images/static/logo.png"
#			}
#		      ]
#
#		  }
#
#       discipline = SystemInterface.add_discipline(data_dict)
#
#       data_dict = {
#		   'key' : KEY,
#		   'name': 'Prof. Dharamaja',
#		   'email': 'abc@gmail.com'
#		  }
#
#       developer = SystemInterface.add_developer(data_dict)
#       
#       data_dict = {
#		   'key' : KEY,
#		   'name': 'Procedure'
#		  }
#
#       section = SystemInterface.add_section(data_dict)
#
#       data_dict = {
#		   "key": KEY,
#                   "experiment": {
#                     "id": "exp123",
#                     "name": "arrays",
#                     "discipline_id": "CSE",
#                     "institute_id": "IITK",
#                     "developers": [
#                       {
#                         "name": "Dinesh Malviya",
#                         "email": "xyz@gmail.com"
#                       },
#                       {
#                         "name": "Ashish Ahuja",
#                         "email": "abc@gmail.com"
#                       }
#                     ],
#                     "hosting_info": [
#                       {
#                         "hosting_status": "hosted",
#                         "hosted_on": "cloud",
#                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
#                       },
#                       {
#                         "hosting_status": "hosted",
#                         "hosted_on": "college-cloud",
#                         "hosted_url": "http://cse14-iiith.ac.in"
#                       }
#                     ],
#                     "integration_level": 4,
#                     "overview": "This experiments describes about parallel and distributed processing",
#                     "assets": [
#                       {
#                         "asset_type": "image",
#                         "path": "vlabs.ac.in/images/static/logo.png"
#                       },
#                       {
#                         "asset_type": "video",
#                         "path": "vlabs.ac.in/video/abc.mkv"
#                       }
#                     ],
#                     "sections": [
#                       "Introduction",
#                       "Objective",
#                       "Tutorial",
#                       "Illustration",
#                       "Procedure",
#                       "Experiment",
#                       "Observations",
#                       "Assignment",
#                       "References"
#                     ]
#                   }
#                 }
#
#       experiment = SystemInterface.add_experiment(data_dict)
#
#       data_dict = {
#           "key" : KEY,     
#	   "lab": {
#	       "id": "cse02",
#	       "name": "Computer Programming",
#               "overview": "overview",
#	       "discipline_id": "CSE",
#	       "institute_id": "IIITH",
#	       "developers": [
#		   {
#		       "name": "Dinesh Malviya",
#		       "email": "xyz@gmail.com"
#		   },
#		   {
#		       "name": "Ashish Ahuja",
#		       "email": "abc@gmail.com"
#		   }
#	       ],
#	       "hosting_info": [
#		   {
#		       "hosting_status": "hosted",
#		       "hosted_on": "cloud",
#		       "hosted_url": "http://cse14-iiith.vlabs.ac.in"
#		   },
#		   {
#		       "hosting_status": "hosted",
#		       "hosted_on": "college-cloud",
#		       "hosted_url": "http://cse14-iiith.ac.in"
#		   }
#	       ],
#	       "integration_level": 4,
#	       "assets": [
#		   {
#		       "asset_type": "image",
#		       "path": "vlabs.ac.in/images/static/logo.png"
#		   },
#		   {
#		       "asset_type": "video",
#		       "path": "vlabs.ac.in/video/abc.mkv"
#		   }
#	       ],
#	       "experiments": [
#		       "exp123"
#	       ],
#
#	       "sections": [
#		   {
#		       "name": "Procedure"
#		   }
#		   
#		   
#	       ]
#	   }
#       }
#
#
#       with self.assertRaises(TypeError):
#	   SystemInterface.add_lab(data_dict)
#
class TestAddExperiment(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_experiment_in_system_interface(self):
        print "test_add_experiment_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                    }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Theory'
                    }
        section = SystemInterface.add_section(data_dict)
        
        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }
        experiment = SystemInterface.add_experiment(data_dict)
        
        self.assertEqual(experiment.get("exp_name"), 
                             data_dict['experiment']['name'])
        self.assertEqual(experiment.get("exp_id"),
                             data_dict['experiment']['id'])
        self.assertEqual(experiment.get("institute").get("institute_id"),
                             data_dict['experiment']['institute_id'])
        self.assertEqual(experiment.get("discipline").get("discipline_id"),
                             data_dict['experiment']['discipline_id'])
        self.assertEqual(experiment.get("integration_status").get("integration_level"),
                             data_dict['experiment']['integration_level'])
        self.assertEqual(experiment.get("assets")[0].get("path"), 
                             'vlabs.ac.in/images/static/logo.png')
        self.assertEqual(experiment.get("hosting_info")[0].get("hosted_url"),
                             'http://cse14-iiith.ac.in')
        self.assertEqual(experiment.get("developers")[0].get("email").\
                             get("email"), 'xyz@gmail.com')
        self.assertEqual(experiment.get("developers")[1].get("email").\
                             get("email"), 'abc@gmail.com')
        self.assertEqual(experiment.get("sections")[0].get("name"), 'Introduction')

    def test_add_experiment_raises_type_error_in_system_interface(self):
        print "test_add_experiment_raises_type_error_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Procedure'
                    }
        section = SystemInterface.add_section(data_dict)


        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }
        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": 123,
                      "overview":"overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "cloud",
			  "hosted_url": "http://cse14-iiith.vlabs.ac.in"
			},
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  } 
        with self.assertRaises(TypeError):
            SystemInterface.add_experiment(data_dict)
class TestAddInstitute(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_institute_in_system_interface(self):
        print "test_add_institute_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                    }
        institute = SystemInterface.add_institute(data_dict)
        institute_cls = System.delegate.entities['institute']
        institute = institute_cls.get_all()[0]

        self.assertEqual(institute.get("institute_name"), 
                             data_dict['institute_name'])
        self.assertEqual(institute.get("institute_id"), data_dict['institute_id'])
        self.assertEqual(institute.get("assets")[0].get("path"), 
                             'vlabs.ac.in/images/static/logo.png')

#    def test_add_institute_raises_type_error_in_system_interface(self):
#        print "test_add_institute_raises_type_error_in_system_interface"
 
#        data_dict = {
#                    'key' : KEY,
#                    'asset_type': 'Image',
#                    'path': 'vlabs.ac.in/images/static/logo.png'
#                   }

#        asset = SystemInterface.add_asset(data_dict)
       
#        data_dict = {
#                    'key' : KEY,
#                    'institute_name': 'IIT Kanpur',
#                    'institute_id': 123,
#                    		    "assets": [
#			{
#			  "asset_type": "image",
#			  "path": "vlabs.ac.in/images/static/logo.png"
#			}
#		      ]

#                    }
#        with self.assertRaises(TypeError):
#            SystemInterface.add_institute(data_dict)

class TestAddDiscipline(TestCase):

    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_discipline_in_system_interface(self):
        print "test_add_discipline_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'array',
                    'discipline_id': 'cse02',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                   }

        discipline = SystemInterface.add_discipline(data_dict)

        self.assertEqual(discipline.get("discipline_name"), 
                             data_dict['discipline_name'])
        self.assertEqual(discipline.get("discipline_id"), data_dict['discipline_id'])
        self.assertEqual(discipline.get("assets")[0].get("path"), 
                             'vlabs.ac.in/images/static/logo.png')
        
    def test_add_discipline_raises_type_error_in_system_interface(self):
        print "test_add_discipline_raises_type_error_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'cse02',
                    'discipline_id': 123,
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

		    }
        with self.assertRaises(TypeError):
            SystemInterface.add_discipline(data_dict)

class TestAddSection(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_section_in_system_interface(self):
        print "test_add_section_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name' : 'Theory'
                   }

        section = SystemInterface.add_section(data_dict)

        self.assertEqual(section.get("name"), 
                             data_dict['name'])
        
    def test_add_section_raises_type_error_in_system_interface(self):
        print "test_add_section_raises_type_error_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name' : 123
		    }
        with self.assertRaises(TypeError):
            SystemInterface.add_section(data_dict)
class TestAddName(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_name_in_system_interface(self):
        print "test_add_name_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'name' : 'Prof. S. Dharmaraja'
                   }

        name = SystemInterface.add_name(data_dict)

        self.assertEqual(name.get("name"), 
                             data_dict['name'])
        
    def test_add_name_raises_type_error_in_system_interface(self):
        print "test_add_name_raises_type_error_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'name' : 123
		    }
        with self.assertRaises(TypeError):
            SystemInterface.add_name(data_dict)
class TestAddEmail(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_email_in_system_interface(self):
        print "test_add_email_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'email' : 'dharmar@maths.iitd.ac.in'
                   }

        email = SystemInterface.add_email(data_dict)

        self.assertEqual(email.get("email"), 
                             data_dict['email'])
        
    def test_add_email_raises_type_error_in_system_interface(self):
        print "test_add_email_raises_type_error_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'email' : 123
		    }
        with self.assertRaises(TypeError):
            SystemInterface.add_email(data_dict)
class TestAddDeveloper(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_developer_in_system_interface(self):
        print "test_add_developer_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        self.assertEqual(developer.get("name").get("name"),
                             data_dict['name'])
        self.assertEqual(developer.get("email").get("email"),
                             data_dict['email'])

    def test_add_developer_raises_type_error_in_system_interface(self):
        print "test_add_developer_raises_type_error_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'name': 'Prof. S. Dharmaraja',
                    'email': 123456
		    }

        with self.assertRaises(TypeError):
            SystemInterface.add_developer(data_dict)
class TestAddHosting_Info(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_hosting_info_in_system_interface(self):
        print "test_add_hosting_info_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                    }

        hosting_info = SystemInterface.add_hosting_info(data_dict)
        hosting_info_cls = System.delegate.entities['hosting_info']
        hosting_info = hosting_info_cls.get_all()[0]

        self.assertEqual(hosting_info.get("hosting_status"),
                             data_dict['hosting_status'])
        self.assertEqual(hosting_info.get("hosted_url"), data_dict['hosted_url'])
        self.assertEqual(hosting_info.get("hosted_on"), data_dict['hosted_on'])

class TestAddIntegration_Status(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_integration_status_in_system_interface(self):
        print "test_add_integration_status_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)
        integration_status_cls = System.delegate.entities['integration_status']
        integration_status = integration_status_cls.get_all()[0]

        self.assertEqual(integration_status.get("integration_level"), 
                             data_dict['integration_level'])


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

    def test_delete_lab_in_system_interface(self):
        print "test_delete_lab_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)
        
        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)


        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
 		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)
 
        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)


        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse1-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {
           "key" : KEY,     
	   "lab": {
	       "id": "cse02",
	       "name": "Computer Programming",
               "overview": "overview",
	       "discipline_id": "CSE",
	       "institute_id": "IITK",
	       "developers": [
		   {
		       "name": "Dinesh Malviya",
		       "email": "xyz@gmail.com"
		   },
		   {
		       "name": "Ashish Ahuja",
		       "email": "abc@gmail.com"
		   }
	       ],
	       "hosting_info": [
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "cloud",
		       "hosted_url": "http://cs14-iiith.vlabs.ac.in"
		   },
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "college-cloud",
		       "hosted_url": "http://cse14-iiith.co.in"
		   }
	       ],
	       "integration_level": 4,
	       "assets": [
		   {
		       "asset_type": "image",
		       "path": "vlabs.ac.in/images/static/logo.png"
		   },
		   {
		       "asset_type": "video",
		       "path": "vlabs.ac.in/video/abc.mkv"
		   }
	       ],
	       "sections": [
		   {
		       "name": "Introduction"
		   }
		   		   
	       ],
		       "experiments": [
			   "exp123"
		       ]

	   }
       }


        data_dict1 = {
               "key" : KEY,     
               "lab": {
                   "id": "cse03",
                   "name": "Computer Programming",
                   "overview": "overview",
                   "discipline_id": "CSE",
                   "institute_id": "IITK",
                   "developers": [
                       {
                           "name": "Dinesh Malviya",
                           "email": "xyz@gmail.com"
                       },
                       {
                           "name": "Ashish Ahuja",
                           "email": "abc@gmail.com"
                       }
                   ],
                   "hosting_info": [
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "cloud",
                           "hosted_url": "http://ce14-iiith.vlabs.ac.in"
                       },
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "college-cloud",
                           "hosted_url": "http://se14-iiith.ac.in"
                       }
                   ],
                   "integration_level": 4,
                   "assets": [
                       {
                           "asset_type": "image",
                           "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                           "asset_type": "video",
                           "path": "vlabs.ac.in/video/abc.mkv"
                       }
                   ],
                   "sections": [
                       {
                           "name": "Introduction"
                       }
                                              
                   ],
                   "experiments": [
                   "exp123"
                   ]

               }
           }

        lab = SystemInterface.add_lab(data_dict)
        lab1 = SystemInterface.add_lab(data_dict1)
        lab_id = SystemInterface.delete_lab("cse02", KEY)
        
        self.assertEqual(lab_id, "cse02")

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

    def test_delete_experiment_in_system_interface(self):
        print "test_delete_experiment_in_system_interface"

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)


        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)
      
        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)
        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        data_dict1 = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp23",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        exp = SystemInterface.add_experiment(data_dict)
        exp1 = SystemInterface.add_experiment(data_dict1)
        exp_id = SystemInterface.delete_experiment('exp123', KEY)
        
        self.assertEqual(exp_id, 'exp123')

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

    def test_delete_institute_in_system_interface(self):
        print "test_delete_institute_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                    }

        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]
                     }

        institute = SystemInterface.add_institute(data_dict)
        institute1 = SystemInterface.add_institute(data_dict1)
        institute_id = SystemInterface.delete_institute("IITKgp", KEY)
        
        self.assertEqual(institute_id, "IITKgp")

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

    def test_delete_section_in_system_interface(self):
        print "test_delete_section_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name': 'Quiz'
                   }

        data_dict1 = {
                    'key' : KEY,
                    'name' : 'Theory'
                   }

        exp = SystemInterface.add_section(data_dict)
        exp1 = SystemInterface.add_section(data_dict1)
        s_id = SystemInterface.delete_section(1)
        
        self.assertEqual(s_id, 1)

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

    def test_delete_discipline_name_in_system_interface(self):
        print "test_update_discipline_name_in_system_interface"

        data_dict = {'discipline_name': 'Computer Science',
                    'discipline_id': 'CSE',
                    'key' : KEY,
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                    }

        data_dict1 = {'discipline_name': 'Electronics and Communication',
                    'discipline_id': 'ECE',
                    'key' : KEY,
		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]
                    }

        dis = SystemInterface.add_discipline(data_dict)
        dis1 = SystemInterface.add_discipline(data_dict1)
        discipline_id = SystemInterface.delete_discipline('ECE', KEY)

        self.assertEqual(discipline_id,'ECE')

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

    def test_delete_hosting_info_in_system_interface(self):
        print "test_delete_hosting_info_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                    }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict1 = {
                    'key' : KEY,
                    'hosting_status': 'not hosted',
                    'hosted_url': 'http://cse12-iiith.vlabs.ac.in',
                    'hosted_on': 'server'
                     }
        hosting_info1 = SystemInterface.add_hosting_info(data_dict1)
        hosted_url = SystemInterface.delete_hosting_info("http://cse14-iiith.vlabs.ac.in", KEY)
        
        self.assertEqual(hosted_url, "http://cse14-iiith.vlabs.ac.in")

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

    def test_delete_integration_status_in_system_interface(self):
        print "test_delete_integration_status_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        data_dict1 = {
                    'key' : KEY,
                    'integration_level': 2
                     }

        integration_status = SystemInterface.add_integration_status(data_dict)
        integration_status1 = SystemInterface.add_integration_status(data_dict1)
        integration_level = SystemInterface.delete_integration_status(2, KEY)
        
        self.assertEqual(integration_level, 2)


class TestGetLabs(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_in_system_interface(self):
        print "test_get_labs_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)
        
        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com',
		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse02",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                         "asset_type": "video",
                         "path": "vlabs.ac.in/video/abc.mkv"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Procedure"
                       }                       
                     ],
                         "experiments": [
                           "exp123"
                         ]

                   }
                 }

        data_dict1 = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse03",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                         "asset_type": "video",
                         "path": "vlabs.ac.in/video/abc.mkv"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }
                                              
                     ],
                         "experiments": [
                           "exp123"
                         ]

                   }
                 }

        lab1 = SystemInterface.add_lab(data_dict)
        lab2 = SystemInterface.add_lab(data_dict1)

        lab_list = SystemInterface.get_labs()
        
        self.assertEqual(lab_list[0].get("lab_name"), data_dict['lab']['name'])
        self.assertEqual(lab_list[1].get("lab_name"), data_dict1['lab']['name'])
        self.assertEqual(lab_list[0].get("lab_id"), 
                             data_dict['lab']['id'])
        self.assertEqual(lab_list[1].get("lab_id"), 
                             data_dict1['lab']['id'])

class TestGetSections(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_section_in_system_interface(self):
        print "test_get_section_in_system_interface"

        data_dict = {'name': 'Theory',
                    'key' : KEY
                   }

        data_dict1 = {'name': 'Aim',
                     'key' : KEY
                     }

        section1 = SystemInterface.add_section(data_dict)
        section2 = SystemInterface.add_section(data_dict1)

        section_list = SystemInterface.get_sections()
        
        self.assertEqual(section_list[0].get("name"), data_dict['name'])
        self.assertEqual(section_list[1].get("name"), data_dict1['name'])

class TestGetExperiments(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_experiments_in_system_interface(self):
        print "test_get_experiments_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)
          
        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)  

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute1 = SystemInterface.add_institute(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'discipline_name': 'electronics and communication',
                    'discipline_id': 'ECE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline1 = SystemInterface.add_discipline(data_dict1)

        data_dict1 = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99848",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        exp1 = SystemInterface.add_experiment(data_dict)
        exp2 = SystemInterface.add_experiment(data_dict1)

        exp_list = SystemInterface.get_experiments()
        
        self.assertEqual(exp_list[0].get("exp_name"), data_dict['experiment']['name'])
        self.assertEqual(exp_list[1].get("exp_name"), data_dict1['experiment']['name'])
        self.assertEqual(exp_list[0].get("exp_id"), 
                             data_dict['experiment']['id'])
        self.assertEqual(exp_list[1].get("exp_id"), 
                             data_dict1['experiment']['id'])

class TestGetInstitutes(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_institutes_in_system_interface(self):
        print "test_get_institutes_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
,
                    'key' : KEY
                    }

        data_dict1 = {'institute_name': "IIT Delhi",
                     'institute_id': 'IITD',
                     		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
,
                     'key' : KEY
                     }

        inst1 = SystemInterface.add_institute(data_dict)
        inst2 = SystemInterface.add_institute(data_dict1)

        inst_list = SystemInterface.get_institutes()
        
        self.assertEqual(inst_list[0].get("institute_name"), data_dict['institute_name'])
        self.assertEqual(inst_list[1].get("institute_name"), data_dict1['institute_name'])
        self.assertEqual(inst_list[0].get("institute_id"), 
                             data_dict['institute_id'])
        self.assertEqual(inst_list[1].get("institute_id"), 
                             data_dict1['institute_id'])

class TestGetDisciplines(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_disciplines_in_system_interface(self):
        print "test_get_disciplines_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                    }

        asset = SystemInterface.add_asset(data_dict)


        data_dict = {'discipline_name': 'data structure',
                    'discipline_id': 'cse01',
                    'key' : KEY,
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        data_dict1 = {'discipline_name': "Automata",
                      'discipline_id': 'DFA',
                      'key' : KEY,
                      		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                      }

        dis = SystemInterface.add_discipline(data_dict)
        dis1 = SystemInterface.add_discipline(data_dict1)

        dis_list = SystemInterface.get_disciplines()
        
        self.assertEqual(dis_list[0].get("discipline_name"), data_dict["discipline_name"])
        self.assertEqual(dis_list[1].get("discipline_name"), data_dict1["discipline_name"])
        self.assertEqual(dis_list[0].get("discipline_id"), 
                             data_dict["discipline_id"])
        self.assertEqual(dis_list[1].get("discipline_id"), 
                             data_dict1["discipline_id"])

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

    def test_get_hosting_info_in_system_interface(self):
        print "test_get_hosting_info_in_system_interface"

        data_dict = {'hosting_status': 'hosted',
                     'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                     'hosted_on': 'cloud',
                     'key' : KEY
                    }

        data_dict1 = {'hosting_status': 'not hosted',
                      'hosted_url': 'http://cse12-iiith.vlabs.ac.in',
                      'hosted_on': 'server',
                      'key' : KEY
                     }

        host1 = SystemInterface.add_hosting_info(data_dict)
        host2 = SystemInterface.add_hosting_info(data_dict1)

        host_list = SystemInterface.get_hosting_info()
        
        self.assertEqual(host_list[0].get("hosting_status"), data_dict['hosting_status'])
        self.assertEqual(host_list[1].get("hosting_status"), data_dict1['hosting_status'])
        self.assertEqual(host_list[0].get("hosted_url"), data_dict['hosted_url'])
        self.assertEqual(host_list[1].get("hosted_url"), data_dict1['hosted_url'])
        self.assertEqual(host_list[0].get("hosted_on"), data_dict['hosted_on'])
        self.assertEqual(host_list[1].get("hosted_on"), data_dict1['hosted_on'])


class TestGetAssets(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_assets_in_system_interface(self):
        print "test_get_assets_in_system_interface"
        
        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict1 = {
                     'key' : KEY,
                     'asset_type': 'Video',
                     'path': 'vlabs.ac.in/images/static/icon.png'
                     }

        asset1 = SystemInterface.add_asset(data_dict1)
        
        asset_dict_list = SystemInterface.get_assets()
        
        self.assertEqual(asset_dict_list[0].get("asset_type")["asset_type"],
                             data_dict['asset_type'])
        self.assertEqual(asset_dict_list[1].get("asset_type")["asset_type"],
                             data_dict1['asset_type'])
        self.assertEqual(asset_dict_list[0].get("path"), 
                             data_dict['path'])
        self.assertEqual(asset_dict_list[1].get("path"), 
                             data_dict1['path'])


class TestGetLabById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_lab_by_id_in_system_interface(self):
        print "test_get_lab_by_id_in_system_interface"

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)
       
        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Icon',
                    'path': 'vlabs.ac.in/images/static/icon.png'
                   }

        asset2 = SystemInterface.add_asset(data_dict)

        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {
           "key" : KEY,     
           "lab": {
	       "id": "cse02",
	       "name": "Computer Programming",
               "overview": "overview",
	       "discipline_id": "CSE",
	       "institute_id": "IITK",
	       "developers": [
		   {
		       "name": "Dinesh Malviya",
		       "email": "xyz@gmail.com"
		   },
		   {
		       "name": "Ashish Ahuja",
		       "email": "abc@gmail.com"
		   }
	       ],
	       "hosting_info": [
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "cloud",
		       "hosted_url": "http://cse1-iiith.vlabs.ac.in"
		   },
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "college-cloud",
		       "hosted_url": "http://cse4-iiith.ac.in"
		   }
	       ],
	       "integration_level": 4,
	       "assets": [
		   {
		       "asset_type": "logo",
		       "path": "vlabs.ac.in/images/static/logo.png"
		   },
		   {
		       "asset_type": "video1",
		       "path": "vlabs.ac.in/video/abc.mkv"
		   }
	       ],
	       "experiments": [
			   "exp123"
		       ],
	       "sections": [
		   {
		       "name": "Introduction"
		   }
	       ]
	   }
       }


        data_dict1 = {
               "key" : KEY,     
               "lab": {
               "id": "cse03",
               "name": "Computer Programming",
                   "overview": "overview",
               "discipline_id": "CSE",
               "institute_id": "IITK",
               "developers": [
               {
                   "name": "Dinesh Malviya",
                   "email": "xyz@gmail.com"
               },
               {
                   "name": "Ashish Ahuja",
                   "email": "abc@gmail.com"
               }
               ],
               "hosting_info": [
               {
                   "hosting_status": "hosted",
                   "hosted_on": "cloud",
                   "hosted_url": "http://ce14-iiith.vlabs.ac.in"
               },
               {
                   "hosting_status": "hosted",
                   "hosted_on": "college-cloud",
                   "hosted_url": "http://cs14-iiith.ac.in"
               }
               ],
               "integration_level": 4,
               "assets": [
               {
                   "asset_type": "logo1",
                   "path": "vlabs.ac.in/images/static/logo.png"
               },
               {
                   "asset_type": "video2",
                   "path": "vlabs.ac.in/video/abc.mkv"
               }
               ],
               "sections": [
               {
                   "name": "Introduction"
               }
               
               ],
               "experiments": [
                   "exp123"
                   ]

           }
           }

        lab1 = SystemInterface.add_lab(data_dict)
        lab2 = SystemInterface.add_lab(data_dict1)

        lab_data_one = SystemInterface.get_lab_by_id(1)
        lab_data_two = SystemInterface.get_lab_by_id(2)
        
        self.assertEqual(lab_data_one.get("lab_name"), data_dict['lab']['name'])
        self.assertEqual(lab_data_two.get("lab_name"), data_dict1['lab']['name'])
        self.assertEqual(lab_data_one.get("lab_id"), 
                             data_dict['lab']['id'])
        self.assertEqual(lab_data_two.get("lab_id"), 
                             data_dict1['lab']['id'])


class TestGetExperimentById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_experiment_by_id_in_system_interface(self):
        print "test_get_experiment_by_id_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute1 = SystemInterface.add_institute(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'discipline_name': 'electronics and communication',
                    'discipline_id': 'ECE',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline1 = SystemInterface.add_discipline(data_dict1)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)
    
        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        data_dict1 = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99848",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        exp1 = SystemInterface.add_experiment(data_dict)
        exp2 = SystemInterface.add_experiment(data_dict1)

        exp_data_one = SystemInterface.get_experiment_by_id(1)
        exp_data_two = SystemInterface.get_experiment_by_id(2)
        
        self.assertEqual(exp_data_one.get("exp_name"), data_dict['experiment']['name'])
        self.assertEqual(exp_data_two.get("exp_name"), data_dict1['experiment']['name'])
        self.assertEqual(exp_data_one.get("exp_id"), data_dict['experiment']['id'])
        self.assertEqual(exp_data_two.get("exp_id"), data_dict1['experiment']['id'])
      
class TestGetInstituteById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_institute_by_id_in_system_interface(self):
        print "test_get_institute_by_id_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)


        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Delhi',
                    'institute_id': 'IITD',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        inst1 = SystemInterface.add_institute(data_dict)
        inst2 = SystemInterface.add_institute(data_dict1)

        inst_data_one = SystemInterface.get_institute_by_id(1)
        inst_data_two = SystemInterface.get_institute_by_id(2)
        
        self.assertEqual(inst_data_one.get("institute_name"), data_dict['institute_name'])
        self.assertEqual(inst_data_two.get("institute_name"), data_dict1['institute_name'])
        self.assertEqual(inst_data_one.get("institute_id"), 
                             data_dict['institute_id'])
        self.assertEqual(inst_data_two.get("institute_id"), 
                             data_dict1['institute_id'])

class TestGetSectionById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_section_by_id_in_system_interface(self):
        print "test_get_section_by_id_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name' : "Theory"
                   }

        data_dict1 = {
                    'key' : KEY,
                    'name' : "Quiz"
                   }

        section1 = SystemInterface.add_section(data_dict)
        section2 = SystemInterface.add_section(data_dict1)

        section_data_one = SystemInterface.get_section_by_id(1)
        section_data_two = SystemInterface.get_section_by_id(2)
        
        self.assertEqual(section_data_one.get("name"), data_dict['name'])
        self.assertEqual(section_data_two.get("name"), data_dict1['name'])


class TestUpdateLab(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_lab_in_system_interface(self):
        print "test_update_lab_name_in_system_interface"

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key': KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)


        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        experiment = SystemInterface.add_experiment(data_dict)


        data_dict = {
           "key" : KEY,
           "lab": {
	       "id": "cse03",
	       "name": "Computer Programming",
               "overview": "overview",
	       "discipline_id": "CSE",
	       "institute_id": "IITK",
	       "developers": [
		   {
		       "name": "Dinesh Malviya",
		       "email": "xyz@gmail.com"
		   },
		   {
		       "name": "Ashish Ahuja",
		       "email": "abc@gmail.com"
		   }
	       ],
	       "hosting_info": [
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "cloud",
		       "hosted_url": "http://cse14-iiith.vlabs.ac.in"
		   },
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "college-cloud",
		       "hosted_url": "http://cse14-iiith.ac.in"
		   }
	       ],
	       "integration_level": 4,
	       "assets": [
		   {
		       "asset_type": "image",
		       "path": "vlabs.ac.in/images/static/logo.png"
		   },
		   {
		       "asset_type": "video",
		       "path": "vlabs.ac.in/video/abc.mkv"
		   }
	       ],
	       "sections": [
		   {
		       "name": "Introduction"
		   }
		   
	       ],
		       "experiments": [
			   "exp123"
		       ]

	   }
        }
        lab = SystemInterface.add_lab(data_dict)


        data_dict1 = {
                    'key': KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'discipline_name': 'electronics engineering',
                    'discipline_id': 'ECE',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                    }

        discipline = SystemInterface.add_discipline(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'integration_level': 3
                    }

        integration_status = SystemInterface.add_integration_status(data_dict1)


        data_dict1 = {
           "key" : KEY,
           "experiment": {
              "id": "exp1234",
              "overview": "overview",
              "name": "Parallel and distributed processing",
              "discipline_id": "CSE",
              "institute_id": "IITK",
              "developers": [
                 {
                    "name": "Dinesh Malviya",
                    "email": "xyz@gmail.com"
                 },
                 {
                    "name": "Ashish Ahuja",
                    "email": "abc@gmail.com"
                 }
              ],
              "hosting_info": [
                 {
                    "hosting_status": "hosted",
                    "hosted_on": "college-cloud",
                    "hosted_url": "http://cse14-iiith.ac.in"
                 }
              ],
              "integration_level": 4,
              "assets": [
                 {
                    "asset_type": "image",
                    "path": "vlabs.ac.in/images/static/logo.png"
                 },
                 {
                    "asset_type": "video",
                    "path": "vlabs.ac.in/video/abc.mkv"
                 }
              ],
              "sections": [
                 "Introduction",
                 "Objective",
                 "Tutorial",
                 "Illustration",
                 "Procedure",
                 "Experiment",
                 "Observations",
                 "Assignment",
                 "References"
              ]
           }
        }
        experiment1 = SystemInterface.add_experiment(data_dict1)

        data_dict1 = {
           "key" : KEY,
           "lab": {
	       "id": "cse03",
	       "name": "Computer Programming",
               "overview": "overviewasds",
	       "discipline_id": "CSE",
	       "institute_id": "IITK",
	       "developers": [
		   {
		       "name": "Dinesh Malviya",
		       "email": "xyz@gmail.com"
		   },
		   {
		       "name": "Ashish Ahuja",
		       "email": "abc@gmail.com"
		   }
	       ],
	       "hosting_info": [
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "cloud",
		       "hosted_url": "http://cse14-iiith.vlabs.ac.in"
		   },
		   {
		       "hosting_status": "hosted",
		       "hosted_on": "college-cloud",
		       "hosted_url": "http://cse14-iiith.ac.in"
		   }
	       ],
	       "integration_level": 4,
	       "assets": [
		   {
		       "asset_type": "image",
		       "path": "vlabs.ac.in/images/static/logo.png"
		   }
	       ],
	       "sections": [
		   {
		       "name": "Introduction"
		   }
	       ],
                      "experiments": [
                         "exp1234", "exp123"
                      ]
	   }
        }

        lab1 = SystemInterface.update_lab(data_dict1)

        self.assertEqual(lab1.get("lab_name"), data_dict1['lab']['name'])
        self.assertEqual(lab1.get("lab_id"), data_dict1['lab']['id'])
        self.assertEqual(lab1.get("overview"), data_dict1['lab']['overview'])
        self.assertEqual(lab1.get("institute").get("institute_id"),
                             data_dict1['lab']['institute_id'])
        self.assertEqual(lab1.get("discipline").get("discipline_id"),
                             data_dict1['lab']['discipline_id'])
        self.assertEqual(lab1.get("integration_status").\
                             get("integration_level"),
                             data_dict1['lab']['integration_level'])
        self.assertEqual(lab1.get("hosting_info")[0].get("hosted_url"),
                             data_dict1['lab']['hosting_info'][0]['hosted_url'])
        self.assertEqual(lab1.get("hosting_info")[1].get("hosted_url"),
                             data_dict1['lab']['hosting_info'][1]['hosted_url'])
        self.assertEqual(lab1.get("developers")[0].get("email").get("email"),
                             data_dict1['lab']['developers'][0]['email'])
        self.assertEqual(lab1.get("developers")[1].get("email").get("email"),
                             data_dict1['lab']['developers'][1]['email'])
        self.assertEqual(lab1.get("assets")[0].get("path"),
                             data_dict1['lab']['assets'][0]['path'])
        self.assertEqual(lab.get("sections")[0].get("name"),
			    'Introduction')
        self.assertEqual(lab1.get("developers")[0].get("email").get("email"),
                            data_dict1['lab']['developers'][0].get("email"))
        self.assertEqual(lab1.get("assets")[0].get("path"),
                             data_dict1['lab']["assets"][0].get("path"))
        self.assertEqual(lab1.get("experiments")[1].get("exp_id"),
                              experiment1.get("exp_id"))
        self.assertEqual(lab1.get("experiments")[0].get("exp_id"),
                              experiment.get("exp_id"))
    
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

    def test_update_experiment_name_in_system_interface(self):
        print "test_update_experiment_name_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)
     
        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Theory'
                    }
        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        exp = SystemInterface.add_experiment(data_dict)

        data_dict1 = {
                    'key' : KEY,
                    'integration_level': 3
                    }

        integration_status = SystemInterface.add_integration_status(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'asset_type': 'Video1',
                    'path': 'vlabs.ac.in/images/video/icon.png'
                   }

        asset = SystemInterface.add_asset(data_dict1)


        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'discipline_name': 'electronics & engineering',
                    'discipline_id': 'ECE',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                   }

        discipline = SystemInterface.add_discipline(data_dict1)
        
        data_dict1 = {
                    'key' : KEY,
                    'name': 'Aim'
                    }
        section = SystemInterface.add_section(data_dict1)


        data_dict1 = {"key" : KEY,
                      "experiment": {
                         "overview": "overview",
                         "name": "queue",
                         "id": "exp123",
                         "discipline_id": "CSE",
                         "institute_id": "IITK",
                         'integration_level': 3,
                         "sections": [
                            "Theory",
                            "Objective",
                            "Tutorial",
                            "Illustration",
                            "Procedure",
                            "Experiment",
                            "Observations",
                            "Assignment",
                            "References"
                         ],
                         "assets": [
                            {
                               "asset_type": "image",
                               "path": "vlabs.ac.in/images/static/logo.png"
                            }
                         ],
                         "developers": [
                            {
                               "name": "Prof. Dharamaja",
                               "email": "abc@gmail.com"
                            },
                            {
                               "name": "Prof. Pallavi Pawar",
                               "email": "pallavi.pawar@gmail.com"
                            }
                         ],
                         "hosting_info": [
                            {
                               "hosting_status": "hosted",
                               "hosted_on": "cloud",
                               "hosted_url": "http://cse14-iiith.ac.in"
                            },
                            {
                               "hosting_status": "hosted",
                               "hosted_on": "server",
                               "hosted_url": "http://iitkgp.vlab.co.in/"
                            }
                         ]
                      }
                   }
        
        exp1 = SystemInterface.update_experiment(data_dict1)
        self.assertEqual(exp1.get("exp_name"), data_dict1['experiment']['name'])
        self.assertEqual(exp1.get("overview"), data_dict1['experiment']['overview'])
        self.assertEqual(exp1.get("exp_id"), data_dict1['experiment']['id'])
        self.assertEqual(exp1.get("institute").get("institute_id"),
                             data_dict1['experiment']['institute_id'])
        self.assertEqual(exp1.get("discipline").get("discipline_id"),
                             data_dict1['experiment']['discipline_id'])
        self.assertEqual(exp1.get("integration_status").\
                             get("integration_level"),
                             data_dict1['experiment']['integration_level'])
        self.assertEqual(exp1.get("hosting_info")[0].get("hosted_url"), 
                             data_dict1['experiment']['hosting_info'][0]['hosted_url'])
        self.assertEqual(exp1.get("hosting_info")[1].get("hosted_url"), 
                             data_dict1['experiment']['hosting_info'][1]['hosted_url'])
        self.assertEqual(exp1.get("developers")[0].get("email").get("email"), 
                             data_dict1['experiment']['developers'][0]['email'])
        self.assertEqual(exp1.get("developers")[1].get("email").get("email"), 
                             data_dict1['experiment']['developers'][1]['email'])
        self.assertEqual(exp1.get("assets")[0].get("path"), 
                             data_dict1['experiment']['assets'][0]['path'])
        self.assertEqual(exp1.get("sections")[0].get("name"), 
                             data_dict1['experiment']['sections'][1])


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

    def test_update_institute_name_in_system_interface(self):
        print "test_update_institute_name_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    'overview' : 'overview',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Delhi',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]
                   }


        institute1 = SystemInterface.update_institute(data_dict1)
        
        self.assertEqual(institute1.get("institute_name"), data_dict1['institute_name'])
        self.assertEqual(institute1.get("assets")[0].get("path"), 
                             data_dict1['assets'][0]['path'])
class TestUpdateSection(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_section_name_in_system_interface(self):
        print "test_update_section_name_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name': 'Theory'
                   }

        data_dict1 = {
                    'key' : KEY,
                    's_id': 1,
                    'name': 'Quiz'
                   }

        section = SystemInterface.add_section(data_dict)
        section1 = SystemInterface.update_section(data_dict1)
        
        self.assertEqual(section1.get("name"), data_dict1['name'])

class TestUpdateDiscipline(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_discipline_name_in_system_interface(self):
        print "test_update_discipline_name_in_system_interface"
 
        data_dict = {'discipline_name': 'Computer Science',
                    'discipline_id': 'CSE',
                    'key' : KEY,
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        data_dict1 = {'discipline_name': 'Computer Science and Engineering',
                      'discipline_id': 'CSE',
		      "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ],
                      'key' : KEY
                     }

        dis1 = SystemInterface.add_discipline(data_dict)
        dis = SystemInterface.update_discipline(data_dict1)
        
        self.assertEqual(dis.get("discipline_name"), data_dict1['discipline_name'])
        self.assertEqual(dis.get("assets")[0].get("path"), 
                             data_dict1['assets'][0]['path'])

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

    def test_update_hosting_info_in_system_interface(self):
        print "test_update_hosting_info_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                    }

        data_dict1 = {
                    'key' : KEY,
                    'hosting_status': 'not hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'server'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)
        hosting_info1 = SystemInterface.update_hosting_info(data_dict1)
        
        self.assertEqual(hosting_info1.get("hosting_status"), data_dict1['hosting_status'])
        self.assertEqual(hosting_info1.get("hosted_on"), data_dict1['hosted_on'])


class TestGetLabByLabId(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_lab_by_labid_in_system_interface(self):
        print "test_get_lab_by_labid_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                    }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
 		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
 		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,                    
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)


        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {
               "key" : KEY,
               "lab": {
                   "id": "cse03",
                   "name": "Computer Programming",
                   "overview": "overview",
                   "discipline_id": "CSE",
                   "institute_id": "IITK",
                   "developers": [
                       {
                           "name": "Dinesh Malviya",
                           "email": "xyz@gmail.com"
                       },
                       {
                           "name": "Ashish Ahuja",
                           "email": "abc@gmail.com"
                       }
                   ],
                   "hosting_info": [
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "cloud",
                           "hosted_url": "http://cse1-iiith.vlabs.ac.in"
                       },
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "college-cloud",
                           "hosted_url": "http://cse4-iiith.ac.in"
                       }
                   ],
                   "integration_level": 4,
                   "assets": [
                       {
                           "asset_type": "image",
                           "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                           "asset_type": "video",
                           "path": "vlabs.ac.in/video/abc.mkv"
                       }
                   ],
                   "sections": [
                       {
                           "name": "Introduction"
                       }
                                              
                   ],
                       "experiments": [
                               "exp123"
                           ]

               }
           }

        data_dict1 = {
               "key" : KEY,
               "lab": {
                   "id": "cse02",
                   "name": "Computer Programming",
                   "overview": "overview",
                   "discipline_id": "CSE",
                   "institute_id": "IITK",
                   "developers": [
                       {
                           "name": "Dinesh Malviya",
                           "email": "xyz@gmail.com"
                       },
                       {
                           "name": "Ashish Ahuja",
                           "email": "abc@gmail.com"
                       }
                   ],
                   "hosting_info": [
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "cloud",
                           "hosted_url": "http://ce14-iiith.vlabs.ac.in"
                       },
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "college-cloud",
                           "hosted_url": "http://ce14-iiith.ac.in"
                       }
                   ],
                   "integration_level": 4,
                   "assets": [
                       {
                           "asset_type": "image",
                           "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                           "asset_type": "video",
                           "path": "vlabs.ac.in/video/abc.mkv"
                       }
                   ],
                   "sections": [
                       {
                           "name": "Introduction"
                       }
                                              
                   ],
                   "experiments": [
                   "exp123"
                   ]

               }
           }
        lab = SystemInterface.add_lab(data_dict)
        lab1 = SystemInterface.add_lab(data_dict1)

        lab = SystemInterface.get_lab(data_dict['lab']['id'])
        lab1 = SystemInterface.get_lab(data_dict1['lab']['id'])
        
        self.assertEqual(lab.get("lab_id"), data_dict['lab']['id'])
        self.assertEqual(lab1.get("lab_id"), data_dict1['lab']['id'])

class TestGetLabsByInstitute(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_institute_in_system_interface(self):
        print "test_get_labs_by_institute_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Logo',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)


        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "icon",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)


        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        experiment = SystemInterface.add_experiment(data_dict)


        data_dict = {
               "key" : KEY,     
           "lab": {
               "id": "cse02",
               "name": "Computer Programming",
                   "overview": "overview",
               "discipline_id": "CSE",
               "institute_id": "IITK",
               "developers": [
               {
                   "name": "Dinesh Malviya",
                   "email": "xyz@gmail.com"
               },
               {
                   "name": "Ashish Ahuja",
                   "email": "abc@gmail.com"
               }
               ],
               "hosting_info": [
               {
                   "hosting_status": "hosted",
                   "hosted_on": "cloud",
                   "hosted_url": "http://cse14-iiith.vlabs.ac.in"
               },
               {
                   "hosting_status": "hosted",
                   "hosted_on": "college-cloud",
                   "hosted_url": "http://cse14-iiith.ac.in"
               }
               ],
               "integration_level": 4,
               "assets": [
               {
                   "asset_type": "logo",
                   "path": "vlabs.ac.in/images/static/logo.png"
               },
               {
                   "asset_type": "video",
                   "path": "vlabs.ac.in/video/abc.mkv"
               }
               ],
               "sections": [
               {
                   "name": "Introduction"
               }
                              
               ],
                   "experiments": [
                   "exp123"
                   ]

           }
           }

        data_dict1 = {
               "key" : KEY,     
               "lab": {
                   "id": "cse03",
                   "name": "Computer Programming",
                   "overview": "overview",
                   "discipline_id": "CSE",
                   "institute_id": "IITK",
                   "developers": [
                       {
                           "name": "Dinesh Malviya",
                           "email": "xyz@gmail.com"
                       },
                       {
                           "name": "Ashish Ahuja",
                           "email": "abc@gmail.com"
                       }
                   ],
                   "hosting_info": [
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "cloud",
                           "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                           "hosting_status": "hosted",
                           "hosted_on": "college-cloud",
                           "hosted_url": "http://cse14-iiith.ac.in"
                       }
                   ],
                   "integration_level": 4,
                   "assets": [
                       {
                           "asset_type": "image",
                           "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                           "asset_type": "video",
                           "path": "vlabs.ac.in/video/abc.mkv"
                       }
                   ],
                   "sections": [
                       {
                           "name": "Introduction"
                       }
                       
                   ],
                   "experiments": [
                   "exp123"
                   ]

               }
           }

        lab = SystemInterface.add_lab(data_dict)
        lab1 = SystemInterface.add_lab(data_dict1)

        labs = SystemInterface.get_labs_by_institute("IIT Kanpur")

        self.assertEqual(labs[0]['institute']['institute_name'], "IIT Kanpur")

class TestGetLabsByLabName(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_lab_name_in_system_interface(self):
        print "test_get_labs_by_lab_name_in_system_interface"

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "Icon",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)
        
        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }
        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse02",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                         "asset_type": "video",
                         "path": "vlabs.ac.in/video/abc.mkv"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }
                     ],
                     "experiments": [
                     "exp123"
                     ]

                   }
                 }

        data_dict1 = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse03",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                         "asset_type": "video",
                         "path": "vlabs.ac.in/video/abc.mkv"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }
                       ],
                       "experiments": [
                         "exp123"
                         ]
                   }
                 }
        lab = SystemInterface.add_lab(data_dict)
        lab1 = SystemInterface.add_lab(data_dict1)

        labs = SystemInterface.get_labs_by_lab_name(data_dict['lab']['name'])

        self.assertEqual(labs[0]['lab_name'], data_dict['lab']['name'])

class TestGetLabsByDiscipline(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_discipline_in_system_interface(self):
        print "test_get_labs_by_discipline_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)


        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "icon",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'Computer Science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }
        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse02",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                         "asset_type": "video",
                         "path": "vlabs.ac.in/video/abc.mkv"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }
                       
                     ],
                     "experiments": [
                     "exp123"
                     ]

                   }
                 }

        data_dict1 = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse03",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       },
                       {
                         "asset_type": "video",
                         "path": "vlabs.ac.in/video/abc.mkv"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }                       
                     ],
                         "experiments": [
                           "exp123"
                         ]
                   }
                 }

        lab = SystemInterface.add_lab(data_dict)
        lab1 = SystemInterface.add_lab(data_dict1)

        labs = SystemInterface.get_labs_by_discipline("Computer Science")

        self.assertEqual(labs[0]['discipline']['discipline_name'], "Computer Science")

class TestGetLabsByKeywordLabName(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_labs_by_keyword_lab_in_system_interface(self):
        print "test_get_labs_by_keyword_lab_name_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud'
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    "assets": [
                    {
                    "asset_type": "video",
                    "path": "vlabs.ac.in/images/static/icon.png"
                }
                ]

            }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
		   'key' : KEY,
		   'name': 'Procedure'
		  }

        section = SystemInterface.add_section(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
              "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        experiment = SystemInterface.add_experiment(data_dict)

        data_dict = {'lab_name': 'data structure',
                    'lab_id': 'cse02',
                    'overview': 'overview',
                    'key': KEY,
                    'institute_id': 'IITK',
                    'discipline_id': 'CSE',
                    'assets': [{'path':'vlabs.ac.in/images/static/logo.png',
                                    'asset_type': 'image'},
                                {'path':'vlabs.ac.in/images/static/image.png',
                                    'asset_type': 'image'}],
                    'developers': [{'name':'Prof. Dharamaja',
                                    'email': 'abc@gmail.com',
                                    'institute_id': 'IITK', 'discipline_id': 'CSE'},
                                    {'name':'Prof. Pallavi Pawar',
                                    'email': 'pallavi.pawar@gmail.com',
                                    'institute_id': 'IITK', 'discipline_id': 'CSE'}],
                    'hosting_info': [{'hosted_url':'http://cse14-iiith.vlabs.ac.in',
                                    'hosting_status': 'hosted',
                                    'hosted_on': 'cloud'},
                                    {'hosted_url':'http://iitkgp.vlab.co.in/',
                                    'hosting_status': 'hosted',
                                    'hosted_on': 'server'}],
                    'integration_level': 4,
                    'experiments': ['exp123']
                   }

        data_dict = {
		   "key" : KEY,
                   "lab": {
                     "id": "cse02",
                     "name": "data bases",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }
                                              
                     ],
                         "experiments": [
                           "exp123"
                         ]

                   }
                 }

        data_dict1 = {
		   "key" : KEY,
                   "lab": {
                     "id": "cse03",
                     "name": "data structures",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Dinesh Malviya",
                         "email": "xyz@gmail.com"
                       },
                       {
                         "name": "Ashish Ahuja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       },
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "college-cloud",
                         "hosted_url": "http://cse14-iiith.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Introduction"
                       }
                                              
                     ],
                         "experiments": [
                           "exp123"
                         ]

                   }
                 }

        lab1 = SystemInterface.add_lab(data_dict)
        lab2 = SystemInterface.add_lab(data_dict1)

        labs_list = SystemInterface.get_labs_by_keyword_lab_name("data")

        self.assertEqual(labs_list[0].get("lab_name"), data_dict['lab']['name'])
        self.assertEqual(labs_list[1].get("lab_name"), data_dict1['lab']['name'])
        self.assertEqual(labs_list[0].get("lab_id"),
                             data_dict['lab']['id'])
        self.assertEqual(labs_list[1].get("lab_id"),
                             data_dict1['lab']['id'])


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

    def test_update_developer_name_in_system_interface(self):
        print "test_update_developer_name_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict1 = {
                    'key': KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
		    "assets": [
			{
			  "asset_type": "logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute1 = SystemInterface.add_institute(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'discipline_name': 'electronics engineering',
                    'discipline_id': 'ece',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]

                    }


        discipline1 = SystemInterface.add_discipline(data_dict1)


        data_dict1 = {
                    'key': KEY,
                    'email': 'abc@gmail.com',
                    'name': 'Prof. Raja'
                   }

        developer1 = SystemInterface.update_developer(data_dict1)

        self.assertEqual(developer1.get("name").get("name"),
                             data_dict1['name'])

class TestGetNames(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_name_in_system_interface(self):
        print "test_get_name_in_system_interface"

        data_dict = {'name': 'Prof. Dharamaraj',
                    'key': KEY
                   }

        data_dict1 = {'name': 'Prof. Yamaraja',
                     'key': KEY
                     }

        name1 = SystemInterface.add_name(data_dict)
        name2 = SystemInterface.add_name(data_dict1)

        name_list = SystemInterface.get_names()
        
        self.assertEqual(name_list[0].get("name"), data_dict['name'])
        self.assertEqual(name_list[1].get("name"), data_dict1['name'])

class TestGetEmails(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_email_in_system_interface(self):
        print "test_get_email_in_system_interface"

        data_dict = {'email': 'abc@gmail.com',
                    'key': KEY
                   }

        data_dict1 = {'email': 'xyz@gmail.com',
                     'key': KEY
                     }

        email1 = SystemInterface.add_email(data_dict)
        email2 = SystemInterface.add_email(data_dict1)

        email_list = SystemInterface.get_emails()
        
        self.assertEqual(email_list[0].get("email"), data_dict['email'])
        self.assertEqual(email_list[1].get("email"), data_dict1['email'])

class TestGetDevelopers(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_developer_in_system_interface(self):
        print "test_get_developer_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com',
                    'institute_id': 'IITK',
                    'discipline_id': 'CSE'
                   }

        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute1 = SystemInterface.add_institute(data_dict1)

        data_dict1 = {
                    'key' : KEY,
                    'discipline_name': 'electronics and communication',
                    'discipline_id': 'ECE',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline1 = SystemInterface.add_discipline(data_dict1)

        data_dict1 = {'name': 'Prof. Yamraja',
                      'email': 'xyz@gmail.com',
                      'key': KEY
                     }

        developer1 = SystemInterface.add_developer(data_dict)
        developer2 = SystemInterface.add_developer(data_dict1)

        developer_list = SystemInterface.get_developers()
        
        self.assertEqual(developer_list[0].get("name").get("name"),
                             data_dict['name'])
        self.assertEqual(developer_list[1].get("name").get("name"),
                             data_dict1['name'])

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

    def test_delete_name_in_system_interface(self):
        print "test_delete_name_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'name': 'Prof. Dharamaraja'
                   }

        data_dict1 = {
                    'key': KEY,
                    'name' : 'Prof. Raja'
                   }

        name = SystemInterface.add_name(data_dict)
        name1 = SystemInterface.add_name(data_dict1)
        name_id = SystemInterface.delete_name(1)

        self.assertEqual(name_id, 1)

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

    def test_delete_email_in_system_interface(self):
        print "test_delete_email_in_system_interface"

        data_dict = {
                    'key': KEY,
                    'email': 'abc@gmail.com'
                   }

        data_dict1 = {
                    'key': KEY,
                    'email' : 'xyz@gmail.com'
                   }

        email = SystemInterface.add_email(data_dict)
        email1 = SystemInterface.add_email(data_dict1)
        email_id = SystemInterface.delete_email(data_dict1['email'],
                                                data_dict1['key'])

        self.assertEqual(email_id.get("email"), data_dict1["email"])

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

    def test_delete_developer_in_system_interface(self):
        print "test_delete_developer_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]
                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/icon.png"
			}
		      ]
                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com',
                    'institute_id': 'IITK',
                    'discipline_id': 'CSE'
                   }

        data_dict1 = {
                    'key': KEY,
                    'name' : 'Prof. Raja',
                    'email': 'xyz@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)
        developer1 = SystemInterface.add_developer(data_dict1)
        dev = SystemInterface.delete_developer(data_dict['email'],
                                                      data_dict['key'])
        
        self.assertEqual(dev.get("email"), data_dict['email'])

class TestGetExpByExpId(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_exp_by_expid_in_system_interface(self):
        print "test_get_exp_by_expid_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)


        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
 		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
 		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        integration_status = SystemInterface.add_integration_status(data_dict)

        data_dict = {
                    'hosting_status': 'hosted',
                    'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                    'hosted_on': 'cloud',
                    'key' : KEY
                   }

        hosting_info = SystemInterface.add_hosting_info(data_dict)

        data_dict = {
                    "key" : KEY,
		    "experiment": {
		      "id": "exp123",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }


        data_dict1 = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99848",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Dinesh Malviya",
			  "email": "xyz@gmail.com"
			},
			{
			  "name": "Ashish Ahuja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "college-cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			},
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/video/abc.mkv"
			}
		      ],
		      "sections": [
			"Introduction",
			"Objective",
			"Tutorial",
			"Illustration",
			"Procedure",
			"Experiment",
			"Observations",
			"Assignment",
			"References"
		      ]
		    }
		  }

        exp = SystemInterface.add_experiment(data_dict)
        exp1 = SystemInterface.add_experiment(data_dict1)

        exp = SystemInterface.get_experiment(data_dict['experiment']['id'])
        exp1 = SystemInterface.get_experiment(data_dict1['experiment']['id'])
        
        self.assertEqual(exp.get("exp_id"), data_dict['experiment']['id'])
        self.assertEqual(exp1.get("exp_id"), data_dict1['experiment']['id'])

class TestGetInstituteByInstituteId(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_institute_by_instituteid_in_system_interface(self):
        print "test_get_institute_by_instituteid_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Delhi',
                    'institute_id': 'IITD',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]
                    }

        data_dict1 = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ]
                    }

        institute = SystemInterface.add_institute(data_dict)
        institute1 = SystemInterface.add_institute(data_dict1)

        institute = SystemInterface.get_institute(data_dict['institute_id'])
        institute1 = SystemInterface.get_institute(data_dict1['institute_id'])
        
        self.assertEqual(institute.get("institute_id"), data_dict['institute_id'])
        self.assertEqual(institute1.get("institute_id"), data_dict1['institute_id'])

class TestGetDisciplineByDisciplineId(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_discipline_by_disid_in_system_interface(self):
        print "test_get_discipline_by_disid_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)


        data_dict = {'discipline_name': 'Computer Science',
                    'discipline_id': 'CSE',
                    'key' : KEY,
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        data_dict1 = {'discipline_name': 'Electronics',
                    'discipline_id': 'ECE',
                    'key' : KEY,
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        dis = SystemInterface.add_discipline(data_dict)
        dis1 = SystemInterface.add_discipline(data_dict1)

        dis = SystemInterface.get_discipline(data_dict['discipline_id'])
        dis1 = SystemInterface.get_discipline(data_dict1['discipline_id'])
        
        self.assertEqual(dis.get("discipline_id"), data_dict['discipline_id'])
        self.assertEqual(dis1.get("discipline_id"), data_dict1['discipline_id'])

class TestGetDeveloperByEmail(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_developer_by_email_in_system_interface(self):
        print "test_get_developer_by_email_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict = {
                    'key' : KEY,
                    'institute_name': 'IIT Kanpur',
                    'institute_id': 'IITK',
                    		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                    }

        institute = SystemInterface.add_institute(data_dict)

        data_dict = {
                    'key' : KEY,
                    'discipline_name': 'computer science',
                    'discipline_id': 'CSE',
                    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ]

                   }

        discipline = SystemInterface.add_discipline(data_dict)

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamaja',
                    'email': 'abc@gmail.com'
                   }

        developer = SystemInterface.add_developer(data_dict)

        developer = SystemInterface.get_developer(data_dict['email'])
        
        self.assertEqual(developer.get("email").get("email"), 
                             data_dict['email'])
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

    def test_get_integration_status_by_IL_in_system_interface(self):
        print "test_get_integration_status_by_IL_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'integration_level': 4
                    }

        data_dict1 = {
                    'key' : KEY,
                    'integration_level': 2
                     }

        integration_status = SystemInterface.add_integration_status(data_dict)
        integration_status1 = SystemInterface.add_integration_status(data_dict1)
        integration_status = SystemInterface.get_integration_status_by_IL(2)
        
        self.assertEqual(integration_status.get("integration_level"), 2)

class TestAddAsset(TestCase):
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_asset_in_system_interface(self):
        print "test_add_asset_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        asset_cls = System.delegate.entities['asset']
        asset = asset_cls.get_all()[0]

        self.assertEqual(asset.get("asset_type").get("asset_type"), 
                             data_dict['asset_type'])
        self.assertEqual(asset.get("path"), data_dict['path'])
        
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

    def test_update_asset_type_in_system_interface(self):
        print "test_update_asset_type_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/static/images/logo.png'
                    }

        data_dict1 = {
                    'key' : KEY,
                    'asset_type': 'Video', 
                    'path': 'vlabs.ac.in/static/images/logo.png'
                    }

        asset = SystemInterface.add_asset(data_dict)
        asset1 = SystemInterface.update_asset(data_dict1)
        
        self.assertEqual(asset1.get("asset_type")["asset_type"], data_dict1['asset_type'])

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

    def test_delete_asset_in_system_interface(self):
        print "test_delete_asset_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/static/images/logo.png'
                    }

        data_dict1 = {
                    'key' : KEY,
                    'asset_type': 'Video',
                    'path': 'vlabs.ac.in/static/images/icon.png'
                    }

        asset = SystemInterface.add_asset(data_dict)
        asset1 = SystemInterface.add_asset(data_dict1)
        path = SystemInterface.delete_asset("vlabs.ac.in/static/images/icon.png", KEY)
        
        self.assertEqual(path, "vlabs.ac.in/static/images/icon.png")

class TestGetAssets(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_assets_in_system_interface(self):
        print "test_get_assets_in_system_interface"
        
        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict1 = {
                     'key' : KEY,
                     'asset_type': 'Video',
                     'path': 'vlabs.ac.in/images/static/icon.png'
                     }

        asset1 = SystemInterface.add_asset(data_dict1)
        
        asset_dict_list = SystemInterface.get_assets()
        
        self.assertEqual(asset_dict_list[0].get("asset_type")["asset_type"],
                             data_dict['asset_type'])
        self.assertEqual(asset_dict_list[1].get("asset_type")["asset_type"],
                             data_dict1['asset_type'])
        self.assertEqual(asset_dict_list[0].get("path"), 
                             data_dict['path'])
        self.assertEqual(asset_dict_list[1].get("path"), 
                             data_dict1['path'])

class TestGetAssetByPath(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_asset_by_path_in_system_interface(self):
        print "test_get_asset_by_path_in_system_interface"
        
        data_dict = {
                    'key' : KEY,
                    'asset_type': 'Image',
                    'path': 'vlabs.ac.in/images/static/logo.png'
                   }

        asset = SystemInterface.add_asset(data_dict)

        data_dict1 = {
                     'key' : KEY,
                     'asset_type': 'Video',
                     'path': 'vlabs.ac.in/images/static/icon.png'
                     }

        asset1 = SystemInterface.add_asset(data_dict1)

        asset_data_one = SystemInterface.get_asset_by_path(data_dict['path'])

        self.assertEqual(asset_data_one.get("path"), data_dict['path'])
class TestGetHosting_Info_by_hosted_url(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_hosting_info_by_hosted_url_in_system_interface(self):
        print "test_get_hosting_info_by_hosted_url_in_system_interface"

        data_dict = {'hosting_status': 'hosted',
                     'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                     'hosted_on': 'cloud',
                     'key' : KEY
                    }

        data_dict1 = {'hosting_status': 'not hosted',
                      'hosted_url': 'http://cse12-iiith.vlabs.ac.in',
                      'hosted_on': 'server',
                      'key' : KEY
                     }

        host1 = SystemInterface.add_hosting_info(data_dict)
        host2 = SystemInterface.add_hosting_info(data_dict1)

        host_list = SystemInterface.get_hosting_info_by_hosted_url('http://cse12-iiith.vlabs.ac.in')
        
        self.assertEqual(host_list.get("hosted_url"), data_dict1['hosted_url'])

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

    def test_update_name_in_system_interface(self):
        print "test_update_name_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name': 'Prof. Dharamraj'
                   }

        data_dict1 = {
                    'key' : KEY,
                    'n_id': 1,
                    'name': 'Prof. Dharam'
                   }

        name = SystemInterface.add_name(data_dict)
        name1 = SystemInterface.update_name(data_dict1)
        
        self.assertEqual(name1.get("name"), data_dict1['name'])

class TestGetNameById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_name_by_id_in_system_interface(self):
        print "test_get_name_by_id_in_system_interface"

        data_dict = {
                    'key' : KEY,
                    'name' : "Prof. Dharamraj"
                   }

        data_dict1 = {
                    'key' : KEY,
                    'name' : "Prof. Dharamrajuuuu"
                   }

        name1 = SystemInterface.add_name(data_dict)
        name2 = SystemInterface.add_name(data_dict1)

        name_data_one = SystemInterface.get_name_by_id(1)
        name_data_two = SystemInterface.get_name_by_id(2)
        
        self.assertEqual(name_data_one.get("name"), data_dict['name'])
        self.assertEqual(name_data_two.get("name"), data_dict1['name'])

if __name__ == '__main__':
    unittest.main()
