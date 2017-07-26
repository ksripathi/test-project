
# -*- coding: utf-8 -*-
import os
import requests
import json
from flask import session, render_template, Blueprint, request, \
     jsonify, abort, current_app, redirect, url_for
from flask import Flask
from runtime.utils.type_utils import jsonify_list
from runtime.exceptions.custom_exceptions import *
from runtime.system.system_interface import SystemInterface
import yaml

api = Blueprint('APIs', __name__)

@api.route('/labs', methods=['GET'])
def get_lab():
    if request.method == 'GET':
        if 'lab_id' in request.args:
            lab_id  = request.args['lab_id']
            try:
                current_app.logger.debug("running operation get_lab")
                lab = SystemInterface.get_lab(lab_id)
                current_app.logger.debug("completed operation get_lab")
                return jsonify(lab)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)
                
        elif 'lab_name' in request.args:
            lab_name  = request.args['lab_name']
            try:
                current_app.logger.debug("running operation get_labs_by_lab_name")
                labs = SystemInterface.get_labs_by_lab_name(lab_name)
                return jsonify(labs)
                
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

        elif 'institute_name' in request.args:
            institute_name  = request.args['institute_name']
            try:
                current_app.logger.debug("running operation get_labs_by_institute")
                labs = SystemInterface.get_labs_by_institute(institute_name)
                current_app.logger.debug("completed operation get_labs_by_institute")
                return jsonify_list(labs)
                
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

        elif 'discipline_name' in request.args:
            discipline_name  = request.args['discipline_name']
            try:
                current_app.logger.debug("running operation get_labs_by_discipline")
                labs = SystemInterface.get_labs_by_discipline(discipline_name)
                current_app.logger.debug("completed operation get_labs_by_discipline")
                return jsonify_list(labs)
                
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

        elif 'asset_type' in request.args:
            asset_type  = request.args['asset_type']
            try:
                current_app.logger.debug("running operation get_labs_by_asset")
                labs = SystemInterface.get_labs_by_asset(asset_type)
                current_app.logger.debug("completed operation get_labs_by_asset")
                return jsonify_list(labs)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

        elif 'keyword_lab_name' in request.args:
            keyword  = request.args['keyword_lab_name']
            try:
                current_app.logger.debug("running operation get_labs"
                                         " _by_keyword_lab_name")
                labs = SystemInterface.get_labs_by_keyword_lab_name(keyword)
                current_app.logger.debug("completed operation get_labs_by_"
                                         " keyword_lab_name")
                return jsonify_list(labs)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

        else:
            try:
                current_app.logger.debug("running operation get_labs")                
                labs = SystemInterface.get_labs()
                current_app.logger.debug("completed operation get_labs")
                return jsonify_list(labs)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)
         

@api.route('/labs', methods=['POST'])
def add_lab():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("running operation add_labs")
            lab = SystemInterface.add_lab(data_dict)
            return_data = {}
            return_data["data"] = lab
            return_data["status"] = "success"
            return_data["status_code"] = 200
            current_app.logger.debug("completed operation add_labs")
            return jsonify(return_data)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/labs', methods=['PUT'])
def update():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'lab_id' in request.args:
            data_dict['lab']['id']  = request.args['lab_id']
        else:
            abort(500, "Please provide the 'lab_id' to update the lab")
        
        try:
            current_app.logger.debug("execute update_lab")
            lab = SystemInterface.update_lab(data_dict)
            current_app.logger.debug("executed update_lab")
            return jsonify(lab)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/labs', methods=['DELETE'])
def delete_lab():
    if request.method == 'DELETE':
        if 'lab_id' in request.args and 'key' in request.args:
            lab_id  = request.args['lab_id']
            key = request.args['key']
            try:
                current_app.logger.debug("execute delete_lab")
                lab = SystemInterface.delete_lab(lab_id, key)
                current_app.logger.debug("executed delete_lab")
                return jsonify({"status":"sucess"})

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                       "msg": err_str}
                abort(401, msg)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)
            
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                           "msg": err_str}
                abort(500, msg)
            
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
                abort(404, msg)
            
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            
@api.route('/experiments', methods=['GET'])
def get_experiment():
    if request.method == 'GET':
        if 'exp_id' in request.args:
            exp_id  = request.args['exp_id']
            try:
                current_app.logger.debug("execute get_exp_by_expid")
                exp = SystemInterface.get_experiment(exp_id)
                current_app.logger.debug("executed get_exp_by_expid")
                return jsonify(exp)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)
        else:
            try:
                current_app.logger.debug("execute get_experiments")
                experiments = SystemInterface.get_experiments()
                current_app.logger.debug("executed get_experiments")
                return jsonify_list(experiments)

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                           "status code": 401,
                           "msg": err_str}
                abort(401, msg)
                
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                           "msg": err_str }
                abort(500, msg)
                
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
                
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
                abort(404, msg)
                
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
                
@api.route('/experiments', methods=['POST'])
def get_add_experiment():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_experiment")
            exp = SystemInterface.add_experiment(data_dict)
            current_app.logger.debug("executed add_experiment")
            return jsonify(exp.to_client())

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/disciplines', methods=['GET'])
def get_discipline():
    if request.method == 'GET':
        if 'discipline_id' in request.args:
            discipline_id  = request.args['discipline_id']
            try:
                current_app.logger.debug("running operation get_discipline")
                discipline = SystemInterface.get_discipline(discipline_id)
                current_app.logger.debug("completed operation get_discipline")
                return jsonify(discipline)
            
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                        "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)
                
        
        else:

            try:
                current_app.logger.debug("running operation get_disciplines")
                disciplines = SystemInterface.get_disciplines()               
                current_app.logger.debug("completed operation get_disciplines")
                return jsonify_list(disciplines)
            
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)
@api.route('/disciplines', methods=['POST'])
def add_discipline():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("running operation add_discipline")
            dis = SystemInterface.add_discipline(data_dict)           
            current_app.logger.debug("completed operation add_discipline")
            return jsonify(dis)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/experiments', methods=['PUT'])
def update_experiment():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'exp_id' in request.args:
            data_dict['experiment']['id']  = request.args['exp_id']
        else:
            abort(500, "Please provide the 'exp_id' to update the exp")
        
        try:
            current_app.logger.debug("execute update_experiment")
            exp = SystemInterface.update_experiment(data_dict)
            current_app.logger.debug("execute update_experiment")
            return jsonify(exp)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/experiments', methods=['DELETE'])
def delete_experiment():
    if request.method == 'DELETE':
        if 'exp_id' in request.args and 'key' in request.args:
            exp_id  = request.args['exp_id']
            key = request.args['key']
            try:
                current_app.logger.debug("running operation delete_experiment")
                exp_id = SystemInterface.delete_experiment(exp_id, key)
                current_app.logger.debug("completed operation delete_experiment")
                return jsonify({"status":"sucess"})
            
            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                        "msg": err_str}
                abort(401, msg)
            
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)
            
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                       "msg": err_str}
                abort(404, msg)
            
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            
@api.route('/sections/<id>', methods=['GET', 'PUT', 'DELETE'])
def update_and_delete_section(id):
    if request.method == 'GET':
        try:
            current_app.logger.debug("running operation get_section_by_id")
            section = SystemInterface.get_section_by_id(id)
            current_app.logger.debug("completed operation get_section_by_id")
            return jsonify(section)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
    
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
            data_dict['s_id']=id
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("running operation update_section")
            section = SystemInterface.update_section(data_dict)
            current_app.logger.debug("completed operation update_section")
            return jsonify(section)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
        
    if request.method == 'DELETE':

        try:
            current_app.logger.debug("running operation delete_section")
            section = SystemInterface.delete_section(id)
            current_app.logger.debug("completed operation delete_section")
            return jsonify({"status":"sucess"})

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
@api.route('/sections', methods=['GET'])
def get_sections():
    if request.method == 'GET':
        try:
            current_app.logger.debug("execute get_sections")
            sections = SystemInterface.get_sections()
            current_app.logger.debug("executed get_sections")
            return jsonify_list(sections)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/sections', methods=['POST'])
def add_section():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_section")
            section = SystemInterface.add_section(data_dict)
            current_app.logger.debug("executed add_section")
            return jsonify(section)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/institutes', methods=['PUT'])
def update_institute():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'institute_id' in request.args:
            data_dict['institute_id']  = request.args['institute_id']
        else:
            abort(500, "Please provide the 'institute_id' to update the institute")
        
        try:
            current_app.logger.debug("running operation update_institute")
            institute = SystemInterface.update_institute(data_dict)
            current_app.logger.debug("completed operation update_institute")
            return jsonify(institute.to_client())

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",  
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/institutes', methods=['DELETE'])
def delete_institute():
    if request.method == 'DELETE':
        if 'institute_id' in request.args and 'key' in request.args:
            institute_id  = request.args['institute_id']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_institute")
                institute = SystemInterface.delete_institute(institute_id, key)
                current_app.logger.debug("completed operation delete_institute")
                return jsonify({"status":"sucess"})

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                        "msg": err_str}
                abort(401, msg)
            
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)
            
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                       "msg": err_str}
                abort(404, msg)
            
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
@api.route('/disciplines', methods=['PUT'])
def update_discipline():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'discipline_id' in request.args:
            data_dict['discipline_id']  = request.args['discipline_id']
        else:
            abort(500, "Please provide the 'discipline_id' to update the institute")
        
        try:
            current_app.logger.debug("running operation update_discipline")
            discipline = SystemInterface.update_discipline(data_dict)
            current_app.logger.debug("completed operation update_discipline")
            return jsonify(discipline.to_client())
        
        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/disciplines', methods=['DELETE'])
def delete_discipline():
    if request.method == 'DELETE':
        if 'discipline_id' in request.args and 'key' in request.args:
            discipline_id  = request.args['discipline_id']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_discipline")
                discipline = SystemInterface.delete_discipline(discipline_id, key)
                current_app.logger.debug("completed operation delete_discipline")
                return jsonify({"status":"sucess"})
            
            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                        "msg": err_str}
                abort(401, msg)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)
            
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)            
            
            
@api.route('/institutes', methods=['GET'])
def get_institute():
    if request.method == 'GET':
       if 'institute_id' in request.args:
           institute_id  = request.args['institute_id']
           try:
               current_app.logger.debug("running operation get_institute")
               institute = SystemInterface.get_institute(institute_id)
               current_app.logger.debug("completed operation get_institute")
               return jsonify(institute)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)
               

       else:
           try:
               current_app.logger.debug("running operation get_institutes")
               institutes = SystemInterface.get_institutes()
               current_app.logger.debug("completed operation get_institutes")
               return jsonify_list(institutes)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)
            
@api.route('/institutes', methods=['POST'])
def add_institute():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("running operation add_institute")
            institute = SystemInterface.add_institute(data_dict)
            current_app.logger.debug("completed operation add_institute")
            return jsonify(institute)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/hosting_info', methods=['GET'])
def get_hosting_info():
    if request.method == 'GET':
       if 'hosted_url' in request.args:
           hosted_url  = request.args['hosted_url']
           try:
               current_app.logger.debug("execute get_hosting_info_by_hosted_url")
               hosting_info = SystemInterface.get_hosting_info_by_hosted_url(hosted_url)
               current_app.logger.debug("executed get_hosting_info_by_hosted_url")
               return jsonify(hosting_info)

           except NotAuthorizedError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
               abort(401, msg)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)
       else:
           try:
               current_app.logger.debug("execute get_hosting_info")
               hosting_info = SystemInterface.get_hosting_info()
               current_app.logger.debug("executed get_hosting_info")
               return jsonify_list(hosting_info)

           except NotAuthorizedError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
               abort(401, msg)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)
@api.route('/hosting_info', methods=['POST'])
def add_hosting_info():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_hosting_info")
            hosting_info = SystemInterface.add_hosting_info(data_dict)
            current_app.logger.debug("executed add_hosting_info")
            return jsonify(hosting_info)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/hosting_info', methods=['PUT'])
def update_hosting_info():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'hosted_url' in request.args:
            data_dict['hosted_url']  = request.args['hosted_url']
        else:
            abort(500, "Please provide the 'hosted_url' to update the hosting_info")
        
        try:
            current_app.logger.debug("running operation update_hosting_info")
            hosting_info = SystemInterface.update_hosting_info(data_dict)
            current_app.logger.debug("completed operation update_hosting_info")
            return jsonify(hosting_info)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/hosting_info', methods=['DELETE'])
def delete_hosting_info():
    if request.method == 'DELETE':
        if 'hosted_url' in request.args and 'key' in request.args:
            hosted_url  = request.args['hosted_url']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_hosting_info")
                hosting_info = SystemInterface.delete_hosting_info(hosted_url, key)
                current_app.logger.debug("completed operation delete_hosting_info")
                return jsonify({"status":"sucess"})

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                        "msg": err_str}
                abort(401, msg)
            
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)
            
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                       "msg": err_str}
                abort(404, msg)
            
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            
@api.route('/integration_status', methods=['GET'])
def get_integration_status():
    if request.method == 'GET':
       if 'integration_level' in request.args:
           integration_level  = request.args['integration_level']
           try:
               current_app.logger.debug("execute get_integration_status_by_IL")
               integration_status = SystemInterface.get_integration_status_by_IL\
                 (integration_level)
               current_app.logger.debug("executed get_integration_status_by_IL")
               return jsonify(integration_status.to_client())

           except NotAuthorizedError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
               abort(401, msg)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                        "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

       else:
           try:
               current_app.logger.debug("execute get_integration_status")
               integration_status = SystemInterface.get_integration_status()
               current_app.logger.debug("executed get_integration_status")
               return jsonify_list(integration_status)

           except NotAuthorizedError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
               abort(401, msg)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)
@api.route('/integration_status', methods=['POST'])
def add_integration_status():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_integration_status")
            integration_status = SystemInterface.add_integration_status(data_dict)
            current_app.logger.debug("executed add_integration_status")
            return jsonify(integration_status)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/integration_status', methods=['DELETE'])
def delete_integration_status():
    if request.method == 'DELETE':
        if 'integration_level' in request.args and 'key' in request.args:
            integration_level  = request.args['integration_level']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_integration_status")
                integration_status = SystemInterface.delete_integration_status(integration_level, key)
                current_app.logger.debug("completed operation delete_integration_status")
                return jsonify({"status":"sucess"})

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                        "msg": err_str}
                abort(401, msg)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)
            
            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                       "msg": err_str}
                abort(404, msg)
            
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            
@api.route('/assets', methods=['GET'])
def get_asset():
    if request.method == 'GET':
       if 'path' in request.args:
           path  = request.args['path']
           try:
               current_app.logger.debug("running operation get_asset_by_path")
               asset = SystemInterface.get_asset_by_path(path)
               current_app.logger.debug("completed operation get_asset_by_path")
               return jsonify(asset)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str }
               abort(500, msg)
           
           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
           
           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
               abort(404, msg)
           
           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
       else:
           try:
               current_app.logger.debug("running operation get_assets")
               assets = SystemInterface.get_assets()
               current_app.logger.debug("completed operation get_assets")
               return jsonify_list(assets)
        
           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str }
               abort(500, msg)
           
           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
           
           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
               abort(404, msg)
           
           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
@api.route('/assets', methods=['POST'])
def add_asset():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("running operation add_asset")
            asset = SystemInterface.add_asset(data_dict)
            current_app.logger.debug("completed operation add_asset")
            return jsonify(asset)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/assets', methods=['PUT'])
def update_asset():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'path' in request.args:
            data_dict['path']  = request.args['path']
        else:
            abort(500, "Please provide the 'path' to update the asset")
        
        try:
            current_app.logger.debug("running operation update_asset")
            asset = SystemInterface.update_asset(data_dict)
            current_app.logger.debug("completed operation update_asset")
            return jsonify(asset)
        
        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/assets', methods=['DELETE'])
def delete_asset():
    if request.method == 'DELETE':
        if 'path' in request.args and 'key' in request.args:
            path  = request.args['path']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_asset")
                asset = SystemInterface.delete_asset(path, key)
                current_app.logger.debug("completed operation delete_asset")
                return jsonify({"status":"sucess"})
            
            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                        "msg": err_str}
                abort(401, msg)
            
            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
                abort(404, msg)
            
            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "msg": err_str}
                abort(500, msg)
            
            
@api.route('/emails', methods=['DELETE'])
def delete_email():
    if request.method == 'DELETE':
        if 'email' in request.args and 'key' in request.args:
            email  = request.args['email']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_email")
                email = SystemInterface.delete_email(email, key)
                current_app.logger.debug("completed operation delete_email")
                return jsonify({"status":"sucess"})

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                       "msg": err_str}
                abort(401, msg)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

@api.route('/emails', methods=['GET'])
def get_email():
    if request.method == 'GET':
       if 'email' in request.args:
           email  = request.args['email']
           try:
               current_app.logger.debug("execute get_email")
               email = SystemInterface.get_email(email)
               current_app.logger.debug("executed get_email")
               return jsonify(email)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

       else:
           try:
               current_app.logger.debug("execute get_emails")
               emails = SystemInterface.get_emails()
               current_app.logger.debug("executed get_emails")
               return jsonify_list(emails)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)

           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
               abort(404, msg)

           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                       "msg": err_str}
               abort(500, msg)
@api.route('/emails', methods=['POST'])
def add_email():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_email")
            email = SystemInterface.add_email(data_dict)
            current_app.logger.debug("executed add_email")
            return jsonify(email)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/names', methods=['GET'])
def get_names():
    if request.method == 'GET':
        try:
            current_app.logger.debug("execute get_names")
            names = SystemInterface.get_names()
            current_app.logger.debug("executed get_names")
            return jsonify_list(names)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/names', methods=['POST'])
def add_name():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_name")
            name = SystemInterface.add_name(data_dict)
            current_app.logger.debug("executed add_name")
            return jsonify(name)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            

@api.route('/developers', methods=['GET'])
def get_developer():
    if request.method == 'GET':
       if 'email' in request.args:
           email  = request.args['email']
           try:
               current_app.logger.debug("execute get_developer")
               developer = SystemInterface.get_developer(email)
               current_app.logger.debug("executed get_developer")
               return jsonify(developer)
           
           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str }
               abort(500, msg)

           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
           
           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
               abort(404, msg)
           
           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
           
       else:
           try:
               current_app.logger.debug("execute get_developers")
               developers = SystemInterface.get_developers()
               current_app.logger.debug("executed get_developers")
               return jsonify_list(developers)

           except TypeError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str }
               abort(500, msg)
           
           except StateError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
           
           except NotFoundError as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "status code": 404,
                        "msg": err_str}
               abort(404, msg)
           
           except Exception as e:
               current_app.logger.error("Exception = %s" % str(e))
               err_str = str(e)
               msg = {"status": "failure",
                        "msg": err_str}
               abort(500, msg)
@api.route('/developers', methods=['POST'])
def add_developer():
    if request.method == 'POST':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("execute add_developer")
            developer = SystemInterface.add_developer(data_dict)
            current_app.logger.debug("executed add_developer")
            return jsonify(developer.to_client())

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
            
@api.route('/developers', methods=['DELETE'])
def delete_developer():
    if request.method == 'DELETE':
        if 'email' in request.args and 'key' in request.args:
            email  = request.args['email']
            key = request.args['key']

            try:
                current_app.logger.debug("running operation delete_developer")
                developer = SystemInterface.delete_developer(email, key)
                current_app.logger.debug("completed operation delete_developer")
                return jsonify({"status":"sucess"})

            except NotAuthorizedError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                        "status code": 401,
                       "msg": err_str}
                abort(401, msg)

            except TypeError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str }
                abort(500, msg)

            except StateError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

            except NotFoundError as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
                abort(404, msg)

            except Exception as e:
                current_app.logger.error("Exception = %s" % str(e))
                err_str = str(e)
                msg = {"status": "failure",
                       "msg": err_str}
                abort(500, msg)

@api.route('/developers', methods=['PUT'])
def update_developer():
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
        else:
            abort(500, "the request does not contain data in json")

        if 'email' in request.args:
            data_dict['email']  = request.args['email']
        else:
            abort(500, "Please provide the 'email' to update the developer")
        
        try:
            current_app.logger.debug("running operation update_developer")
            developer = SystemInterface.update_developer(data_dict)
            current_app.logger.debug("completed operation update_developer")
            return jsonify(developer.to_client())

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

@api.route('/names/<id>', methods=['GET', 'PUT', 'DELETE'])
def update_and_delete_name(id):
    if request.method == 'GET':
        try:
            current_app.logger.debug("running operation get_name_by_id")
            name = SystemInterface.get_name_by_id(id)
            current_app.logger.debug("completed operation get_name_by_id")
            return jsonify(name)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
    
    if request.method == 'PUT':
        if request.is_json:
            data_json = json.dumps(request.get_json())
            data_dict = yaml.safe_load(data_json)
            data_dict['n_id']=id
        else:
            abort(500, "the request does not contain data in json")

        try:
            current_app.logger.debug("running operation update_name")
            name = SystemInterface.update_name(data_dict)
            current_app.logger.debug("completed operation update_name")
            return jsonify(name)

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
        
    if request.method == 'DELETE':

        try:
            current_app.logger.debug("running operation delete_name")
            name = SystemInterface.delete_name(id)
            current_app.logger.debug("completed operation delete_name")
            return jsonify({"status":"sucess"})

        except NotAuthorizedError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                    "status code": 401,
                       "msg": err_str}
            abort(401, msg)

        except TypeError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str }
            abort(500, msg)

        except StateError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)

        except NotFoundError as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "status code": 404,
                       "msg": err_str}
            abort(404, msg)

        except Exception as e:
            current_app.logger.error("Exception = %s" % str(e))
            err_str = str(e)
            msg = {"status": "failure",
                       "msg": err_str}
            abort(500, msg)
