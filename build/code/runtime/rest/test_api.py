
# -*- coding: utf-8 -*-
import unittest
from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError
from runtime.utils.class_persistence_template import db
from runtime.rest.app import create_app
from runtime.config.system_config import KEY
from runtime.rest.api import *
from runtime.system.system import System
import datetime
config = {
         'SQLALCHEMY_DATABASE_URI': ''
         }

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
        print "test_add_lab_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
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
                     "overview": "This experiments describes about parallel and distributed processing",
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)


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

    def test_update_lab(self):
        print "test_update_lab"
        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Introduction',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Prof. Dharamaja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "overview": "This experiments describes about parallel and distributed processing",
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/static/logo.png"
                       }
                     ],
                     "sections": [
                       "Introduction"
                     ]
                   }
                 }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse02",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Prof. Dharamaja",
                         "email": "abc@gmail.com"

                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)


        payload1 = {'asset_type': 'Video',
                   'path': 'vlabs.ac.in/images/video/icon.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                    'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'discipline_name': 'Electronics & Comuunication Engg.',
                    'discipline_id': 'ECE',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                    'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'name': 'Prof. Pallavi Pawar',
                   'email': 'pallavi.pawar@gmail.com',
                   'key': KEY}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'name': 'Theory',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload1),
                                 headers=headers)
                          
        payload1 = {'integration_level': 3,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'hosting_status': 'hosted',
                   'hosted_url': 'http://iitk.vlab.co.in/',
                   'hosted_on': 'server',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {           
		   "key" : KEY,     
                   "lab": {
                     "name": "Computer Programming",
                     "overview": "cp overview",
                     "discipline_id": "ECE",
                     "institute_id": "IITKgp",
                     "developers": [                    
                       {
                         "name": "Prof. Pallavi Pawar",
                         "email": "pallavi.pawar@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {                       
                         "hosting_status": "hosted",
                         "hosted_on": "server",
                         "hosted_url": "http://iitk.vlab.co.in/"
                       }
                     ],
                     "integration_level": 3,
                     "assets": [
                       {
                         "asset_type": "image",
                         "path": "vlabs.ac.in/images/video/icon.png"
                       }
                     ],
                     "sections": [
                       {
                         "name": "Theory"
                       }                                              
                     ],
                         "experiments": [
                           "exp123"
                         ]

                   }
                 }

        response = self.client.put("/labs?lab_id=cse02", 
                                       data=json.dumps(payload1),
                                       headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_delete_lab"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)
  
        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
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
                     "overview": "This experiments describes about parallel and distributed processing",
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

        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)        

        payload = {           
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
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/labs?lab_id=cse02&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_labs(self):
        print "test_get_labs_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)


        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
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
                     "overview": "This experiments describes about parallel and distributed processing",
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
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/labs", headers=headers)
        self.assertEqual(response.status_code, 200)

class TestGetLabbyLabId(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_lab_by_labid(self):
        print "test_get_lab_by_labid_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)


        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
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
                     "overview": "This experiments describes about parallel and distributed processing",
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
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)


        response = self.client.get("/labs?lab_id=cse02", headers=headers)
        self.assertEqual(response.status_code, 200)

class TestGetLabsbyInstitute(TestCase):
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
        print "test_get_labs_by_institute_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
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
                     "overview": "This experiments describes about parallel and distributed processing",
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

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
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


        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)


        response = self.client.get("/labs?institute_name=IIT Kanpur", headers=headers)
        self.assertEqual(response.status_code, 200)

class TestGetLabsbyLabName(TestCase):
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
        print "test_get_labs_by_lab_name_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)


        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Theory',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Prof. Dharamaja",
                         "email": "abc@gmail.com"
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
                     "overview": "This experiments describes about parallel and distributed processing",
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
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse02",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Prof. Dharamaja",
                         "email": "abc@gmail.com"
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


        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)


        response = self.client.get("/labs?lab_name=Computer Programming", headers=headers)
        self.assertEqual(response.status_code, 200)

class TestGetLabsbyDiscipline(TestCase):
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
        print "test_get_labs_by_discipline_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}


        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
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
                     "overview": "This experiments describes about parallel and distributed processing",
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        payload = {           
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

        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)


        response = self.client.get("/labs?discipline_name=Computer Science",
                                       headers=headers)
        self.assertEqual(response.status_code, 200)

class TestGetLabbyLabNameKeyWord(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_lab_by_labname_keyword(self):
        print "test_get_lab_by_labname_keyword_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}


        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {
		   "key": KEY,
                   "experiment": {
                     "id": "exp123",
                     "name": "arrays",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Prof. Dharamaja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
                       }
                     ],
                     "integration_level": 4,
                     "overview": "This experiments describes about parallel and distributed processing",
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)
       
        payload = {           
		   "key" : KEY,     
                   "lab": {
                     "id": "cse02",
                     "name": "Computer Programming",
                     "overview": "overview",
                     "discipline_id": "CSE",
                     "institute_id": "IITK",
                     "developers": [
                       {
                         "name": "Prof. Dharamaja",
                         "email": "abc@gmail.com"
                       }
                     ],
                     "hosting_info": [
                       {
                         "hosting_status": "hosted",
                         "hosted_on": "cloud",
                         "hosted_url": "http://cse14-iiith.vlabs.ac.in"
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/labs", data=json.dumps(payload),
                                 headers=headers)


        response = self.client.get("/labs?keyword_lab_name=data", headers=headers)
        self.assertEqual(response.status_code, 200)

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

    def test_get_experiment_by_expid(self):
        print "test_get_experiment_by_expid_in_rest"
        payload = {'integration_level': 4,
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                       headers=headers)


        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers) 

        payload = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99847",
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/experiments", headers=headers)
        self.assertEqual(response.status_code, 200)


class TestGetDisciplineByDisId(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_discipline_by_disid(self):
        print "test_get_discipline_by_disid_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'IIT Delhi',
                   'discipline_id': 'EEE10',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/disciplines?discipline_id=EEE10",
                                       headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_experiment_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                       headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}   

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers) 

        payload = {'integration_level': 4,
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99847",
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
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/experiments", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_discipline_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'IIT Delhi',
                   'discipline_id': 'EEE10',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_disciplines(self):
        print "test_get_discipline_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'IIT Delhi',
                   'discipline_id': 'EEE10',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/disciplines", headers=headers)
        self.assertEqual(response.status_code, 200)

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

    def test_update_discipline(self):
        print "test_update_discipline"
 
        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)
        
        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)
        
        payload1 = {'asset_type': 'Video',
                   'path': 'vlabs.ac.in/images/video/icon.png',
                   'key': KEY}
        
        response = self.client.post("/assets", data=json.dumps(payload1),
                                 headers=headers)
        """
        payload1 = {'discipline_name': 'Computer Science and Engineering',
                   'assests' : [],
                   'key': KEY}
        
        response = self.client.put("/disciplines?discipline_id=CSE", data=json.dumps(payload1),
                                 headers=headers)
        """
        self.assertEqual(response.status_code, 200)
        
class TestGetExperiment(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_experiments(self):
        print "test_get_experiments_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                     headers=headers)

        payload = {'integration_level': 4,
                    'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}  

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99847",
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
               
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/experiments", headers=headers)
        self.assertEqual(response.status_code, 200)

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

    def test_update_experiment(self):
        print "test_update_experiment"
        
        payload = {'integration_level': 4,
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                  headers=headers)

        payload = {'name': 'Procedure',
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99847",
                      "overview": "overview",
		      "name": "Parallel and distributed processing",
		      "discipline_id": "CSE",
		      "institute_id": "IITK",
		      "developers": [
			{
			  "name": "Prof. Dharamaja",
			  "email": "abc@gmail.com"
			}
		      ],
		      "hosting_info": [
			{
			  "hosting_status": "hosted",
			  "hosted_on": "cloud",
			  "hosted_url": "http://cse14-iiith.ac.in"
			}
		      ],
		      "integration_level": 4,
		      "assets": [
			{
			  "asset_type": "Logo",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],
		      "sections": [
			"Procedure"	
		      ]
		    }
                    }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)
        
        payload1 = {'integration_level': 3,
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'asset_type': 'Icon',
                   'path': 'vlabs.ac.in/images/static/icon.png',
                   'key': KEY}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload1),
                                  headers=headers)

        payload1 = {'name': 'Objective',
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'institute_name': 'IIT Kharagpur',
                   'institute_id': 'IITKgp',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'discipline_name': 'Electronic Communication',
                   'discipline_id': 'ECE',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'name': 'Prof. Pallavi Pawar',
                   'email': 'pallavi.pawar@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'hosting_status': 'hosted',
                   'hosted_url': 'http://iitkgp.vlab.co.in/',
                   'hosted_on': 'server',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload1),
                                 headers=headers)
            
        payload1 = {"key" : KEY,
		    "experiment": {
                      "overview": "overview",
		      "name": "queue",
		      "discipline_id": "ECE",
		      "institute_id": "IITKgp",
                      'integration_level': 3,
                      "sections": [
			"Objective"
		      ],
                      "assets": [			
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ],
                      "developers": [			
			{
			  "name": "Prof. Pallavi Pawar",
			  "email": "pallavi.pawar@gmail.com"
			}
		      ],
                      "hosting_info": [			
                        {
			  "hosting_status": "hosted",
			  "hosted_on": "server",
			  "hosted_url": "http://iitkgp.vlab.co.in/"
			}
		      ],
                   }
                }

        headers = {'Content-Type': 'application/json'}

        response = self.client.put("/experiments?exp_id=e99847", 
                                       data=json.dumps(payload1),
                                       headers=headers)
        self.assertEqual(response.status_code, 200)


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

    def test_update_section(self):
        print "test_update_section"
        payload = {'name': 'Theory',
                   'key': KEY}

        payload1 = {'name': 'Theory',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.put("/sections/1", data=json.dumps(payload1),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_delete_section"

        payload = {'name': 'Theory',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/sections/1", headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_delete_experiment(self):
        print "test_delete_experiment"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                  headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'integration_level': 4,
                    'key': KEY
                  }
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof. Dharamaja',
                   'email': 'abc@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload = {
                    "key" : KEY,
		    "experiment": {
		      "id": "e99847",
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

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/experiments", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/experiments", headers=headers)
        self.assertEqual(response.status_code, 200)

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

    def test_get_sections(self):
        print "test_get_sections_in_rest"

        payload = {'name': 'Theory',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/sections", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_section_in_rest"
        payload = {'name': 'Quiz',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_names(self):
        print "test_get_names_in_rest"

        payload = {'name': 'Prof. Dharamraj',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/names", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/names", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_name_in_rest"
        payload = {'name': 'Prof. Dharamraj',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/names", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

class TestUpdateNameById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_name_by_id(self):
        print "test_update_name_by_id"
        payload = {'name': 'Prof. Dharamraj',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/names", data=json.dumps(payload),
                                 headers=headers)

        payload1 = {'name': 'Prof. Dharamrajuuuu',
                   'key': KEY}

        response = self.client.put("/names/1", data=json.dumps(payload1),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

class TestDeleteNameById(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_name_by_id(self):
        print "test_delete_name_by_id"

        payload = {'name': 'Prof. Dharamraj',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/names", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/names/1", headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_emails(self):
        print "test_get_emails_in_rest"

        payload = {'email': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/emails", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/emails", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_email_in_rest"
        payload = {'email': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/emails", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)


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
        print "test_delete_email"

        payload = {'email': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/emails", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/emails?email=dharamraj@gmail.com&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_developers(self):
        print "test_get_developers_in_rest"

        payload = {'dev_name': 'Prof. Dharamraj',
                   'email_id': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/developers", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_developer_in_rest"

        payload = {'name': 'Prof. Dharamraj',
                   'email': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_update_developer"

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/image.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "video",
			  "path": "vlabs.ac.in/images/static/video.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload = {'name': 'Prof.Dharamraj',
                   'email': 'dharamraj@gmail.com',
                   'key': KEY}
        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        payload1 = {'institute_name': 'IIT Kharagpur',
                    'institute_id': 'IITKgp',
                    "assets": [
                        {
                "asset_type": "Icon",
                "path": "vlabs.ac.in/images/static/icon.png"
                }],

                    'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload1 = {'discipline_name': 'Electronics & Comuunication Engg.',
                    'discipline_id': 'ECE',
                    "assets": [
                        {
                "asset_type": "logo",
                "path": "vlabs.ac.in/images/static/logo.png"
                }],
                        'key': KEY
                        }


        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        payload1 = {'name': 'Prof.Raj', 'key': KEY}

        response = self.client.put("/developers?email=dharamraj@gmail.com",
                                       data=json.dumps(payload1),
                                    headers=headers)

        self.assertEqual(response.status_code, 200)
        
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
        print "test_delete_developer"

        payload = {'name': 'Prof. Dharamraj',
                   'email': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/developers?email=dharamraj@gmail.com&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_add_institute_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_institutes(self):
        print "test_get_institutes_in_rest"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIIT Hyderabad',
                   'institute_id': 'IIITH',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/institutes", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_update_institute"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kanpur',
                   'institute_id': 'IITK',
                   "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        payload1 = {'asset_type': 'Video',
                   'path': 'vlabs.ac.in/images/video/icon.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload1),
                                 headers=headers)

        payload1 = {'institute_name': 'IIT Kharagpur',
		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                    'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.put("/institutes?institute_id=IITK", data=json.dumps(payload1),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_delete_institute"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'institute_name': 'IIT Kharagpur',
                   'institute_id': 'IITKgp',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/institutes", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/institutes?institute_id=IITKgp&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_delete_discipline"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        payload = {'discipline_name': 'Computer Science',
                   'discipline_id': 'CSE',
                   		    "assets": [
			{
			  "asset_type": "image",
			  "path": "vlabs.ac.in/images/static/logo.png"
			}
		      ],

                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/disciplines", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/disciplines?discipline_id=CSE&key=defaultkey", 
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_get_hosting_info_in_rest"

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/hosting_info", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_hosting_info_in_rest"
        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_update_hosting_info"

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        payload1 = {'hosting_status': 'not hosted', 
                    'hosted_on': 'server', 
                    'key': KEY}
    

        response = self.client.put("/hosting_info?hosted_url=http://cse14-iiith.vlabs.ac.in", data=json.dumps(payload1),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_delete_hosting_info"

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/hosting_info?hosted_url=http://cse14-iiith.vlabs.ac.in&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_get_integration_status_in_rest"

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/integration_status", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_integration_status_in_rest"
        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_delete_integration_status"

        payload = {'integration_level': 4,
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/integration_status", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/integration_status?integration_level=4&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_assets(self):
        print "test_get_assets_in_rest"

        payload = {'asset_type': 'Images',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/assets", headers=headers)
        self.assertEqual(response.status_code, 200)

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
        print "test_add_asset_in_rest"
        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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
        print "test_update_asset"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        payload1 = {'asset_type': 'Video',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.put("/assets?path=vlabs.ac.in/images/static/logo.png", data=json.dumps(payload1),
                                 headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_delete_asset(self):
        print "test_delete_asset"

        payload = {'asset_type': 'Image',
                   'path': 'vlabs.ac.in/images/static/logo.png',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/assets", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/assets?path=vlabs.ac.in/images/static/logo.png&key=defaultkey",
                                          headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_developers(self):
        print "test_get_developers_in_rest"

        payload = {'dev_name': 'Prof. Dharamraj',
                   'email_id': 'dharamraj@gmail.com',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/developers", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/developers", headers=headers)
        self.assertEqual(response.status_code, 200)

class TestGetSectionbyid(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_section_by_id(self):
        print "test_get_section_by_id"

        payload = {'name': 'Theory',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/sections", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/sections/1", headers=headers)

        self.assertEqual(response.status_code, 200)

class TestGetNamebyid(TestCase):
    TESTING = True
    def create_app(self):
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_name_by_id(self):
        print "test_get_name_by_id"

        payload = {'name': 'Prof. Dharamraj',
                   'key': KEY
                  }

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/names", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.delete("/names/1", headers=headers)

        self.assertEqual(response.status_code, 200)

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

    def test_get_asset_by_path(self):
        print "test_get_hosting_info_by_hosted_url_in_rest"

        payload = {'hosting_status': 'hosted',
                   'hosted_url': 'http://cse14-iiith.vlabs.ac.in',
                   'hosted_on': 'cloud',
                   'key': KEY}

        headers = {'Content-Type': 'application/json'}

        response = self.client.post("/hosting_info", data=json.dumps(payload),
                                 headers=headers)

        response = self.client.get("/hosting_info", headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
