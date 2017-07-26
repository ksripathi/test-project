
from runtime.rest.app import create_app
from runtime.config import flask_app_config as config
from runtime.utils.class_persistence_template import db
from runtime.system.system import System
from runtime.config.system_config import KEY

def populate():
    session_cls = System.delegate.entities['session']
    institute_cls = System.delegate.entities['institute']
    discipline_cls = System.delegate.entities['discipline']
    integration_status_cls = System.delegate.entities['integration_status']

    inst1 = institute_cls(institute_name="Amrita University", institute_id="amrita",
                              assets=[])
    inst1.save()
    inst2 = institute_cls(institute_name="College of Engineering, Pune",
                              institute_id="coep", assets=[])
    inst2.save()
    inst3 = institute_cls(institute_name="Dayalbagh Educational institute_cls",
                          institute_id="dei", assets=[])
    inst3.save()
    inst4 = institute_cls(institute_name="IIT Bombay", institute_id="iitb", assets=[])
    inst4.save()
    inst5 = institute_cls(institute_name="IIT Delhi", institute_id="iitd", assets=[])
    inst5.save()
    inst6 = institute_cls(institute_name="IIT Guwahati", institute_id="iitg", assets=[])
    inst6.save()
    inst7 = institute_cls(institute_name="IIIT Hyderabad", institute_id="iiith",
                              assets=[])
    inst7.save()
    inst8 = institute_cls(institute_name="IIT Kanpur", institute_id="iitk", assets=[])
    inst8.save()
    inst9 = institute_cls(institute_name="IIT Kharagpur", institute_id="iitkgp",
                              assets=[])
    inst9.save()
    inst10 = institute_cls(institute_name="IIT Madras", institute_id="iitm", assets=[])
    inst10.save()
    inst11 = institute_cls(institute_name="IIT Roorkee", institute_id="iitr", assets=[])
    inst11.save()
    inst12 = institute_cls(institute_name="NIT Surathkal", institute_id="nitk",
                               assets=[])
    inst12.save()

    dis1 = discipline_cls(discipline_name="Aerospace Engineering", discipline_id="aero",
                              assets=[])
    dis1.save()
    dis2 = discipline_cls(discipline_name="Biotechnology and Biomedical Engineering",
                          discipline_id="biotech", assets=[])
    dis2.save()
    dis3 = discipline_cls(discipline_name="Chemical Engineering",
                              discipline_id="chem-engg", assets=[])
    dis3.save()
    dis4 = discipline_cls(discipline_name="Chemical Sciences",
                              discipline_id="chem", assets=[])
    dis4.save()
    dis5 = discipline_cls(discipline_name="Civil Engineering",
                              discipline_id="civil", assets=[])
    dis5.save()
    dis6 = discipline_cls(discipline_name="Computer Science and Engineering",
                          discipline_id="cse", assets=[])
    dis6.save()
    dis7 = discipline_cls(discipline_name="Electrical Engineering",
                              discipline_id="ee", assets=[])
    dis7.save()
    dis8 = discipline_cls(discipline_name="Electronics and Communication",
                              discipline_id="ece", assets=[])
    dis8.save()
    dis9 = discipline_cls(discipline_name="Humanities", discipline_id="hmt", assets=[])
    dis9.save()
    dis10 = discipline_cls(discipline_name="Mechanical Engineering",
                               discipline_id="mech", assets=[])
    dis10.save()
    dis11 = discipline_cls(discipline_name="Physical Sciences",
                               discipline_id="phy-sc", assets=[])
    dis11.save()
    dis12 = discipline_cls(discipline_name="Textile Engineering",
                               discipline_id="tex-engg", assets=[])
    dis12.save()
    dis13 = discipline_cls(discipline_name="Design Engineering",
                               discipline_id="dsgn-engg", assets=[])
    dis13.save()
    dis14 = discipline_cls(discipline_name="Material Sciences",
                               discipline_id="mat-sc", assets=[])
    dis14.save()

    dis15 = discipline_cls(discipline_name="Metallurgical and Materials Engineering",
                               discipline_id="mm-engg", assets=[])
    dis15.save()

    dis16 = discipline_cls(discipline_name="Mining Engineering",
                               discipline_id="mine-engg", assets=[])
    dis16.save()

    dis17 = discipline_cls(discipline_name="Industrial and Systems Engineering",
                               discipline_id="is-engg", assets=[])
    dis17.save()

    integration_status0 = integration_status_cls(integration_level=0)
    integration_status0.save()

    integration_status1 = integration_status_cls(integration_level=1)
    integration_status1.save()

    integration_status2 = integration_status_cls(integration_level=2)
    integration_status2.save()

    integration_status3 = integration_status_cls(integration_level=3)
    integration_status3.save()

    integration_status4 = integration_status_cls(integration_level=4)
    integration_status4.save()

    integration_status5 = integration_status_cls(integration_level=5)
    integration_status5.save()

    integration_status6 = integration_status_cls(integration_level=6)
    integration_status6.save()

if __name__ == "__main__":
    db.create_all(app=create_app(config))
    populate()
