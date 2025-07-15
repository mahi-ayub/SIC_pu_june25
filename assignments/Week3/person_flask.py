from flask import Flask, jsonify, request
from person_dao import Person, Db_operations

people = Db_operations()
people.create_db()
people.create_table()

app = Flask(__name__)

@app.route('/people', methods=['POST'])
def people_create():
    body = request.get_json()
    new_person = Person(body['name'], body['gender'], body['dob'], body['location'])
    id = people.insert_row(new_person)
    person = people.search_row(id)
    if person:
        person_dict = {
            'id': person[0],
            'name': person[1],
            'gender': person[2],
            'location': person[3],
            'dob': str(person[4])
        }
        return jsonify(person_dict)
    return jsonify({'message': 'Error creating person'}), 500

@app.route('/people/<int:id>', methods=['GET'])
def people_read_by_id(id):
    person = people.search_row(id)
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'location': person[3],
        'dob': str(person[4])
    })

@app.route('/people', methods=['GET'])
def people_read_all():
    people_list = people.list_all_rows()
    result = [{
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'location': person[3],
        'dob': str(person[4])
    } for person in people_list]
    return jsonify(result)

@app.route('/people/<int:id>', methods=['PUT'])
def people_update(id):
    body = request.get_json()
    old_person = people.search_row(id)
    if not old_person:
        return jsonify({'message': 'Person not found'}), 404

    updated_data = (
        body['name'],
        body['gender'],
        body['location'],
        body['dob'],
        id
    )
    people.update_row(updated_data)

    person = people.search_row(id)
    return jsonify({
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'location': person[3],
        'dob': str(person[4])
    })

@app.route('/people/<int:id>', methods=['DELETE'])
def people_delete(id):
    person = people.search_row(id)
    if not person:
        return jsonify({'message': 'Person not found', 'is_error': 1}), 404
    people.delete_row(id)
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

if __name__ == '__main__':
    app.run(debug=True)
