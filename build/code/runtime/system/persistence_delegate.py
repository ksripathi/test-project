
# -*- coding: utf-8 -*-
from runtime.persistence.entities import *
from runtime.exceptions.custom_exceptions import *
from flask import current_app, abort

class PersistenceDelegate():
   
    def __init__(self):
        self.entities = {'session': Session,
                         'lab': Lab,
                         'experiment' : Experiment,
                         'section' : Section,
                         'institute' : Institute,
                         'discipline' : Discipline,
                         'hosting_info': HostingInfo,
                         'asset' : Asset,
                         'asset_type': AssetType,
                         'integration_status': IntegrationStatus,
                         'name' : Name,
                         'email' : Email,
                         'developer' : Developer
                        }


    def get_object(self, cls, **kwargs):
        ret_val = None
        try:
            ret_val = cls.apply_filters(**kwargs)[0]
        except NotFoundError as e:
            ret_val = None
        
        return ret_val


    def get_lab(self, **kwargs):
        current_app.logger.debug("running get lab operation")
        current_app.logger.debug("completed get lab operation")

        return self.get_object(Lab, **kwargs)

    def get_section(self, **kwargs):
        current_app.logger.debug("running get section operation")
        current_app.logger.debug("completed get section operation")
        return self.get_object(Section, **kwargs)

    def get_experiment(self, **kwargs):
        current_app.logger.debug("running get experiment operation")
        current_app.logger.debug("completed get experiment operation")
        return self.get_object(Experiment, **kwargs)

    def get_institute(self, **kwargs):
        current_app.logger.debug("running get institute operation")
        current_app.logger.debug("completed get institute operation")
        return self.get_object(Institute, **kwargs)

    def get_discipline(self, **kwargs):
        current_app.logger.debug("running get discipline operation")
        current_app.logger.debug("completed get discipline operation")
        return self.get_object(Discipline, **kwargs)

    def get_hosting_info(self, **kwargs):
        current_app.logger.debug("running get hostinginfo operation")
        current_app.logger.debug("completed get hostinginfo operation")
        return self.get_object(HostingInfo, **kwargs)

    def get_asset(self, **kwargs):
        current_app.logger.debug("running get asset operation")
        current_app.logger.debug("completed get asset operation")
        return self.get_object(Asset, **kwargs)

    def get_integration_status(self, **kwargs):
        current_app.logger.debug("running get instegration status operation")
        current_app.logger.debug("completed get integration status operation")
        return self.get_object(IntegrationStatus, **kwargs)

    def discipline_exists(self, discipline):
        current_app.logger.debug("running check on the existence of"
                                 " discipline = %s" % 
                                 discipline.to_client())
        discipline_id = discipline.get("discipline_id")
        current_app.logger.debug("completed check on the existence of"
                                 " discipline with discipline_id = %s"
                                 % discipline_id)
        return discipline == self.get_discipline(discipline_id=discipline_id)

    def add_discipline(self, discipline):
        current_app.logger.debug("running add discipline to system operation"
                                 " discipline = %s" % discipline.to_client())
        discipline.save()
        current_app.logger.debug("completed add discipline to system operation"
                                 " discipline = %s" % discipline.to_client())
        return discipline

    def delete_discipline(self, discipline_id):
        record = self.get_discipline(discipline_id=discipline_id)
        if not record:
            abort(404, 'No Discipline  with discipline_id %s' % (discipline_id))
        else:
            try:
                current_app.logger.debug("running delete operation on"
                                         " discipline with discipline_id = %s"
                                         % discipline_id)
                record.delete()
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.debug("completed delete operation on"
                                         " discipline with discipline_id = %s"
                                         % discipline_id)
                print e
                abort(500, str(e))

        return discipline_id

    def update_discipline(self, discipline, discipline_name, assets):
        current_app.logger.debug("running update discipline operation")

        discipline.set(discipline_name=discipline_name, assets=assets)
        discipline.save()
       
        current_app.logger.debug("completed update discipline operation")
        return discipline


    def get_labs(self, **kwargs):
        current_app.logger.debug("")
        ret_val = None
        try:
            current_app.logger.debug("running operation get labs")
            ret_val = Lab.apply_filters(**kwargs)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            ret_val = None
        
        return ret_val

    def get_institutes(self, **kwargs):
        current_app.logger.debug("")
        ret_val = None
        try:
            current_app.logger.debug("running operation get institutes")
            ret_val = Institute.apply_filters(**kwargs)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            ret_val = None
        
        return ret_val

    def get_assets(self, **kwargs):
        current_app.logger.debug("")
        ret_val = None
        try:
            current_app.logger.debug("running operation get assets")
            ret_val = Asset.apply_filters(**kwargs)
        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            ret_val = None
        
        return ret_val


    def lab_exists(self, lab):
        current_app.logger.debug("running check on the existence of"
                                 " lab = %s" % lab)
        lab_id = lab.get("lab_id")
        current_app.logger.debug("completed check on the existence of"
                                 " lab with lab_id = %s" % lab_id)
        return lab == self.get_lab(lab_id=lab_id)
        
    def asset_type_exists(self, asset_type):
        current_app.logger.debug("running check on the existence of"
                                 " asset_type = %s" % asset_type)
        asset_type = asset_type.get("asset_type")
        current_app.logger.debug("completed check on the existence of"
                                 " asset_type with type as = %s" % asset_type)
        return asset_type == self.get_asset_type(asset_type=asset_type)
        
    def section_exists(self, section):
        current_app.logger.debug("running check on the existence of"
                                 " section = %s" % section) 
        name = section.get("name")
        current_app.logger.debug("completed check on the existence of"
                                 " section with name = %s" % name)
        return section == self.get_section(name=name)
        
    def experiment_exists(self, experiment):
        current_app.logger.debug("running check on the existence of"
                                 " experiment = %s" % experiment)
        exp_id = experiment.get("exp_id")
        current_app.logger.debug("completed check on the existence of"
                                 " experiment with exp_id = %s" % exp_id)
        return experiment == self.get_experiment(exp_id=exp_id)
        
    def institute_exists(self, institute):
        current_app.logger.debug("running check on the existence of"
                                 " institute = %s" % institute)
        institute_id = institute.get("institute_id")
        current_app.logger.debug("completed check on the existence of"
                                 " institute with institute_id = %s" % institute_id)
        return institute == self.get_institute(institute_id=institute_id)
        
    def name_exists(self, name):
        ret_val = False
        try:
            current_app.logger.debug("running check on the existence of name")
            if self.get_name(name=name.get("name")) is not None:
                ret_val = True
            current_app.logger.debug("completed check on the existence of name")
        except Exception as e:
            current_app.logger.error("Error in returning the name")
            pass
        return ret_val
        
    def email_exists(self, email):
        ret_val = False
        try:
            current_app.logger.debug("running check on the existence of email")
            if self.get_email(email=email.get("email")) is not None:
                ret_val = True
            current_app.logger.debug("completed check on the existence of email")
        except Exception as e:
            current_app.logger.error("Error in returning the email")
            pass

        return ret_val
        
    def developer_exists(self, developer):
        ret_val = False
        try:
            current_app.logger.debug("running check on the existence of"
                                     " developer")
            if self.get_developer(email=developer.get("email")) is not None:
                ret_val = True
            current_app.logger.debug("completed check on the existence of"
                                     " developer")
        except Exception as e:
            current_app.logger.error("Error in returning the developer")
            pass

        return ret_val
        
    def hosting_info_exists(self, hosting_info):
        current_app.logger.debug("running check on the existence of"
                                 " hosting_info = %s" % 
                                 hosting_info.to_client())
        hosted_url = hosting_info.get("hosted_url")
        current_app.logger.debug("completed check on the existence of" 
                                 " hosting_info with hosted_url = %s"
                                 % hosted_url)
        return hosting_info == self.get_hosting_info(hosted_url=hosted_url)
   
    def asset_exists(self, asset):
        current_app.logger.debug("running check on the existence of"
                                 " asset = %s" % asset.to_client())
        path = asset.get("path")
        current_app.logger.debug("completed check on the existence of"
                                 " asset with path = %s" % path)
        return asset == self.get_asset(path=path)
  
    def integration_status_exists(self, integration_status):
        current_app.logger.debug("running check on the existence of"
                                     " integration_status = %s"
                                    % integration_status.to_client())
        integration_level = integration_status.get("integration_level")

        current_app.logger.debug("completed check on the existence of"
                                 " integration_status"
                                 " with integration_level = %s" % 
                                 integration_level)
        return integration_status == self.get_integration_status(
                                     integration_level=integration_level)
        

    def add_lab(self, lab):
        current_app.logger.debug("running add lab to system operation"
                                 " lab = %s" % lab.to_client())
        lab.save()
        current_app.logger.debug("completed add lab to system operation"
                                 " lab = %s" % lab.to_client())
        return lab

    def add_experiment(self, experiment):
        current_app.logger.debug("running add experiment to system operation"
                                 " experiment = %s" % experiment.to_client())
        experiment.save()
        current_app.logger.debug("completed add experiment to system operation"
                                 " experiment = %s" % experiment.to_client())
        return experiment

    def add_section(self, section):
        current_app.logger.debug("running add section to system operation"
                                 " section = %s" % section.to_client())
        section.save()
        current_app.logger.debug("completed add section to system operation"
                                 " section = %s" % section.to_client())
        return section

    def add_institute(self, institute):
        current_app.logger.debug("running add institute to system operation"
                                 " institute = %s" % institute.to_client())
        institute.save()
        current_app.logger.debug("completed add institute to system operation"
                                 " institute = %s" % institute.to_client())
        return institute

    def add_hosting_info(self, hosting_info):
        current_app.logger.debug("running add hosting_info to system operation"
                                 " hosting_info = %s" % 
                                 hosting_info.to_client())
        hosting_info.save()
        current_app.logger.debug("completed add hosting_info"
                                 " to system operation"
                                 " hosting_info = %s" % 
                                 hosting_info.to_client())
        return hosting_info

    def add_asset_type(self, asset_type):
        current_app.logger.debug("running add asset type to system operation"
                                 " asset = %s" % asset_type.to_client())
        asset_type.save()
        current_app.logger.debug("completed add asset to system operation"
                                 " asset = %s" % asset_type.to_client())
        return asset_type

    def add_asset(self, asset):
        current_app.logger.debug("running add asset to system operation"
                                 " asset = %s" % asset.to_client())
        asset_type = asset.get("asset_type")
        current_app.logger.debug("running add asset to system"
                                 " with asset type = %s" % asset_type)

        if not self.asset_type_exists(asset_type):
            asset_type.save()
            current_app.logger.debug("completed add operation"
                                    " to system with asset" 
                                    " type = %s" % asset_type)

        asset.save()
        current_app.logger.debug("completed add asset to system operation"
                                 " asset = %s" % asset.to_client())
        return asset

    def add_integration_status(self, integration_status):
        current_app.logger.debug("running add integration_status to"
                                 " system operation"
                                 " integration_status = %s" % 
                                 integration_status.to_client())
        integration_status.save()
        current_app.logger.debug("completed add integration_status to"
                                 " system operation"
                                 " integration_status = %s" % 
                                 integration_status.to_client())
        return integration_status


    def delete_lab(self, lab_id):
        record = self.get_lab(lab_id=lab_id)
        if not record:
            abort(404, 'No Lab with lab_id %s' % (lab_id))
        else:
            try:
                current_app.logger.debug("running delete operation on"
                                         " lab with lab_id = %s"
                                         % lab_id)
                record.delete()
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.debug("completed delete operation on"
                                         " lab with lab_id = %s"
                                         % lab_id)
                print e
                abort(500, str(e))

        return lab_id

    def delete_section(self, s_id):
        record = Section.get_by_id(s_id)
        if not record:
            abort(404, 'No Section with id %s' % (e_id))
        else:
            try:
                current_app.logger.debug("running delete operation on section")
                record.delete()
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.debug("completed delete"
                                         " operation on section")
                print e
                abort(500, str(e))

        return s_id

    def delete_experiment(self, exp_id):
        record = self.get_experiment(exp_id=exp_id)
        if not record:
            abort(404, 'No Experiment found with exp_id %s' % (exp_id))
        else:
            try:
                current_app.logger.debug("running delete operation on"
                                         " experiment with exp_id = %s"
                                         % exp_id)
                record.delete()
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.debug("completed delete operation on"
                                         " experiment with exp_id = %s"
                                         % exp_id)
                print e
                abort(500, str(e))

        return exp_id

    def delete_institute(self, institute_id):
        record = self.get_institute(institute_id=institute_id)
        if not record:
            abort(404, 'No Institute with id %s' % (institute_id))
        else:
            try:
                current_app.logger.debug("running delete on institute"
                                         " with institute_id = %s" % 
                                         institute_id)
                record.delete()
                current_app.logger.debug("completed delete on institute"
                                         " with institute_id = %s" % 
                                         institute_id)
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(e))
                print e
                abort(500, str(e))

        return institute_id

    def delete_hosting_info(self, hosted_url):
        record = self.get_hosting_info(hosted_url=hosted_url)
        if not record:
            abort(404, 'No HostingInfo with id %s' % (hosted_url))
        else:
            try:
                current_app.logger.debug("running delete on hosting_info"
                                         " with hosted_url = %s" % hosted_url)
                record.delete()
                current_app.logger.debug("completed delete on hosting_info"
                                         " with hosted_url = %s" % hosted_url)
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(e))
                print e
                abort(500, str(e))

        return hosted_url

    def delete_asset(self, path):
        record = self.get_asset(path=path)
        if not record:
            abort(404, 'No Asset found with path %s' % (path))
        else:
            try:
                current_app.logger.debug("running delete on asset"
                                         " with path = %s" % path)
                record.delete()
                current_app.logger.debug("completed delete on asset"
                                         " with path = %s" % path)
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(e))
                print e
                abort(500, str(e))

        return path

    def delete_integration_status(self, integration_level):
        record = self.get_integration_status(integration_level=integration_level)
        if not record:
            abort(404, 'No IntegrationStatus with id %s' % (integration_level))
        else:
            try:
                current_app.logger.debug("running delete on integration_status"
                                         " with integration_level = %s" 
                                         % integration_level)
                record.delete()
                current_app.logger.debug("completed delete on integration_status"
                                         " with integration_level = %s" 
                                         % integration_level)
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(e))
                print e
                abort(500, str(e))

        return integration_level


    def update_lab(self, lab, lab_name, overview, institute, discipline,
                       sections, integration_status, hosting_info, developers,
                       assets, experiments):

        current_app.logger.debug("running update lab operation")

        lab.set(lab_name=lab_name, overview=overview, institute=institute, 
                    discipline=discipline, sections=sections, hosting_info=hosting_info,
                    integration_status=integration_status,
                    developers=developers, assets=assets,
                    experiments=experiments)
        lab.save()
 
        current_app.logger.debug("completed update lab operation") 

        return lab

    def update_section(self, section, name):
        current_app.logger.debug("running update section operation"
                                 " with section name = %s" % name)

        section.set(name=name)
        section.save()

        current_app.logger.debug("completed update section operation"
                                 " with section name = %s" % name)
        return section

    def update_experiment(self, experiment, exp_name, overview, institute, 
                          discipline, integration_status, hosting_info,
                          developers, assets, sections):
        current_app.logger.debug("running update experiment operation")

        experiment.set(exp_name=exp_name, overview=overview,
                           institute=institute, discipline=discipline,
                           integration_status=integration_status, 
                           hosting_info=hosting_info, 
                           developers=developers, assets=assets, 
                           sections=sections)
        experiment.save()

        current_app.logger.debug("completed update experiment operation")

        return experiment

    def update_institute(self, institute, institute_name, assets):

        current_app.logger.debug("running update institute operation")

        institute.set(institute_name=institute_name, assets=assets)
        institute.save()

        current_app.logger.debug("completed update institute operation")

        return institute

    def update_hosting_info(self, hosting_info, hosting_status, hosted_on):

        current_app.logger.debug("running update hosting_info operation")

        hosting_info.set(hosting_status=hosting_status, hosted_on=hosted_on)
        hosting_info.save()

        current_app.logger.debug("completed update hosting_info operation")

        return hosting_info

    def update_asset(self, asset, asset_type):
        
        current_app.logger.debug("running update asset operation")
        asset_type.save()
        asset.set(asset_type=asset_type)
        asset.save()

        current_app.logger.debug("completed update asset operation")
        return asset


    def get_lab_by_id(self, id):
        ret_val = None
        try:
            current_app.logger.debug("running operation get"
                                     " lab by ID = %s" % id)
            ret_val = Lab.get_by_id(id)
        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            ret_val = None
        
        return ret_val

    def get_experiment_by_id(self, id):
        ret_val = None
        try:
            current_app.logger.debug("running operation get"
                                     " experiment by ID = %s" % id)
            ret_val = Experiment.get_by_id(id)
        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            ret_val = None
        
        return ret_val

    def get_institute_by_id(self, id):
        ret_val = None
        try:
            current_app.logger.debug("running operation get"
                                     " institute by ID = %s" % id)
            ret_val = Institute.get_by_id(id)
        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            ret_val = None
        
        return ret_val

    def get_discipline_by_id(self, id):
        ret_val = None
        try:
            current_app.logger.debug("running operation get"
                                     " discipline by ID = %s" % id)
            ret_val = Discipline.get_by_id(id)
        except Exception as err:
            current_app.logger.error("Exception = %s" % str(err))
            ret_val = None
        
        return ret_val



    def add_experiments_to_lab(self, labid, experiments):
        lab = self.get_lab_by_id(labid)
        experiment_list = []
        for experiment in experiments:

            current_app.logger.debug("running add experiments to a lab"
                                     " operation with labid = %s" % labid)

            if self.experiment_exists(experiment):
                experiment = self.get_experiment(exp_id=experiment.
                                                     get('exp_id'),
                                                 exp_name=experiment.
                                                     get('exp_name'))
            else:
                experiment.save()

            experiment_list.append(experiment)

        lab.set(experiments=experiment_list)

        current_app.logger.debug("completed add experiments to a lab operation")        
        return lab

    def add_assets_to_lab(self, lab, assets):
        asset_list = []
        for asset in assets:

            current_app.logger.debug("running add assets to a" 
                                     " lab = %s" % lab.to_client())
            if self.asset_exists(asset):
                asset = self.get_asset(path=asset.get('path'),
                                           asset_type=asset.
                                           get('asset_type'))
            else:
                asset.save()

            asset_list.append(asset)

        lab.set(assets=asset_list)

        current_app.logger.debug("completed add assets to a lab = %s"
                                 % lab.to_client())
        return lab

    def add_sections_to_experiment(self, experiment, sections):
        section_list = []
        for section in sections:
            current_app.logger.debug("running add sections to an"
                                   " experiment = %s" % experiment.to_client())
            if self.section_exists(section):
                section = self.get_section(name=section.get('name'))
            else:
                section.save()

            section_list.append(section)

        experiment.set(sections=section_list)

        current_app.logger.debug("completed add sections to an"
                                 " experiment = %s" % experiment.to_client())
        return experiment

    def add_labs_to_institute(self, instituteid, labs):
        institute = self.get_institute_by_id(instituteid)
        lab_list = []
        for lab in labs:
            current_app.logger.debug("running add labs to an institute with"
                                     " instituteid = %s" % instituteid)
            if self.lab_exists(lab):
                lab = self.get_lab(lab_id=lab.get('lab_id'),
                                                 lab_name=lab.get('lab_name'))
            else:
                lab.save()

            lab_list.append(lab)

        institute.set(labs=lab_list)

        current_app.logger.debug("completed add labs to an institute with"
                                 " instituteid = %s" % instituteid)
        return institute


    def add_name(self, name):
        current_app.logger.debug("running add name to system operation"
                                 " name = %s" % name.to_client())
        name.save()
        current_app.logger.debug("completed add name to system operation"
                                 " name = %s" % name.to_client())
        return name

    def add_email(self, email):
        current_app.logger.debug("running add email to system operation"
                                 " email = %s" % email.to_client())
        email.save()
        current_app.logger.debug("completed add email to system operation"
                                 " email = %s" % email.to_client())
        return email

    def add_developer(self, developer):
        current_app.logger.debug("running add developer to system"
                                 " developer = %s" % developer.to_client())
        name = developer.get("name")
        current_app.logger.debug("running add developer to system"
                                 " with name = %s" % name)
        email = developer.get("email")
        current_app.logger.debug("running add developer to system"
                                 " with email = %s" % email)

        if not self.name_exists(name.get("name")):
            name.save()
            current_app.logger.debug("completed add operation"
                                    " to system with developer" 
                                    " name = %s" % name)
        if not self.email_exists(email.get("email")):
            email.save()
            current_app.logger.debug("completed add operation"
                                    " to system with developer"
                                    " email = %s" % email)
        developer.save()

        current_app.logger.debug("completed add developer"
                                 " operation = %s" % developer.to_client())
        return developer


    def update_developer(self, dev, dev_name):

        current_app.logger.debug("running update developer operation")
        dev_name.save()
        dev.set(name=dev_name)
        dev.save()

        current_app.logger.debug("completed update developer operation")

        return dev


    def delete_name(self, n_id):
        current_app.logger.debug("running delete on developer name")
        record = Name.get_by_id(n_id)
        if not record:
            abort(404, 'No Name with id %s' % (n_id))
        else:
            try:
                record.delete()
                current_app.logger.debug("completed delete on developer"
                                         " name")
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(e))
                print e
                abort(500, str(e))

        return n_id

    def delete_email(self, email_id):
        record = self.get_email(email=email_id.get("email"))
        current_app.logger.debug("running delete on developer"
                                 " email with email_id = %s" % email_id)
        if not record:
            abort(404, 'No Email with id %s' % (email_id))
        else:
            try:               
                record.delete()
                current_app.logger.debug("completed delete on developer"
                                        " email with email_id = %s" % email_id)
                #db.session.delete(record)
                #db.session.commit()
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(etest_delete_developer))
                print e
                abort(500, str(e))

        return email_id

    def delete_developer(self, email_id):
        record = self.get_developer(email=email_id)
        if not record:
            current_app.logger.debug("running delete on developer"
                                     " with email_id = %s" % email_id)
            abort(404, 'No Developer with id %s' % (email_id))
        else:
            try:
                record.delete()
                current_app.logger.debug("completed delete on developer"
                                         " with email_id = %s" % email_id)
                self.delete_email(email_id)
               
            except Exception, e:
                current_app.logger.error("Exception = %s" % str(e))
                print e
                abort(500, str(e))

        return email_id


    def get_name(self, **kwargs):
        current_app.logger.debug("running get developer's name operation")
        current_app.logger.debug("completed get developer's name operation")
        return self.get_object(Name, **kwargs)

    def get_email(self, **kwargs):
        current_app.logger.debug("running get developer's email operation")
        current_app.logger.debug("completed get developer's email operation")
        return self.get_object(Email, **kwargs)

    def get_developer(self, **kwargs):
        current_app.logger.debug("running get developer operation")
        current_app.logger.debug("completed get developer operation")
        return self.get_object(Developer, **kwargs)

    def get_asset_type(self, **kwargs):
        current_app.logger.debug("running get asset_type operation")
        current_app.logger.debug("completed get asset_type operation")

        return self.get_object(AssetType, **kwargs)

    def update_name(self, name, n_name):
        name.set(name=n_name)
        name.save()
        return name
