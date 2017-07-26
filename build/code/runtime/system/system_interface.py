
# -*- coding: utf-8 -*-
from runtime.system.system import *
import datetime
from flask import current_app
from runtime.config.system_config import KEY

class SystemInterface ():

    def __init__(self):
        raise Error('Can not instantiate')

    @staticmethod
    def initialize(cls):
        System.initialize_system(cls)


    @staticmethod
    def add_lab(data_dict):
        session_cls = System.delegate.entities['session']
        lab_cls = System.delegate.entities['lab']
        exp_cls = System.delegate.entities['experiment']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        section_cls = System.delegate.entities['section']
        hosting_info_cls = System.delegate.entities['hosting_info']

        session = session_cls(key=data_dict['key'])
        del(data_dict['key'])

        section_list=data_dict['lab']['sections']        
        section_obj_list=[]
        for section_x in section_list:
            section = System.do("get_section", name=section_x['name'])
            if section is None:
                section = section_cls(name=str(section_x))
                section = System.do("add_section", section=section, session=session)
            section_obj_list.append(section)

        experiments=data_dict['lab']['experiments']
        exp_list = []
        for e_id in experiments:
            experiment = System.do("get_experiment", exp_id=e_id)
            exp_list.append(experiment)

        institute_id = data_dict['lab']['institute_id']
        institute = System.do("get_institute", institute_id=institute_id)

        integration_level = data_dict['lab']['integration_level']
        integration_status = System.do("get_integration_status",
                                           integration_level=integration_level)

        discipline_id = data_dict['lab']['discipline_id']
        discipline = System.do("get_discipline", discipline_id=discipline_id)

        assets = data_dict['lab']['assets']
        asset_list = []
        for asset_x in assets:
            asset_type = asset_type_cls(asset_type=str(asset_x['asset_type']))
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=\
                                                str(asset_x['asset_type']))
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)
            asset_list.append(asset)
 
        developers = data_dict['lab']['developers']
        developer_list = []
        for developer_x in developers:
            name = name_cls(name=developer_x['name'])
            email = email_cls(email=developer_x['email'])
            developer = System.do("get_developer", email=email)
            if developer is None:
                developer = developer_cls(name=name, email=email)
                developer = System.do("add_developer", developer=developer, session=session)
            developer_list.append(developer)

        hosting_info = data_dict['lab']['hosting_info']
        hosting_info_list = []
        for hosting_info_x in hosting_info:
            hosting_info = System.do("get_hosting_info", hosted_url=hosting_info_x['hosted_url'])
            if hosting_info is None:
                hosting_info = hosting_info_cls(hosting_status=str(hosting_info_x['hosting_status']), \
                                      hosted_url=str(hosting_info_x['hosted_url']), hosted_on=str(hosting_info_x['hosted_on']))
                hosting_info = System.do("add_hosting_info", hosting_info=hosting_info, session=session)
            hosting_info_list.append(hosting_info)

        lab = lab_cls(lab_name=data_dict['lab']['name'],
                                lab_id=data_dict['lab']['id'],
                                overview=data_dict['lab']['overview'],
                                institute=institute,
                                integration_status=integration_status,
                                discipline=discipline,
                                assets=asset_list,
                                experiments=exp_list,
                                developers=developer_list,
                                sections=section_obj_list,
                                hosting_info=hosting_info_list)
        try:
            current_app.logger.debug("running operation add_lab")
            lab = System.do("add_lab", lab=lab, session=session)
            current_app.logger.debug("completed operation add_lab")
            return lab.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_section(data_dict):
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']

        session = session_cls(key=data_dict['key'])
        section = section_cls(name=data_dict['name'])
        try:
            current_app.logger.debug("running operation add_section")
            question = System.do("add_section", section=section, 
                                    session=session)
            current_app.logger.debug("completed operation add_section")
            return section.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_experiment(data_dict):
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']
        experiment_cls = System.delegate.entities['experiment']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        developer_cls = System.delegate.entities['developer']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        hosting_info_cls = System.delegate.entities['hosting_info']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        session = session_cls(key=data_dict['key'])
        del(data_dict['key'])

        sections = data_dict['experiment']['sections']
        section_list = []
        for section_x in sections:
            section = System.do("get_section", name=section_x)
            if section is None:
                section = section_cls(name=str(section_x))
                section = System.do("add_section", section=section, session=session)
            section_list.append(section)

        institute_id = data_dict['experiment']['institute_id']
        institute = System.do("get_institute", institute_id=institute_id)

        discipline_id = data_dict['experiment']['discipline_id']
        discipline = System.do("get_discipline", discipline_id=discipline_id)

        integration_level = data_dict['experiment']['integration_level']
        integration_status = System.do("get_integration_status",
                                           integration_level=integration_level)

        assets = data_dict['experiment']['assets']
        asset_list = []
        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=\
                                                str(asset_x['asset_type']))
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)
            asset_list.append(asset)

        developers = data_dict['experiment']['developers']
        developer_list = []
        for developer_x in developers:
            name = name_cls(name=developer_x['name'])
            email = email_cls(email=developer_x['email'])
            developer = System.do("get_developer", email=email)
            if developer is None:
                developer = developer_cls(name=name, email=email)
                developer = System.do("add_developer", developer=developer,
                                          session=session)
            developer_list.append(developer)

        hosting_info = data_dict['experiment']['hosting_info']
        hosting_info_list = []
        for hosting_info_x in hosting_info:
            hosting_info = System.do("get_hosting_info", hosted_url=hosting_info_x['hosted_url'])
            if hosting_info is None:
                hosting_info = hosting_info_cls(hosting_status=str(hosting_info_x['hosting_status']), \
                                      hosted_url=str(hosting_info_x['hosted_url']), hosted_on=str(hosting_info_x['hosted_on']))
                hosting_info = System.do("add_hosting_info", hosting_info=hosting_info, session=session)
            hosting_info_list.append(hosting_info)

        experiment = experiment_cls(exp_name=data_dict['experiment']['name'],
                                exp_id=data_dict['experiment']['id'],
                                overview=data_dict['experiment']['overview'],
                                sections=section_list,
                                institute=institute,
                                discipline=discipline,
                                assets=asset_list,
                                integration_status=integration_status,
                                developers=developer_list,
                                hosting_info=hosting_info_list)
        try:
            current_app.logger.debug("running operation add_experiment")
            experiment = System.do("add_experiment", experiment=experiment, 
                                    session=session)
            current_app.logger.debug("completed operation add_experiment")
            return experiment

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_institute(data_dict):
        session_cls = System.delegate.entities['session']       
        institute_cls = System.delegate.entities['institute']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        session = session_cls(key=data_dict['key'])
        del(data_dict['key'])

        assets = data_dict['assets']
        asset_list = []
        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=asset_x['asset_type'])
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)

            asset_list.append(asset)

        institute = institute_cls(institute_name=str(data_dict['institute_name']),
                                  institute_id=str(data_dict['institute_id']),
                                  assets=asset_list)

        try:
            current_app.logger.debug("running operation add_institute")
            institute = System.do("add_institute", institute=institute,
                                    session=session)
            current_app.logger.debug("completed operation add_institute")
            return institute.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_discipline(data_dict):
        session_cls = System.delegate.entities['session']
        discipline_cls = System.delegate.entities['discipline']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']

        session = session_cls(key=data_dict['key'])

        assets = data_dict['assets']
        asset_list = []
        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=asset_x['asset_type'])
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)

            asset_list.append(asset)
 
        discipline = discipline_cls(discipline_name=data_dict['discipline_name'],
                                    discipline_id=data_dict['discipline_id'],
                                    assets=asset_list)
        try:
            current_app.logger.debug("running operation add_discipline")
            question = System.do("add_discipline", discipline=discipline, 
                                    session=session)
            current_app.logger.debug("completed operation add_discipline")
            return discipline.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_name(data_dict):
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']

        session = session_cls(key=data_dict['key'])
        name = name_cls(name=str(data_dict['name']))
        try:
            current_app.logger.debug("running operation add_section")
            question = System.do("add_name", name=name, session=session)
            current_app.logger.debug("completed operation add_name")
            return name.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_email(data_dict):
        session_cls = System.delegate.entities['session']
        email_cls = System.delegate.entities['email']

        session = session_cls(key=data_dict['key'])
        email = email_cls(email=str(data_dict['email']))
        try:
            current_app.logger.debug("running operation add_email")
            question = System.do("add_email", email=email, session=session)
            current_app.logger.debug("completed operation add_email")
            return email.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_developer(data_dict):
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']

        session = session_cls(key=data_dict['key'])
        name = name_cls(name=str(data_dict['name']))
        email = email_cls(email=str(data_dict['email']))

        developer = developer_cls(name=name, email=email)

        try:
            current_app.logger.debug("running operation add_developer")
            developer = System.do("add_developer", developer=developer,
                                    session=session)
            current_app.logger.debug("completed operation add_developer")

            return developer
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def get_labs():
        lab_cls = System.delegate.entities['lab']
        try:
            current_app.logger.debug("running operation get labs")
            labs = lab_cls.get_all()
            lab_dict_list = []
            for lab in labs:
                lab_x = lab.to_client()
                lab_dict_list.append(lab_x)
            current_app.logger.debug("got labs")
            return  lab_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def add_hosting_info(data_dict):
        session_cls = System.delegate.entities['session']       
        hosting_info_cls = System.delegate.entities['hosting_info']

        session = session_cls(key=data_dict['key'])
        del(data_dict['key'])

        hosting_info = hosting_info_cls(hosting_status=str(data_dict['hosting_status']),
                                  hosted_url=str(data_dict['hosted_url']),
                                  hosted_on=str(data_dict['hosted_on']))

        try:
            current_app.logger.debug("running operation add_hosting_info")
            hosting_info = System.do("add_hosting_info", hosting_info=hosting_info,
                                    session=session)
            current_app.logger.debug("completed operation add_hosting_info")
            return hosting_info.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def add_integration_status(data_dict):
        session_cls = System.delegate.entities['session']       
        integration_status_cls = System.delegate.entities['integration_status']

        session = session_cls(key=data_dict['key'])
        del(data_dict['key'])

        integration_status = integration_status_cls(integration_level=data_dict['integration_level'])

        try:
            current_app.logger.debug("running operation add_integration_status")
            integration_status = System.do("add_integration_status", integration_status=integration_status,
                                    session=session)
            current_app.logger.debug("completed operation add_integration_status")
            return integration_status.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err


    @staticmethod
    def get_lab_by_id(id):
        lab_cls = System.delegate.entities['lab']
        try:
            current_app.logger.debug("getting lab by id")
            lab = lab_cls.get_by_id(id)
            if not lab:
                return ("No lab found with id: %s" % (id))

            current_app.logger.debug("got lab by id: %s" % id)
            return lab.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_section_by_id(id):
        section_cls = System.delegate.entities['section']
        try:
            current_app.logger.debug("getting section by id")
            section = section_cls.get_by_id(id)
            if not section:
                return ("No section found with id: %s" % (id))

            current_app.logger.debug("got section by id = %s" % id)
            return section.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_institute_by_id(id):
        institute_cls = System.delegate.entities['institute']
        try:
            current_app.logger.debug("getting institute by id")
            institute = institute_cls.get_by_id(id)
            if not institute:
                return ("No institute found with id: %s" % (id))

            current_app.logger.debug("got institute by id = %s" % id)
            return institute.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_experiment_by_id(id):
        experiment_cls = System.delegate.entities['experiment']
        try:
            current_app.logger.debug("getting experiment by id")
            experiment = experiment_cls.get_by_id(id)
            if not experiment:
                return ("No experiment found with id: %s" % (id))

            current_app.logger.debug("got experiment by id = %s" % id)
            return experiment.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_discipline_by_id(id):
        discipline_cls = System.delegate.entities['discipline']
        try:
            current_app.logger.debug("getting discipline by id")
            discipline = discipline_cls.get_by_id(id)
            if not discipline:
                return ("No discipline found with id: %s" % (id))

            current_app.logger.debug("got discipline by id = %s" % id)
            return discipline.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_developer(email_id):
        try:
            email_cls = System.delegate.entities['email']
            email = email_cls(email=str(email_id))

            current_app.logger.debug("running operation get_lab_by_lab_id")
            developer = System.do("get_developer", email=email)
            current_app.logger.debug("completed operation get_lab_by_lab_id")
            if not developer:
                return ("No Developer found with email: %s" % (email_id))
            return developer.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_integration_status_by_IL(integration_level):
        try:
            current_app.logger.debug("running operation get_integration_status_"
                                     " by_integration_level")
            integration_status_id = System.do("get_integration_status_by_IL", 
                                      integration_level=int(integration_level))
            current_app.logger.debug("completed operation get_integration_"
                                     " status_by_integration_level")
            return integration_status_id

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_labs_by_keyword_lab_name(keyword):
        lab_cls = System.delegate.entities['lab']
        try:
            current_app.logger.debug("running get labs by keyword" 
                                     " lab name")
            labs = lab_cls.get_all()
            labs_match_list=[]
            for lab in labs:
                lab_x = lab.to_client()
                if keyword.lower() in (lab_x['lab_name']).lower():
                    labs_match_list.append(lab_x)

            current_app.logger.debug("got labs by keyword lab name")
            return  labs_match_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_lab(lab_id, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))
        try:
            current_app.logger.debug("running operation delete_lab")
            lab = System.do("delete_lab", lab_id=str(lab_id), session=session)
            current_app.logger.debug("completed operation delete_lab")
            return lab
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_discipline(discipline_id, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))

        try:
            current_app.logger.debug("running operation delete_discipline")
            discipline_id = System.do("delete_discipline", discipline_id=str(discipline_id),
                                    session=session)
            current_app.logger.debug("completed operation delete_discipline")
            return discipline_id
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_institute(institute_id, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))

        try:
            current_app.logger.debug("running operation delete_institute")
            institute_id = System.do("delete_institute", institute_id=str(institute_id),
                                      session=session)
            current_app.logger.debug("completed operation delete_institute")
            return institute_id
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_experiment(exp_id, key):
        session_cls = System.delegate.entities['session']

        session = session_cls(key=str(key))
        try:
            current_app.logger.debug("running operation delete_experiment")
            exp = System.do("delete_experiment", exp_id=str(exp_id),
                                    session=session)
            current_app.logger.debug("completed operation delete_experiment")
            return exp
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_section(s_id):
        session_cls = System.delegate.entities['session']

        session = session_cls(key=KEY)
        try:
            current_app.logger.debug("running operation delete_section")
            section = System.do("delete_section", s_id=int(s_id),
                                    session=session)
            current_app.logger.debug("completed operation delete_section")
            return section
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_discipline(discipline_id, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))

        try:
            current_app.logger.debug("running operation delete_discipline")
            discipline_id = System.do("delete_discipline", discipline_id=str(discipline_id),
                                    session=session)
            current_app.logger.debug("completed operation delete_discipline")
            return discipline_id
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_hosting_info(hosted_url, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))

        try:
            current_app.logger.debug("running operation delete_hosting_info")
            hosting_info_id = System.do("delete_hosting_info", hosted_url=str(hosted_url),
                                      session=session)
            current_app.logger.debug("completed operation delete_hosting_info")
            return hosting_info_id
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_integration_status(integration_level, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))

        try:
            current_app.logger.debug("running operation delete_integration_status")
            integration_status_id = System.do("delete_integration_status", 
                                      integration_level=int(integration_level),
                                      session=session)
            current_app.logger.debug("completed operation delete_integration_status")
            return integration_status_id

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def update_lab(data_dict):
        session_cls = System.delegate.entities['session']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        hosting_info_cls = System.delegate.entities['hosting_info']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        developer_cls = System.delegate.entities['developer']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        section_cls = System.delegate.entities['section']

        session = session_cls(key=data_dict['key'])

        lab_id = str(data_dict['lab']['id'])
        lab = System.do("get_lab", lab_id=lab_id)

        if 'name' not in data_dict['lab']:
            lab_name=str(lab.get("lab_name"))
        else:
            lab_name=data_dict['lab']['name']

        if 'overview' not in data_dict['lab']:
            overview=str(lab.get("overview"))
        else:
            overview=data_dict['lab']['overview']

        if 'institute_id' not in data_dict['lab']:
            inst=str(lab.get("institute"))
        else:
            inst = System.do("get_institute", institute_id=
                                      data_dict['lab']['institute_id'])

        if 'discipline_id' not in data_dict['lab']:
            dis=str(lab.get("discipline"))
        else:
            dis = System.do("get_discipline", discipline_id=
                                       data_dict['lab']['discipline_id'])

        if 'integration_level' not in data_dict['lab']:
            integration_status=str(lab.get("integration_status"))
        else:
            integration_status = System.do("get_integration_status_by_IL",
                             integration_level=data_dict['lab']['integration_level'])

        hosting_info = data_dict['lab']['hosting_info']
        hosting_info_list = []
        for hosting_info_x in hosting_info:
            hosting_info = System.do("get_hosting_info",
                                         hosted_url=
                                         hosting_info_x['hosted_url'])
            if hosting_info is None:
                hosting_info = hosting_info_cls(hosting_status=str(hosting_info_x['hosting_status']), \
                                      hosted_url=str(hosting_info_x['hosted_url']), hosted_on=str(hosting_info_x['hosted_on']))
                hosting_info = System.do("add_hosting_info", hosting_info=hosting_info, session=session)
            hosting_info_list.append(hosting_info)

        assets = data_dict['lab']['assets']
        asset_list = []

        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=\
                                                str(asset_x['asset_type']))
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)
            asset_list.append(asset)

        section_list=[]
        for section in data_dict['lab']['sections']:
            if 'experiments' in section.keys():
                experiments = section['experiments']
            else:
                section_list.append(section['name'])

        section_obj_list=[]
        for section_x in section_obj_list:
            section = System.do("get_section", name=section_x['name'])
            if section is None:
                section = section_cls(name=str(section_x['name']))
                section = System.do("add_section", section=section, session=session)
            section_obj_list.append(section)

        developers = data_dict['lab']['developers']
        developer_list = []
        for developer_x in developers:
            name = name_cls(name=developer_x['name'])
            email = email_cls(email=developer_x['email'])
            developer = System.do("get_developer", email=email)
            if developer is None:
                developer = developer_cls(name=name, email=email)
                developer = System.do("add_developer", developer=developer, session=session)
            developer_list.append(developer)

        experiments = data_dict['lab']['experiments']

        exp_list = []
        for e_id in experiments:
            experiment = System.do("get_experiment", exp_id=e_id)
            exp_list.append(experiment)

        try:
            current_app.logger.debug("running operation update_lab")
            lab = System.do("update_lab", lab=lab,
                                    lab_name=lab_name,
                                    overview=overview, session=session,
                                    institute=inst,
                                    discipline=dis,
                                    hosting_info=hosting_info_list,
                                    assets=asset_list,
                                    experiments=exp_list,
                                    developers=developer_list,
                                    sections=section_obj_list,
                                    integration_status=integration_status)
            current_app.logger.debug("completed operation update_lab")
            return lab.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def update_institute(data_dict):
        session_cls = System.delegate.entities['session']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        session = session_cls(key=str(data_dict['key']))

        institute = System.do("get_institute", institute_id=str(data_dict['institute_id']))

        assets = data_dict['assets']
        asset_list = []
        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=asset_x['asset_type'])
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)
            asset_list.append(asset)

        if 'institute_name' not in data_dict:
            institute_name=str(inst.get("institute_name"))
        else:
            institute_name=data_dict['institute_name']

        try:
            current_app.logger.debug("running operation update_institute")
            institute = System.do("update_institute", institute=institute,
                                    institute_name=institute_name, 
                                    session=session, assets=asset_list)
            current_app.logger.debug("completed operation update_institute")
            return institute
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_section(data_dict):
        session_cls = System.delegate.entities['session']
        section_cls = System.delegate.entities['section']

        session = session_cls(key=data_dict['key'])
        section = section_cls.get_by_id(data_dict['s_id'])

        if 'name' not in data_dict:
            name=str(section.get("name"))
        else:
            name=data_dict['name']

        try:
            current_app.logger.debug("running operation update_section")
            section = System.do("update_section", section=section, name=name,\
                                             session=session)
            current_app.logger.debug("completed operation update_section")
            return section.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_experiment(data_dict):
        session_cls = System.delegate.entities['session']
        exp_cls = System.delegate.entities['experiment']
        institute_cls = System.delegate.entities['institute']
        discipline_cls = System.delegate.entities['discipline']
        hosting_info_cls = System.delegate.entities['hosting_info']
        developer_cls = System.delegate.entities['developer']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        section_cls = System.delegate.entities['section']
        session = session_cls(key=str(data_dict['key']))

        exp_id=str(data_dict['experiment']['id'])
        experiment = System.do("get_experiment", exp_id=exp_id)
        if 'name' not in data_dict['experiment']:
            exp_name=str(experiment.get("exp_name"))
        else:
            exp_name=data_dict['experiment']['name']

        if 'overview' not in data_dict['experiment']:
            overview=str(experiment.get("overview"))
        else:
            overview=data_dict['experiment']['overview']

        if 'institute_id' not in data_dict['experiment']:
            inst=str(experiment.get("institute"))
        else:
            inst= System.do("get_institute", institute_id=
                                data_dict['experiment']['institute_id'])

        if 'discipline_id' not in data_dict['experiment']:
            disc=str(experiment.get("discipline"))
        else:
            disc= System.do("get_discipline", discipline_id=
                                data_dict['experiment']['discipline_id'])

        if 'integration_level' not in data_dict['experiment']:
            integration_status=str(experiment.get("integration_status"))
        else:
            integration_status= System.do("get_integration_status_by_IL", 
                      integration_level=
                        data_dict['experiment']['integration_level'])

        hosting_info = data_dict['experiment']['hosting_info']
        hosting_info_list = []
        for hosting_info_x in hosting_info:
            hosting_info = System.do("get_hosting_info",
                                         hosted_url=
                                         hosting_info_x['hosted_url'])
            if hosting_info is None:
                hosting_info = hosting_info_cls(hosting_status=\
                                                    str(hosting_info_x\
                                                        ['hosting_status']), \
                                                    hosted_url=\
                                                    str(hosting_info_x\
                                                        ['hosted_url']), \
                                                    hosted_on=\
                                                    str(hosting_info_x\
                                                            ['hosted_on']))
                hosting_info = System.do("add_hosting_info", \
                                             hosting_info=hosting_info, \
                                             session=session)
            hosting_info_list.append(hosting_info)

        assets = data_dict['experiment']['assets']
        asset_list = []
        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=\
                                                str(asset_x['asset_type']))
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)
            asset_list.append(asset)

        developers = data_dict['experiment']['developers']
        developer_list = []
        for developer_x in developers:
            name = name_cls(name=developer_x['name'])
            email = email_cls(email=developer_x['email'])
            developer = System.do("get_developer", email=email)
            if developer is None:
                developer = developer_cls(name=name, email=email)
                developer = System.do("add_developer", developer=developer,
                                          session=session)
            developer_list.append(developer)

        sections = data_dict['experiment']['sections']
        section_list = []
        for section_x in sections:
            section = System.do("get_section", name=section_x)
            if section is None:
                section = section_cls(name=str(section_x))
                section = System.do("add_section", section=section, session=session)
            section_list.append(section)

        try:
            current_app.logger.debug("running operation update_experiment")
            exp = System.do("update_experiment", exp_name=exp_name, 
                                    experiment=experiment, overview=overview,
                                    session=session, institute=inst, 
                                    discipline=disc, 
                                    integration_status=integration_status, 
                                    hosting_info=hosting_info_list,
                                    assets=asset_list, 
                                    developers=developer_list,
                                    sections=section_list)
            current_app.logger.debug("completed operation update_experiment")
            return exp.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_discipline(data_dict):
        session_cls = System.delegate.entities['session']
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
        session = session_cls(key=data_dict['key'])

        discipline_id = str(data_dict['discipline_id'])
        discipline = System.do("get_discipline", discipline_id=discipline_id)

        assets = data_dict['assets']
        asset_list = []
        for asset_x in assets:
            asset = System.do("get_asset", path=asset_x['path'])
            if asset is None:
                asset_type = asset_type_cls(asset_type=asset_x['asset_type'])
                asset = asset_cls(asset_type=asset_type, \
                                      path=str(asset_x['path']))
                asset = System.do("add_asset", asset=asset, session=session)
            asset_list.append(asset)

        if "discipline_name" not in data_dict:
            discipline_name=str(discipline.get("discipline_name"))
        else:
            discipline_name=data_dict["discipline_name"]

        try:
            current_app.logger.debug("running operation update_discipline")
            discipline = System.do("update_discipline", discipline=discipline,
                                    discipline_name=discipline_name, 
                                    session=session, assets=asset_list)
            current_app.logger.debug("completed operation update_discipline")
            return discipline
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_hosting_info(data_dict):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=data_dict['key'])

        hosted_url = str(data_dict['hosted_url'])
        hosting_info = System.do("get_hosting_info", hosted_url=hosted_url)

        if 'hosting_status' not in data_dict:
            hosting_status=str(hosting_info.get("hosting_status"))
        else:
            hosting_status=data_dict['hosting_status']

        if 'hosted_on' not in data_dict:
            hosted_on=str(hosting_info.get("hosted_on"))
        else:
            hosted_on=data_dict['hosted_on']

        try:
            current_app.logger.debug("running operation update_hosting_info")
            hosting_info = System.do("update_hosting_info", hosting_info=hosting_info,
                                    hosting_status=hosting_status, hosted_on=hosted_on,
                                    session=session)
            current_app.logger.debug("completed operation update_hosting_info")
            return hosting_info.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_asset(data_dict):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(data_dict['key']))
        asset_type_cls = System.delegate.entities['asset_type']
        
        path = str(data_dict['path'])
        asset = System.do("get_asset", path=path)

        if 'asset_type' not in data_dict:
            asset_type=str(asset.get("asset_type"))
        else:
            asset_type = asset_type_cls(asset_type=\
                                            str(data_dict['asset_type']))


        try:
            current_app.logger.debug("running operation update_asset")
            asset = System.do("update_asset", asset=asset,
                                    asset_type=asset_type, 
                                    session=session)
            current_app.logger.debug("completed operation update_asset")
            return asset.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def get_labs():
        lab_cls = System.delegate.entities['lab']
        try:
            current_app.logger.debug("running operation get labs")
            labs = lab_cls.get_all()
            lab_dict_list = []
            for lab in labs:
                lab_x = lab.to_client()
                lab_dict_list.append(lab_x)
            current_app.logger.debug("got labs")
            return  lab_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_experiments():
        experiment_cls = System.delegate.entities['experiment']
        try:
            current_app.logger.debug("getting experiments")
            experiments = experiment_cls.get_all()
            exp_dict_list = [] 
            for exp in experiments:
                exp_x = exp.to_client()
                exp_dict_list.append(exp_x)
            current_app.logger.debug("got experiments")
            return  exp_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_institutes():
        institute_cls = System.delegate.entities['institute']
        try:
            current_app.logger.debug("getting institutes")
            institutes = institute_cls.get_all()
            inst_dict_list = []
            for inst in institutes:
                inst_x = inst.to_client()
                inst_dict_list.append(inst_x)
            current_app.logger.debug("got institutes")
            return  inst_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_disciplines():
        discipline_cls = System.delegate.entities['discipline']
        try:
            current_app.logger.debug("getting disciplines")
            disciplines = discipline_cls.get_all()
            dis_dict_list = []
            for dis in disciplines:
                dis_x = dis.to_client()
                dis_dict_list.append(dis_x)
            current_app.logger.debug("got disciplines")
            return  dis_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_hosting_info():
        hosting_info_cls = System.delegate.entities['hosting_info']
        try:
            current_app.logger.debug("getting hosting_info")
            hosting_info = hosting_info_cls.get_all()
            host_dict_list = []
            for host in hosting_info:
                host_x = host.to_client()
                host_dict_list.append(host_x)
            current_app.logger.debug("got hosting_infos")
            return  host_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_integration_status():
        integration_status_cls = System.delegate.entities['integration_status']
        try:
            current_app.logger.debug("getting integration_status")
            integration_status = integration_status_cls.get_all()
            intstatus_dict_list = []
            for intstatus in integration_status:
                intstatus_x = intstatus.to_client()
                intstatus_dict_list.append(intstatus_x)
            current_app.logger.debug("got integration_status")
            return  intstatus_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def get_lab(lab_id):
        try:
            current_app.logger.debug("running operation get_lab_by_lab_id")
            lab = System.do("get_lab", lab_id=str(lab_id))
            current_app.logger.debug("completed operation get_lab_by_lab_id")
            if not lab:
                return ("No lab found with labid: %s" % (lab_id))
            return lab.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_experiment(exp_id):
        try:
            current_app.logger.debug("running operation get_lab_by_exp_id")
            exp = System.do("get_experiment", exp_id=str(exp_id))
            current_app.logger.debug("completed operation get_lab_by_exp_id")
            if not exp:
                return ("No exp found with expid: %s" % (exp_id))
            return exp.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_institute(institute_id):
        session_cls = System.delegate.entities['session']
        try:
            current_app.logger.debug("running operation get_institute_by_institute_id")
            institute = System.do("get_institute", institute_id=str(institute_id))
            current_app.logger.debug("completed operation get_institute_by_institute_id")
            if not institute:
                return ("No institute found with instituteid: %s" % (institute_id))
            return institute.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_discipline(discipline_id):
        try:
            current_app.logger.debug("running operation get_discipline_by_discipline_id")
            dis = System.do("get_discipline", discipline_id=str(discipline_id))
            current_app.logger.debug("completed operation get_institute_by_institute_id")
            if not dis:
                return ("No discipline found with disid: %s" % (discipline_id))
            return dis.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_labs_by_institute(institute_name):
        institute = System.do("get_institute_by_institute_name",
                                  institute_name=str(institute_name))
        try:
            current_app.logger.debug("running operation get_labs_by_institute")
            labs = System.do("get_labs_by_institute", institute=institute)
            current_app.logger.debug("completed operation get_labs_by_institute")
            labs_dict_list = []
            for lab in labs:
                lab_x = lab.to_client()
                labs_dict_list.append(lab_x)
            current_app.logger.debug("got labs")
            return  labs_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_labs_by_lab_name(lab_name):

        try:
            current_app.logger.debug("running operation get_labs_by_lab_name")
            labs = System.do("get_labs_by_lab_name", lab_name=str(lab_name))
            current_app.logger.debug("completed operation get_labs_by_lab_name")
            labs_dict_list = []
            for lab in labs:
                lab_x = lab.to_client()
                labs_dict_list.append(lab_x)
            current_app.logger.debug("got labs")
            return  labs_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_labs_by_discipline(discipline_name):
        discipline = System.do("get_discipline_by_discipline_name",
                                  discipline_name=str(discipline_name))
        try:
            current_app.logger.debug("running operation get_labs_by_discipline")
            labs = System.do("get_labs_by_discipline", discipline=discipline)
            current_app.logger.debug("completed operation get_labs_by_discipline")
            labs_dict_list = []
            for lab in labs:
                lab_x = lab.to_client()
                labs_dict_list.append(lab_x)
            current_app.logger.debug("got labs")
            return  labs_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_labs_by_asset(asset_type):
        asset = System.do("get_asset_by_asset_type",
                                  asset_type=str(asset_type))
        try:
            current_app.logger.debug("running operation get_labs_by_asset_type")
            labs = System.do("get_labs_by_asset", asset=asset)
            current_app.logger.debug("completed operation get_labs_by_asset_type")
            labs_dict_list = []
            for lab in labs:
                lab_x = lab.to_client()
                labs_dict_list.append(lab_x)
            current_app.logger.debug("got labs")
            return  labs_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_name(data_dict):
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']

        session = session_cls(key=data_dict['key'])
        name = name_cls.get_by_id(data_dict['n_id'])

        if 'name' not in data_dict:
            n_name=str(name.get("name"))
        else:
            n_name=data_dict['name']

        try:
            current_app.logger.debug("running operation update_name")
            name = System.do("update_name", name=name, n_name=n_name,\
                                             session=session)
            current_app.logger.debug("completed operation update_name")
            return name.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_sections():
        section_cls = System.delegate.entities['section']
        try:
            current_app.logger.debug("getting sections")
            sections = section_cls.get_all()
            section_dict_list = []
            for section in sections:
                section_x = section.to_client()
                section_dict_list.append(section_x)
            current_app.logger.debug("got sections")
            return  section_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def update_developer(data_dict):
        session_cls = System.delegate.entities['session']
        name_cls = System.delegate.entities['name']
        email_cls = System.delegate.entities['email']
        developer_cls = System.delegate.entities['developer']

        session = session_cls(key=str(data_dict['key']))
        email = email_cls(email=str(data_dict['email']))
        developer = System.do("get_developer", email=email)

        if 'name' not in data_dict:
            name=developer.get("name")
        else:
            name=name_cls(name=str(data_dict['name']))

        try:
            current_app.logger.debug("running operation update_developer")
            developer = System.do("update_developer", name=name,
                                      developer=developer, session=session)
            current_app.logger.debug("completed operation update_developer")
            return developer

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def get_names():
        name_cls = System.delegate.entities['name']
        try:
            current_app.logger.debug("getting names")
            names = name_cls.get_all()
            name_dict_list = []
            for name in names:
                name_x = name.to_client()
                name_dict_list.append(name_x)
            current_app.logger.debug("got names")
            return  name_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_emails():
        email_cls = System.delegate.entities['email']
        try:
            current_app.logger.debug("getting emails")
            emails = email_cls.get_all()
            email_dict_list = []
            for email in emails:
                email_x = email.to_client()
                email_dict_list.append(email_x)
            current_app.logger.debug("got emails")
            return  email_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_developers():
        developer_cls = System.delegate.entities['developer']
        try:
            current_app.logger.debug("getting developers")
            developers = developer_cls.get_all()
            developer_dict_list = []
            for developer in developers:
                developer_x = developer.to_client()
                developer_dict_list.append(developer_x)
            current_app.logger.debug("got developers")
            return  developer_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_name(id):
        session_cls = System.delegate.entities['session']

        session = session_cls(key=KEY)
        try:
            current_app.logger.debug("running operation delete_name")
            name = System.do("delete_name", n_id=int(id), session=session)
            current_app.logger.debug("completed operation delete_name")
            return name
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_email(email, key):
        session_cls = System.delegate.entities['session']
        email_cls = System.delegate.entities['email']

        session = session_cls(key=str(key))
        email = email_cls(email=str(email))

        try:
            current_app.logger.debug("running operation delete_email")
            email = System.do("delete_email", email=email,
                                    session=session)
            current_app.logger.debug("completed operation delete_email")
            return email
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_developer(email, key):
        session_cls = System.delegate.entities['session']
        email_cls = System.delegate.entities['email']

        session = session_cls(key=str(key))
        email = email_cls(email=str(email))

        try:
            current_app.logger.debug("running operation delete_developer")
            developer = System.do("delete_developer", email=email,
                                    session=session)
            current_app.logger.debug("completed operation delete_developer")
            return developer

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def add_asset(data_dict):
        session_cls = System.delegate.entities['session']       
        asset_cls = System.delegate.entities['asset']
        asset_type_cls = System.delegate.entities['asset_type']
    
        session = session_cls(key=data_dict['key'])
        del(data_dict['key'])

        asset_type = asset_type_cls(asset_type=str(data_dict['asset_type']))
        asset = asset_cls(asset_type=asset_type, path=str(data_dict['path']))

        try:
            current_app.logger.debug("running operation add_asset")
            asset = System.do("add_asset", asset=asset,
                                    session=session)
            current_app.logger.debug("completed operation add_asset")
            return asset.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

    @staticmethod
    def update_asset(data_dict):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(data_dict['key']))
        asset_type_cls = System.delegate.entities['asset_type']
        
        path = str(data_dict['path'])
        asset = System.do("get_asset", path=path)

        if 'asset_type' not in data_dict:
            asset_type=str(asset.get("asset_type"))
        else:
            asset_type = asset_type_cls(asset_type=\
                                            str(data_dict['asset_type']))


        try:
            current_app.logger.debug("running operation update_asset")
            asset = System.do("update_asset", asset=asset,
                                    asset_type=asset_type, 
                                    session=session)
            current_app.logger.debug("completed operation update_asset")
            return asset.to_client()
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def delete_asset(path, key):
        session_cls = System.delegate.entities['session']
        session = session_cls(key=str(key))

        try:
            current_app.logger.debug("running operation delete_asset")
            asset_path = System.do("delete_asset", path=str(path),
                                      session=session)
            current_app.logger.debug("completed operation delete_asset")
            return asset_path
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_assets():
        asset_cls = System.delegate.entities['asset']

        try:
            current_app.logger.debug("getting assets")
            assets = asset_cls.get_all()
            asset_dict_list = []
            for asset in assets:
                asset_x = asset.to_client()
                asset_dict_list.append(asset_x)
            current_app.logger.debug("got assets")
            return  asset_dict_list

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_asset_by_path(path):
        asset_cls = System.delegate.entities['asset']

        try:
            current_app.logger.debug("running get_asset_by_path")
            asset = System.do("get_asset", path=str(path))
            current_app.logger.debug("completed operation get_asset_by_path")
            if not asset:
                return ("No asset found with path: %s" % (path))
            return asset.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_hosting_info_by_hosted_url(hosted_url):
        hosting_info_cls = System.delegate.entities['hosting_info']
        try:
            current_app.logger.debug("getting hosting_info by hosted URL")
            hosting_info = System.do("get_hosting_info", hosted_url=str(hosted_url))
            current_app.logger.debug("completed operation get_hosting_info_by_hosted_url")
            if not hosting_info:
                return ("No hosting_info found with hosted_url: %s" % (hosted_url))
            return hosting_info.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
    @staticmethod
    def get_name_by_id(id):
        name_cls = System.delegate.entities['name']
        try:
            current_app.logger.debug("getting name by id")
            name = name_cls.get_by_id(id)
            if not name:
                return ("No name found with id: %s" % (id))

            current_app.logger.debug("got developer name by id = %s" % id)
            return name.to_client()

        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err
