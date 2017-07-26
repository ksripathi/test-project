
# -*- coding: utf-8 -*-
from runtime.utils.type_utils import *
from runtime.utils.class_templates import *
from runtime.exceptions.custom_exceptions import *

Lab = ClassTemplate.mk_class("Lab")
Experiment = ClassTemplate.mk_class("Experiment")
Discipline =  ClassTemplate.mk_class("Discipline")
Session = ClassTemplate.mk_class("Session")
Section = ClassTemplate.mk_class("Section")
Name = ClassTemplate.mk_class("Name")
Email = ClassTemplate.mk_class("Email")
Developer = ClassTemplate.mk_class("Developer")
Institute = ClassTemplate.mk_class("Institute")
Asset = ClassTemplate.mk_class("Asset")
AssetType = ClassTemplate.mk_class("AssetType")
HostingInfo = ClassTemplate.mk_class("HostingInfo")
IntegrationStatus = ClassTemplate.mk_class("IntegrationStatus")

is_session = is_inst(Session)
check_session = check_pred(is_session)

is_lab = is_inst(Lab)
check_lab = check_pred(is_lab)

is_section = is_inst(Section)
check_section = check_pred(is_section)

def are_labs(labs):
    ret_val = True
    if is_list(labs):
        for lab in labs:
            if not is_lab(lab):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_experiment = is_inst(Experiment)
check_experiment = check_pred(is_experiment)

is_email = is_inst(Email)
check_email = check_pred(is_email)

def are_experiments(experiments):
    ret_val = True
    if is_list(experiments):
        for experiment in experiments:
            if not is_experiment(experiment):
                ret_val = False
    else:
        ret_val = False

    return ret_val

def are_sections(sections):
    ret_val = True
    if is_list(sections):
        for section in sections:
            if not is_section(section):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_developer = is_inst(Developer)
check_dev = check_pred(is_developer)

def are_developers(devs):
    ret_val = True
    if is_list(devs):
        for dev in devs:
            if not is_developer(dev):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_institute = is_inst(Institute)
check_institute = check_pred(is_institute)

def are_institutes(institutes):
    ret_val = True
    if is_list(institutes):
        for institute in institutes:
            if not is_institute(institute):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_name = is_inst(Name)
check_name = check_pred(is_name)

def are_names(names):
    ret_val = True
    if is_list(names):
        for name in names:
            if not is_name(name):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_email = is_inst(Email)
check_email = check_pred(is_email)

def are_emails(emails):
    ret_val = True
    if is_list(emails):
        for email in emails:
            if not is_email(email):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_asset_type = is_inst(AssetType)
check_asset_type = check_pred(is_asset_type)

def are_asset_types(asset_types):
    ret_val = True
    if is_list(asset_types):
        for asset_type in asset_types:
            if not is_asset_type(asset_type):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_discipline = is_inst(Discipline)
check_discipline = check_pred(is_discipline)

def are_disciplines(disciplies):
    ret_val = True
    if is_list(disciplines):
        for discipline in disciplies:
            if not is_discipline(discipline):
                ret_val = False
    else:
        ret_val = False

    return ret_val

is_hosting_info = is_inst(HostingInfo)
check_hosting_info = check_pred(is_hosting_info)

is_integration_status = is_inst(IntegrationStatus)
check_hosting_info = check_pred(is_integration_status)

is_asset = is_inst(Asset)
check_asset = check_pred(is_asset)

def are_assets(assets):
    ret_val = True
    if is_list(assets):
        for asset in assets:
            if not is_asset(asset):
                ret_val = False
    else:
        ret_val = False

    return ret_val

def are_hosting_info(hosting_info):
    ret_val = True
    if is_list(hosting_info):
        for hosting_info in hosting_info:
            if not is_hosting_info(hosting_info):
                ret_val = False
    else:
        ret_val = False

    return ret_val

Session.add_attributes(key=is_str)
Session.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("key") == other.get("key")

Lab.add_attributes(lab_name=is_str,
                    lab_id=is_str,
                    overview=is_str,
                    institute=is_institute,
                    discipline=is_discipline,
                    assets=are_assets,
                    integration_status=is_integration_status,
                    experiments=are_experiments,
                    developers=are_developers,
                    sections=are_sections,                    
                    hosting_info=are_hosting_info)

Lab.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("lab_name") == other.get("lab_name") and \
                  self.get("lab_id") == other.get("lab_id") and \
                  self.get("overview") == other.get("overview") and \
                  self.get("institute") == other.get("institute") and \
                  self.get("discipline") == other.get("discipline") and \
                  self.get("assets") == other.get("assets") and \
                  self.get("sections") == other.get("sections") and \
                  self.get("integration_status") == other.get("integration_status") and \
                  self.get("experiments") == other.get("experiments") and \
                  self.get("developers") == other.get("developers") and \
                  self.get("hosting_info") == other.get("hosting_info")

Experiment.add_attributes(exp_name=is_str, 
                          exp_id=is_str, overview=is_str, \
                          sections=are_sections, 
                          discipline=is_discipline,
                          institute=is_institute,
                          integration_status=is_integration_status,
                          assets=are_assets,
                          developers=are_developers,
                          hosting_info=are_hosting_info)

Experiment.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("exp_name") == other.get("exp_name") and \
                  self.get("exp_id") == other.get("exp_id") and \
                  self.get("overview") == other.get("overview") and \
                  self.get("sections") == other.get("sections") and \
                  self.get("discipline") == other.get("discipline") and \
                  self.get("institute") == other.get("institute") and \
                  self.get("integration_status") == other.\
                  get("integration_status") and \
                  self.get("assets") == other.get("assets") and \
                  self.get("developers") == other.get("developers") and \
                  self.get("hosting_info") == other.get("hosting_info")


Discipline.add_attributes(discipline_name=is_str, 
                          discipline_id=is_str,
                          assets=are_assets)
Discipline.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("discipline_name") == other.get("discipline_name") and \
                  self.get("discipline_id") == other.get("discipline_id") and \
                  self.get("assets") == other.get("assets")
                  

Section.add_attributes(name=is_str)

Section.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("name") == other.get("name")


Name.add_attributes(name=is_alphabetic_str)

Name.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("name") == other.get("name")

Email.add_attributes(email=is_email_str)

Email.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("email") == other.get("email")

Developer.add_attributes(name=is_name,
                         email=is_email)

Developer.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("name") == other.get("name") and\
                  self.get("email") == other.get("email") 
Institute.add_attributes(institute_name=is_str,
                    institute_id=is_str,
                    assets=are_assets)

Institute.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("institute_name") == other.get("institute_name") and \
                  self.get("institute_id") == other.get("institute_id") and \
                  self.get("assets") == other.get("assets")                 

AssetType.add_attributes(asset_type=is_str)

AssetType.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("asset_type") == other.get("asset_type")
Asset.add_attributes(path=is_str,
                    asset_type=is_asset_type)

Asset.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("path") == other.get("path") and \
                  self.get("asset_type") == other.get("asset_type") 
                               
HostingInfo.add_attributes(hosting_status=is_str,
                    hosted_url=is_url, hosted_on=is_str)

HostingInfo.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("hosting_status") ==\
                  other.get("hosting_status") and \
                  self.get("hosted_url") == other.get("hosted_url") and \
                  self.get("hosted_on") == other.get("hosted_on")

IntegrationStatus.add_attributes(integration_level=is_int)

IntegrationStatus.__eq__ = lambda self, other: \
                  isinstance(other, self.__class__) and \
                  self.get("integration_level") == other.\
                  get("integration_level")
