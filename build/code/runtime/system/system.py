
# -*- coding: utf-8 -*-

from runtime.exceptions.custom_exceptions import *
from runtime.objects.entities import is_str, is_lab, are_labs,\
     is_date, is_session, is_section, is_int, is_experiment,\
     are_experiments, are_sections, is_name, is_email, is_developer,\
     is_institute, are_institutes, is_discipline, are_disciplines,\
     is_url, is_hosting_info, is_integration_status, is_asset, are_assets,\
     is_asset_type, are_hosting_info, are_developers

from runtime.utils.type_utils import is_str_or_none
from runtime.config.system_config import KEY
import datetime
from flask import current_app

class System ():

    def __init__(self):
        raise Error('Can not instantiate')

    @staticmethod
    def initialize_system(cls):
        System.delegate = cls()

    @staticmethod
    def is_session_valid(session):
        return session.get("key") == KEY
 
   
    @staticmethod
    def arity_check(args, n):
       if  (len(args) != n) :
          raise ArityError("arity mismatch: size of args  does not " + 
                           "match operation arity " )

    @staticmethod
    def type_check(args, arg_types):
        for key, value in args.iteritems():
            if not arg_types[key](value):
                raise TypeError("type mismatch: argument %s is not of "
                                "type %s" % (value, key))

    @staticmethod   
    def do(op, **args):
        cls = ops_table[op]
        arg_types  = cls.arg_types
        auth_check = cls.auth_check
        state_check = cls.state_check
        arity_and_type_checks_needed = cls.arity_and_type_checks_needed
        try:
            if arity_and_type_checks_needed:
               System.arity_check(args.keys(), len(arg_types.keys()))
               System.type_check(args, arg_types)
            auth_check(args)
            state_check(args)
            return cls.action(args)
        except (ArityError, TypeError, NotAuthorizedError, StateError) as err:
            raise err

class AddLab():
    arg_types = {"lab": is_lab, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        lab = args["lab"]
        if System.delegate.lab_exists(lab):
            raise StateError("lab %s already exists in System"
                                 % lab.to_client())

    @staticmethod
    def action(args):
        lab = args["lab"]
        lab = System.delegate.add_lab(lab)
        return lab

class DeleteLab():
    arg_types = {"lab_id": is_str, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        lab_id = args['lab_id']
        lab = System.delegate.get_lab(lab_id=lab_id)
        if not System.delegate.lab_exists(lab):
            raise StateError("lab %s does not exists in System"
                                 % lab.to_client())

    @staticmethod
    def action(args):
        lab_id = args["lab_id"]
        lab_id = System.delegate.delete_lab(lab_id)
        return lab_id

class DeleteDiscipline():
    arg_types = {"discipline_id": is_str, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        discipline_id = args['discipline_id']
        discipline = System.delegate.get_discipline(discipline_id=discipline_id)    
        if not System.delegate.discipline_exists(discipline):
            raise StateError("discipline %s does not exists in System"
                                 % discipline.to_client())

    @staticmethod
    def action(args):
        discipline_id = args["discipline_id"]
        discipline_id = System.delegate.delete_discipline(discipline_id)
        return discipline_id

class DeleteSection():
    arg_types = {"s_id": is_int, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        s_id = args["s_id"]
        s_id = System.delegate.delete_section(s_id)
        return s_id
        
class UpdateSection():
    arg_types = {"section": is_section, "name": is_str_or_none,
                     "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        section = args['section']
        if not System.delegate.section_exists(section):
            raise StateError("section %s does not exists in System"
                                 % section.to_client())
        
    @staticmethod
    def action(args):
        section = args["section"]
        if not "name" in args:
           name=section.get("name")
        else:
           name=args["name"]

        section = System.delegate.update_section(section, name)
        return section

class DeleteExperiment():
    arg_types = {"exp_id": is_str, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        exp_id = args['exp_id']
        experiment = System.delegate.get_experiment(exp_id=exp_id)
        if not System.delegate.experiment_exists(experiment):
            raise StateError("experiment %s does not exists in System"
                                 % experiment.to_client())

    @staticmethod
    def action(args):
        exp_id = args["exp_id"]
        exp_id = System.delegate.delete_experiment(exp_id)
        return exp_id
        
class UpdateLab():
    arg_types = {"lab": is_lab, "lab_name": is_str,
                     "overview" : is_str, 
                     "session": is_session,
                     "sections" : are_sections,
                     "institute" : is_institute, 
                     "discipline" : is_discipline,
                     "hosting_info": are_hosting_info, 
                     "developers": are_developers,
                     "assets": are_assets, "experiments":are_experiments,
                     "integration_status" : is_integration_status}

    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        lab = args["lab"]
        if not System.delegate.lab_exists(lab):
            raise StateError("lab %s does not exists in System"
                                 % lab.to_client())

    @staticmethod
    def action(args):
        lab = args["lab"]
        lab_name = args["lab_name"]
        overview = args["overview"]
        institute = args["institute"]
        discipline = args["discipline"]
        integration_status = args["integration_status"]
        hosting_info = args["hosting_info"]
        developers = args["developers"]
        assets = args["assets"]
        experiments = args["experiments"]
        sections = args["sections"]
        lab = System.delegate.update_lab(lab, lab_name, overview, institute,
                                         discipline, sections, integration_status,
                                         hosting_info, developers, assets,
                                         experiments)
        return lab

class UpdateDiscipline():
    arg_types = {"discipline": is_discipline, "discipline_name": is_str_or_none,
                     "session": is_session, "assets": are_assets}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        discipline = args['discipline']
        if not System.delegate.discipline_exists(discipline):
            raise StateError("discipline %s does not exists in System"
                                 % discipline.to_client())
        
    @staticmethod
    def action(args):
        discipline = args["discipline"]
        discipline_name=args["discipline_name"]
        assets = args["assets"]
        dis = System.delegate.update_discipline(discipline, discipline_name, assets)
        return dis

class AddExperiment():
    arg_types = {"experiment": is_experiment, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        experiment = args["experiment"]
        if System.delegate.experiment_exists(experiment):
            raise StateError("experiment %s already exists in System"
                                 % experiment.to_client())

    @staticmethod
    def action(args):
        experiment = args["experiment"]
        experiment = System.delegate.add_experiment(experiment)
        return experiment

class AddDiscipline():
    arg_types = {"discipline": is_discipline, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        discipline = args["discipline"]
        if System.delegate.discipline_exists(discipline):
            raise StateError("discipline %s already exists in System"
                                 % discipline.to_client())

    @staticmethod
    def action(args):
        discipline = args["discipline"]
        discipline = System.delegate.add_discipline(discipline)
        return discipline

class UpdateExperiment():
    arg_types = {"exp_name": is_str_or_none,
                     "experiment": is_experiment,
                     "overview" : is_str,
                     "session": is_session,
                     "institute": is_institute,
                     "discipline": is_discipline,
                     "integration_status": is_integration_status,
                     "hosting_info": are_hosting_info,
                     "developers": are_developers,
                     "assets": are_assets, 
                     "sections": are_sections}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        experiment = args['experiment']
        if not System.delegate.experiment_exists(experiment):
            raise StateError("experiment %s does not exists in System"
                                 % experiment.to_client())
        
    @staticmethod
    def action(args):
        experiment = args["experiment"]
        exp_name=args["exp_name"]
        overview = args["overview"]
        institute = args["institute"]
        discipline = args["discipline"]
        integration_status = args["integration_status"]
        hosting_info = args["hosting_info"]
        developers = args["developers"]
        assets = args["assets"]
        sections = args["sections"]
        exp = System.delegate.update_experiment(experiment, exp_name, overview,
                                                institute, discipline, 
                                                integration_status, 
                                                hosting_info, developers,
                                                assets, sections)
        return exp

class AddInstitute():
    arg_types = {"institute": is_institute, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        institute = args["institute"]
        if System.delegate.institute_exists(institute):
            raise StateError("institute %s already exists in System"
                                 % institute.to_client())

    @staticmethod
    def action(args):
        institute = args["institute"]
        institute = System.delegate.add_institute(institute)
        return institute

class UpdateInstitute():
    arg_types = {"institute": is_institute, "institute_name": is_str_or_none, 
                       "session": is_session, "assets": are_assets}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        institute = args['institute']
        if not System.delegate.institute_exists(institute):
            raise StateError("institute %s does not exists in System"
                                 % institute.to_client())


    @staticmethod
    def action(args):
        institute_name = args["institute_name"]
        institute = args["institute"]       
        assets = args["assets"]
        institute = System.delegate.update_institute(institute, institute_name, assets)
        return institute

class DeleteInstitute():
    arg_types = {"institute_id": is_str, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        institute_id = args['institute_id']
        institute = System.delegate.get_institute(institute_id=institute_id)    
        if not System.delegate.institute_exists(institute):
            raise StateError("institute %s does not exists in System"
                                 % institute.to_client())

    @staticmethod
    def action(args):
        institute_id = args["institute_id"]
        institute_id = System.delegate.delete_institute(institute_id)
        return institute_id
        
class UpdateSection():
    arg_types = {"section": is_section, "name": is_str_or_none,
                     "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        section = args['section']
        if not System.delegate.section_exists(section):
            raise StateError("section %s does not exists in System"
                                 % section.to_client())
        
    @staticmethod
    def action(args):
        section = args["section"]
        if not "name" in args:
           name=section.get("name")
        else:
           name=args["name"]

        section = System.delegate.update_section(section, name)
        return section

class AddName():
    arg_types = {"name": is_name, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        name = args["name"]
        if System.delegate.name_exists(name):
            raise StateError("name %s already exists in System"
                                 % name.to_client())

    @staticmethod
    def action(args):
        name = args["name"]
        name = System.delegate.add_name(name)
        return name

class AddEmail():
    arg_types = {"email": is_email, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        email = args["email"]
        if System.delegate.email_exists(email):
            raise StateError("email %s already exists in System"
                                 % email.to_client())

    @staticmethod
    def action(args):
        email = args["email"]
        email = System.delegate.add_email(email)
        return email

class AddDeveloper():
    arg_types = {"developer": is_developer, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        developer = args["developer"]
        if System.delegate.developer_exists(developer):
            raise StateError("developer %s already exists in System"
                                 % developer.to_client())

    @staticmethod
    def action(args):
        developer = args["developer"]
        developer = System.delegate.add_developer(developer)
        return developer

class UpdateDeveloper():
    arg_types = {"developer": is_developer, "name": is_name,
                 "session": is_session}

    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        developer = args["developer"]
        if not System.delegate.developer_exists(developer):
            raise StateError("developer %s does not exists in System"
                                 % developer.to_client())

    @staticmethod
    def action(args):
        developer = args["developer"]
        if not "name" in args:
           name=developer.get("name")
        else:
           name=args["name"]

        developer = System.delegate.update_developer(developer, name)
        return developer

class DeleteName():
    arg_types = {"n_id": is_int, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        n_id = args["n_id"]
        n_id = System.delegate.delete_name(n_id)
        return n_id
        
class DeleteEmail():
    arg_types = {"email": is_email, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        email = args['email']
        if not System.delegate.email_exists(email):
            raise StateError("email %s does not exists in System"
                                 % email.to_client())

    @staticmethod
    def action(args):
        email = args["email"]
        email = System.delegate.delete_email(email)
        return email
        
class DeleteDeveloper():
    arg_types = {"email": is_email, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        email = args["email"]
        email = System.delegate.delete_developer(email)
        return email
        
class AddSectionsToExperiment():
    arg_types = {"sections": are_sections, "experiment": is_experiment, 
                     "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            current_app.logger.error("auth error raised, session = %s" % 
                                        session.to_client())
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        experiment = args["experiment"]
        if not System.delegate.experiment_exists(experiment):
            current_app.logger.error("exp with id = %d does not exist"
                                     " in System" % experiment)
            raise StateError("lab with id = %d does not exist in System"
                                 % labid)

    @staticmethod
    def action(args):
        experiment = args["experiment"]
        sections = args["sections"]
        try:
            exp = System.delegate.add_sections_to_experiment(experiment, sections) 
            return exp
        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

class AddSection():
    arg_types = {"section": is_section, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        section = args["section"]
        if System.delegate.section_exists(section):
            raise StateError("section %s already exists in System"
                                 % section.to_client())

    @staticmethod
    def action(args):
        section = args["section"]
        section = System.delegate.add_section(section)
        return section

class GetLab():
    arg_types = {"lab_id": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        lab_id = args['lab_id']
        lab = System.delegate.get_lab(lab_id=lab_id)
        if not System.delegate.lab_exists(lab):
            raise StateError("lab %s does not exists in System"
                                 % lab.to_client())

    @staticmethod
    def action(args):
        lab_id = args["lab_id"]
        lab = System.delegate.get_lab(lab_id=lab_id)
        return lab

class GetName():
    arg_types = {"name": is_name, "session": is_session}

    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        current_app.logger.debug("checking authorization")
        if not System.is_session_valid(session):
            current_app.logger.debug("authorization is failed")
            raise NotAuthorizedError("Not Authorized to perform this action")
        current_app.logger.debug("authorization check is done")

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        name = args["name"]
        name1 = System.delegate.get_name(name=name.get("name"))
        return name1

class GetEmail():
    arg_types = {"email": is_email, "session": is_session}

    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        current_app.logger.debug("checking authorization")
        if not System.is_session_valid(session):
            current_app.logger.debug("authorization is failed")
            raise NotAuthorizedError("Not Authorized to perform this action")
        current_app.logger.debug("authorization check is done")

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        email = args["email"]
        email1 = System.delegate.get_email(email=email.get("email"))
        return email1

class GetDeveloper():
    arg_types = {"email": is_email}

    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        email = args["email"]
        email = System.delegate.get_developer(email=email)
        return email

class GetExperiment():
    arg_types = {"exp_id": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass
    @staticmethod
    def state_check(args):
        exp_id = args['exp_id']
        exp = System.delegate.get_experiment(exp_id=exp_id)
        if not System.delegate.experiment_exists(exp):
            raise StateError("experiment %s does not exists in System"
                                 % experiment.to_client())

    @staticmethod
    def action(args):
        exp_id = args["exp_id"]
        exp = System.delegate.get_experiment(exp_id=exp_id)
        return exp

class GetInstitute():
    arg_types = {"institute_id": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass
        
    @staticmethod
    def action(args):
        institute_id = args["institute_id"]
        institute = System.delegate.get_institute(institute_id=institute_id)
        return institute

class GetDiscipline():
    arg_types = {"discipline_id": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        discipline_id = args["discipline_id"]
        discipline = System.delegate.get_discipline(discipline_id=discipline_id)
        return discipline

class GetInstituteByInstituteName():
    arg_types = {"institute_name": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        institute_name = args["institute_name"]
        institute = System.delegate.get_institute(institute_name=institute_name)
        return institute

class GetDisciplineByDisciplineName():
    arg_types = {"discipline_name": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        discipline_name = args["discipline_name"]
        discipline = System.delegate.get_discipline(discipline_name=discipline_name)
        return discipline

class GetIntegration_Statusby_IL():
    arg_types = {"integration_level": is_int}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        integration_level = args["integration_level"]
        integration_level = System.delegate.get_integration_status\
          (integration_level=integration_level)
        return integration_level
        
class AddHosting_Info():
    arg_types = {"hosting_info": is_hosting_info, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        hosting_info = args["hosting_info"]
        if System.delegate.hosting_info_exists(hosting_info):
            raise StateError("hosting_info %s already exists in System"
                                 % hosting_info.to_client())

    @staticmethod
    def action(args):
        hosting_info = args["hosting_info"]
        hosting_info = System.delegate.add_hosting_info(hosting_info)
        return hosting_info

class GetHosting_Info():
    arg_types = {"hosted_url": is_url}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass
        
    @staticmethod
    def action(args):
        hosted_url = args["hosted_url"]
        hosting_info = System.delegate.get_hosting_info(hosted_url=hosted_url)
        return hosting_info

class UpdateHosting_Info():
    arg_types = {"hosting_info": is_hosting_info, "hosting_status": is_str_or_none, "hosted_on": is_str_or_none, "session": is_session}                               
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        pass


    @staticmethod
    def action(args):
        hosting_status = args["hosting_status"]
        hosted_on = args["hosted_on"]
        hosting_info = args["hosting_info"]       
        hosting_info = System.delegate.update_hosting_info(hosting_info, hosting_status, hosted_on)
        return hosting_info

class DeleteHosting_Info():
    arg_types = {"hosted_url": is_url, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        hosted_url = args['hosted_url']
        hosting_info = System.delegate.get_hosting_info(hosted_url=hosted_url)
        if not System.delegate.hosting_info_exists(hosting_info):
            raise StateError("hosting_info %s does not exists in System"
                                 % hosting_info.to_client())

    @staticmethod
    def action(args):
        hosted_url = args["hosted_url"]
        hosted_url = System.delegate.delete_hosting_info(hosted_url)
        return hosted_url
        
class AddIntegration_Status():
    arg_types = {"integration_status": is_integration_status, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        integration_status = args["integration_status"]
        if System.delegate.integration_status_exists(integration_status):
            raise StateError("integration_status %s already exists in System"
                                 % integration_status.to_client())

    @staticmethod
    def action(args):
        integration_status = args["integration_status"]
        integration_status = System.delegate.add_integration_status(integration_status)
        return integration_status

class GetIntegration_Status():
    arg_types = {"integration_level": is_int}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        integration_level = args["integration_level"]
        integration_status = System.delegate.get_integration_status(integration_level=integration_level)
        return integration_status

class DeleteIntegration_Status():
    arg_types = {"integration_level": is_int, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        integration_level = args['integration_level']
        integration_status = System.delegate.get_integration_status(integration_level=integration_level)    
        if not System.delegate.integration_status_exists(integration_status):
            raise StateError("integration_status %s does not exists in System"
                                 % integration_status.to_client())

    @staticmethod
    def action(args):
        integration_level = args["integration_level"]
        integration_level = System.delegate.delete_integration_status(integration_level)
        return integration_level
        
class GetLabsByInstitute():
    arg_types = {"institute": is_institute}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        institute = args['institute']
        labs = System.delegate.get_labs(institute=institute)
        return labs

class GetLabsByLabName():
    arg_types = {"lab_name": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        lab_name = args['lab_name']
        labs = System.delegate.get_labs(lab_name=lab_name)
        return labs

class GetLabsByDiscipline():
    arg_types = {"discipline": is_discipline}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        discipline = args['discipline']
        labs = System.delegate.get_labs(discipline=discipline)
        return labs

class AddAssetType():
    arg_types = {"asset_type": is_asset_type, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        asset = args["asset"]
        if System.delegate.asset_type_exists(asset_type):
            raise StateError("asset %s already exists in System"
                                 % asset_type.to_client())

    @staticmethod
    def action(args):
        asset_type = args["asset_type"]
        asset_type = System.delegate.add_asset_type(asset_type)
        return asset_type

class AddAsset():
    arg_types = {"asset": is_asset, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        asset = args["asset"]
        if System.delegate.asset_exists(asset):
            raise StateError("asset %s already exists in System"
                                 % asset.to_client())

    @staticmethod
    def action(args):
        asset = args["asset"]
        asset = System.delegate.add_asset(asset)
        return asset

class GetAsset():
    arg_types = {"path": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        path = args["path"]
        asset = System.delegate.get_asset(path=path)
        return asset

class UpdateAsset():
    arg_types = {"asset_type": is_asset_type,
                     "asset": is_asset,
                     "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        asset = args['asset']
        if not System.delegate.asset_exists(asset):
            raise StateError("asset %s does not exists in System"
                                 % asset.to_client())
        
    @staticmethod
    def action(args):
        asset = args["asset"]
        if not "asset_type" in args:
           asset_type = asset.get("asset_type")
        else:
           asset_type=args["asset_type"]
        asst = System.delegate.update_asset(asset, asset_type)
        return asst

class DeleteAsset():
    arg_types = {"path": is_str, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        path = args['path']
        asset = System.delegate.get_asset(path=path)
        if not System.delegate.asset_exists(asset):
            raise StateError("asset %s does not exists in System"
                                 % asset.to_client())

    @staticmethod
    def action(args):
        path = args["path"]
        path = System.delegate.delete_asset(path)
        return path
        
class AddAssetsToLab():
    arg_types = {"assets": are_assets, "lab": is_lab, 
                     "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            current_app.logger.error("auth error raised, session = %s" % 
                                        session.to_client())
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        lab = args["lab"]
        if not System.delegate.lab_exists(lab):
            current_app.logger.error("lab %s does not exist"
                                     " in System" % lab)
            raise StateError("lab %s does not exist in System"
                                 % lab.to_client())

    @staticmethod
    def action(args):
        lab = args["lab"]
        assets = args["assets"]
        try:
            lab = System.delegate.add_assets_to_lab(lab, assets) 
            return lab
        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            raise err

class GetSection():
    arg_types = {"name": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        name = args["name"]
        section = System.delegate.get_section(name=name)
        return section

class UpdateName():
    arg_types = {"name": is_name, "n_name": is_str, "session": is_session}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        session = args['session']
        if not System.is_session_valid(session):
            raise NotAuthorizedError("Not Authorized to perform this action")

    @staticmethod
    def state_check(args):
        name = args['name']
        if not System.delegate.name_exists(name):
            raise StateError("name %s does not exists in System"
                                 % name.to_client())

    @staticmethod
    def action(args):
        name = args["name"]
        if not "n_name" in args:
           n_name=name.get("name")
        else:
           n_name=args["n_name"]

        name = System.delegate.update_name(name, n_name)
        return name

class GetLabsByAsset():
    arg_types = {"asset": is_asset}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        asset = args['asset']
        labs = System.delegate.get_labs(asset=asset)
        return labs

class GetAssetByAssetType():
    arg_types = {"asset_type": is_str}
    arity_and_type_checks_needed = True

    @staticmethod
    def auth_check(args):
        pass

    @staticmethod
    def state_check(args):
        pass

    @staticmethod
    def action(args):
        asset_type = args['asset_type']
        asset = System.delegate.get_asset(asset_type=asset_type)
        return asset

ops_table = {'add_lab' : AddLab,
             'update_lab': UpdateLab,
             'delete_lab': DeleteLab,
             'get_lab': GetLab,
             'get_labs_by_institute': GetLabsByInstitute,
             'get_labs_by_discipline' : GetLabsByDiscipline,
             'get_labs_by_lab_name': GetLabsByLabName, 
             'get_discipline': GetDiscipline,
             'add_experiment' : AddExperiment,
             'update_experiment' : UpdateExperiment,
             'delete_experiment' : DeleteExperiment,
             'add_institute' : AddInstitute,
             'update_institute': UpdateInstitute,
             'delete_institute': DeleteInstitute,
             'get_institute' : GetInstitute,
             'get_institute_by_institute_name' : GetInstituteByInstituteName,
             'get_discipline_by_discipline_name' : GetDisciplineByDisciplineName,
             'get_integration_status_by_IL': GetIntegration_Statusby_IL,
             'add_section' : AddSection,
             'update_section' : UpdateSection,
             'delete_section' : DeleteSection,
             'add_name' : AddName,
             'add_email' : AddEmail,
             'add_developer' : AddDeveloper,
             'update_developer': UpdateDeveloper,
             'delete_name': DeleteName,
             'delete_email': DeleteEmail,
             'delete_developer': DeleteDeveloper,
             'add_sections_to_experiment': AddSectionsToExperiment,
             'get_experiment' : GetExperiment,
             'add_discipline' : AddDiscipline,
             'update_discipline' : UpdateDiscipline,
             'delete_discipline' : DeleteDiscipline,
             'get_name': GetName,
             'get_email': GetEmail,
             'get_developer': GetDeveloper,
             'add_hosting_info' : AddHosting_Info,
             'get_hosting_info': GetHosting_Info,
             'update_hosting_info': UpdateHosting_Info,
             'delete_hosting_info': DeleteHosting_Info,
             'add_integration_status' : AddIntegration_Status,
             'get_integration_status': GetIntegration_Status,
             'delete_integration_status': DeleteIntegration_Status,
             'add_asset':AddAsset,
             'delete_asset': DeleteAsset,
             'get_asset': GetAsset,
             'update_asset': UpdateAsset,
             'add_assets_to_lab': AddAssetsToLab, 
             'get_section': GetSection, 
             'update_name': UpdateName,
             'get_labs_by_asset': GetLabsByAsset,
             'get_asset_by_asset_type': GetAssetByAssetType
             }
