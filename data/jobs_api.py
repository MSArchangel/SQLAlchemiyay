import flask
from flask import jsonify, request
from . import db_session

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {'jobs': [
            item.to_dict(
                only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                      'end_date', 'is_finished')) for item in jobs]})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({"error": "Not found!"})
    return jsonify(
        {'jobs': [
            jobs.to_dict(
                only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                      'end_date', 'is_finished'))]})
