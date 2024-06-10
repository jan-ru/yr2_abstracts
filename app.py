from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os

app = Flask(__name__)

# Path to your JSON database file
DATABASE_FILE = 'abstracts_definitions.json'
RECORDS_PER_PAGE = 1  # Show one record per page

# Load the database
def load_database():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Save the database
def save_database(data):
    with open(DATABASE_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return redirect(url_for('records', page=1))

@app.route('/records/<int:page>', methods=['GET'])
def records(page):
    data = load_database()
    start = (page - 1) * RECORDS_PER_PAGE
    end = start + RECORDS_PER_PAGE
    records = data[start:end]
    total_pages = (len(data) + RECORDS_PER_PAGE - 1) // RECORDS_PER_PAGE
    return render_template('index.html', data=records, page=page, total_pages=total_pages)

@app.route('/add', methods=['POST'])
def add_record():
    new_record = request.form.to_dict()
    data = load_database()
    new_record['ID'] = max([record['ID'] for record in data], default=0) + 1  # Assign new ID
    data.append(new_record)
    save_database(data)
    return redirect(url_for('records', page=1))

@app.route('/update/<int:record_id>', methods=['POST'])
def update_record(record_id):
    updated_record = request.form.to_dict()
    data = load_database()
    for record in data:
        if record['ID'] == record_id:
            record.update(updated_record)
            break
    save_database(data)
    return redirect(url_for('records', page=1))

@app.route('/delete/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    data = load_database()
    data = [record for record in data if record['ID'] != record_id]
    save_database(data)
    return redirect(url_for('records', page=1))

@app.route('/api/records', methods=['GET'])
def api_get_records():
    data = load_database()
    return jsonify(data)

@app.route('/api/record/<int:record_id>', methods=['GET'])
def api_get_record(record_id):
    data = load_database()
    record = next((record for record in data if record['ID'] == record_id), None)
    return jsonify(record)

@app.route('/api/add', methods=['POST'])
def api_add_record():
    new_record = request.json
    data = load_database()
    new_record['ID'] = max([record['ID'] for record in data], default=0) + 1  # Assign new ID
    data.append(new_record)
    save_database(data)
    return jsonify(new_record), 201

@app.route('/api/delete/<int:record_id>', methods=['DELETE'])
def api_delete_record(record_id):
    data = load_database()
    data = [record for record in data if record['ID'] != record_id]
    save_database(data)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
