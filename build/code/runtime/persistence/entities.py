
# -*- coding: utf-8 -*-
from runtime.objects.entities import *
from runtime.utils.class_persistence_template import *
import datetime

lab_experiments = db.Table('lab_experiments',
		      db.Column('labid', db.Integer, 
                            db.ForeignKey('lab.id')),
		      db.Column('expid', db.Integer,
                            db.ForeignKey('experiment.id')))

lab_assets = db.Table('lab_assets',
                 db.Column('labid', db.Integer, 
                       db.ForeignKey('lab.id')),
		 db.Column('assetid', db.Integer,
                       db.ForeignKey('asset.id')))
                     
lab_developers = db.Table('lab_developers',
		      db.Column('labid', db.Integer, 
                            db.ForeignKey('lab.id')),
		      db.Column('developer_id', db.Integer,
                            db.ForeignKey('developer.id')))

lab_hosting_info = db.Table('lab_hosting_info',
                 db.Column('labid', db.Integer, 
                       db.ForeignKey('lab.id')),
		 db.Column('hosting_infoid', db.Integer,
                       db.ForeignKey('hosting_info.id')))

labs_sections = db.Table('labs_sections',
		      db.Column('labid', db.Integer, 
                            db.ForeignKey('lab.id')),
		      db.Column('section_id', db.Integer,
                            db.ForeignKey('section.id')))

args = {"__tablename__": "lab",
        "id": db.Column(db.Integer, primary_key=True),
        "lab_id": db.Column(db.String(255), unique=True, nullable=False),
        "lab_name": db.Column(db.String(255), unique=False, 
                                       nullable=True),
        "overview": db.Column(db.String(1000), unique=False, 
                                       nullable=True),
        "experiments": db.relationship('Experiment',
                    secondary=lab_experiments, 
                    backref='labs'),
        "institute_id": db.Column(db.Integer, db.ForeignKey('institute.id'), 
                                      unique=False, nullable=False),
        "discipline_id": db.Column(db.Integer, db.ForeignKey('discipline.id'), 
                                      unique=False, nullable=False),

        "integration_status_id": db.Column(db.Integer,
                                               db.ForeignKey\
                                               ('integration_status.id'),
                                               unique=False, nullable=False),
        "assets": db.relationship('Asset',
                    secondary=lab_assets, 
                    backref='labs'),
        "developers": db.relationship('Developer',
                    secondary=lab_developers, 
                    backref='labs'),
        "hosting_info": db.relationship('HostingInfo',
                    secondary=lab_hosting_info, 
                    backref='labs'),
        "sections": db.relationship('Section',
                    secondary=labs_sections, 
                    backref='labs')

       }

Lab = ClassPersistenceTemplate.mk_persistent(Lab, ['lab_id'],\
                                                 **args)

experiments_sections = db.Table('experiments_sections',
		      db.Column('experiment_id', db.Integer, 
                            db.ForeignKey('experiment.id')),
		      db.Column('section_id', db.Integer,
                            db.ForeignKey('section.id')))

experiments_assets = db.Table('experiments_assets',
                 db.Column('experimentid', db.Integer, 
                       db.ForeignKey('experiment.id')),
		 db.Column('assetid', db.Integer,
                       db.ForeignKey('asset.id')))

experiments_developers = db.Table('experiments_developers',
		      db.Column('experiment_id', db.Integer, 
                            db.ForeignKey('experiment.id')),
		      db.Column('developer_id', db.Integer,
                            db.ForeignKey('developer.id')))

experiments_hosting_info = db.Table('experiments_hosting_info',
                 db.Column('experimentid', db.Integer, 
                       db.ForeignKey('experiment.id')),
		 db.Column('hosting_infoid', db.Integer,
                       db.ForeignKey('hosting_info.id')))


disciplines_assets = db.Table('disciplines_assets',
		      db.Column('discipline_id', db.Integer, 
                            db.ForeignKey('discipline.id')),
		      db.Column('assetid', db.Integer,
                            db.ForeignKey('asset.id')))

institutes_labs = db.Table('institutes_labs',
		      db.Column('institute_id', db.Integer, 
                            db.ForeignKey('institute.id')),
		      db.Column('lab_id', db.Integer,
                            db.ForeignKey('lab.id')))

institutes_assets = db.Table('institutes_assets',
		      db.Column('institute_id', db.Integer, 
                            db.ForeignKey('institute.id')),
		      db.Column('assetid', db.Integer,
                            db.ForeignKey('asset.id')))

args = {"__tablename__": "experiment",
        "id": db.Column(db.Integer, primary_key=True),
        "exp_name": db.Column(db.String(255), unique=False, nullable=True),
        "exp_id": db.Column(db.String(255), unique=True, nullable=False),
        "overview": db.Column(db.String(1000), unique=False, nullable=True),
        "intstatus_id": db.Column(db.Integer, db.ForeignKey\
                                      ('integration_status.id'),
                                      unique=False, nullable=False),
        "assets": db.relationship('Asset',
                    secondary=experiments_assets, 
                    backref='experiments'),
        "lb_id": db.Column(db.Integer, 
                                db.ForeignKey('lab.id'), 
                                unique=False),

        "sections": db.relationship('Section',
                    secondary=experiments_sections, 
                    backref='experiments'),

        "institute_id": db.Column(db.Integer, db.ForeignKey('institute.id'), 
                                      unique=False, nullable=False),
        "discipline_id": db.Column(db.Integer, db.ForeignKey('discipline.id'), 
                                      unique=False, nullable=False),

        "developers": db.relationship('Developer',
                    secondary=experiments_developers, 
                    backref='experiments'),
        "hosting_info": db.relationship('HostingInfo',
                    secondary=experiments_hosting_info, 
                    backref='experiments')
        }

Experiment = ClassPersistenceTemplate.mk_persistent(Experiment, ['exp_id'],
                                                        **args)

args = {"__tablename__": "institute",
        "id": db.Column(db.Integer, primary_key=True),
        "institute_name": db.Column(db.String(255), unique=False, nullable=True),
        "institute_id": db.Column(db.String(255), unique=True, nullable=False),
        "labs": db.relationship('Lab', backref=db.backref('institute')),
        "experiments": db.relationship('Experiment', backref=\
                                           db.backref('institute')),
        "assets": db.relationship('Asset', secondary=institutes_assets,
                                      backref='institutes')
       }

Institute = ClassPersistenceTemplate.mk_persistent(Institute, ['institute_id'],\
                                                       **args)

args = {"__tablename__": "discipline",
        "id": db.Column(db.Integer, primary_key=True),
        "discipline_name": db.Column(db.String(255), unique=False, nullable=True),
        "discipline_id": db.Column(db.String(255), unique=True, nullable=False),
        "labs": db.relationship('Lab', backref=db.backref('discipline')),
        "experiments": db.relationship('Experiment', backref=\
                                           db.backref('discipline')),
        "assets": db.relationship('Asset', secondary=disciplines_assets,
                                      backref='disciplines')
        }

Discipline = ClassPersistenceTemplate.mk_persistent(Discipline, ['discipline_id'],\
                                                        **args)

args = {"__tablename__": "section",
        "id": db.Column(db.Integer, primary_key=True),
        "name": db.Column(db.String(255), unique=True, nullable=False)
        }

Section = ClassPersistenceTemplate.mk_persistent(Section, ['name'], **args)

args = {"__tablename__": "name",
        "id": db.Column(db.Integer, primary_key=True),
        "name": db.Column(db.String(255), unique=False,
                                       nullable=True),
        "developers": db.relationship('Developer', 
                                        backref=db.backref('name'))

        }

Name = ClassPersistenceTemplate.mk_persistent(Name, [], **args)
args = {"__tablename__": "email",
        "id": db.Column(db.Integer, primary_key=True),
        "email": db.Column(db.String(255), unique=True, nullable=False),
        "developers": db.relationship('Developer', 
                                        backref=db.backref('email'))
        }

Email = ClassPersistenceTemplate.mk_persistent(Email, ['email'], **args)
args = {"__tablename__": "developer",
        "id": db.Column(db.Integer, primary_key=True),
        "name_id": db.Column(db.Integer, db.ForeignKey('name.id'),
                                 nullable=False),
        "email_id": db.Column(db.Integer,db.ForeignKey('email.id'),
                                 unique=True, nullable=False)
        }

Developer = ClassPersistenceTemplate.mk_persistent(Developer, [], **args)
args = {"__tablename__": "hosting_info",
        "id": db.Column(db.Integer, primary_key=True),
        "hosting_status": db.Column(db.String(255), unique=False,\
                                        nullable=True),
        "hosted_url": db.Column(db.String(255), unique=True, nullable=False),
        "hosted_on": db.Column(db.String(255), unique=False, nullable=True),
       }

HostingInfo = ClassPersistenceTemplate.mk_persistent(HostingInfo,\
                                                         ['hosted_url'],\
                                                         **args)

args = {"__tablename__": "asset_type",
        "id": db.Column(db.Integer, primary_key=True),
        "asset_type": db.Column(db.String(255), unique=True, nullable=False),
        "assets": db.relationship('Asset', backref=db.backref('asset_type'))
        }

AssetType = ClassPersistenceTemplate.mk_persistent(AssetType, ['asset_type'],
                                                       **args)
args = {"__tablename__": "asset",
        "id": db.Column(db.Integer, primary_key=True),
        "asset_type_id": db.Column(db.Integer,db.ForeignKey('asset_type.id'),
                                 unique=True, nullable=False),
        "path": db.Column(db.String(255), unique=True, nullable=False)
       }

Asset = ClassPersistenceTemplate.mk_persistent(Asset, ['path'], **args)

args = {"__tablename__": "integration_status",
        "id": db.Column(db.Integer, primary_key=True),
        "integration_level": db.Column(db.Integer, unique=True,\
                                           nullable=False),
        "labs": db.relationship('Lab', backref=\
                                    db.backref('integration_status')), 
        "experiments": db.relationship('Experiment', backref=\
                                           db.backref('integration_status')), 
        "integration_level": db.Column(db.Integer, unique=True,
                                           nullable=False),
        "labs": db.relationship('Lab', backref=\
                                    db.backref('integration_status'))
       }

IntegrationStatus = ClassPersistenceTemplate.mk_persistent(IntegrationStatus,
                                                ['integration_level'], **args)
