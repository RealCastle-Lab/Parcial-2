# app/routes.py
from flask_restful import Resource
from .data_loader import load_vaccination_data

vaccination_data = load_vaccination_data()

class VaccinationList(Resource):
    def get(self):
        return vaccination_data

class VaccinationYear(Resource):
    def get(self, year):
        results = [record for record in vaccination_data if str(record['Year']) == year]
        if not results:
            return {'message': 'No data found for this year'}, 404
        return results

def initialize_routes(api):
    api.add_resource(VaccinationList, '/api/vaccinations')
    api.add_resource(VaccinationYear, '/api/vaccinations/<string:year>')
