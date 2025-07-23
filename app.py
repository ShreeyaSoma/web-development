from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "age": 24},
    {"id": 2, "name": "Bo", "age": 30}
]

teachers = [
    {"id": 1, "name": "Mr. Bob", "subject": "Math"},
    {"id": 2, "name": "Ms. Alice", "subject": "English"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/teachers', methods=['GET'])
def get_teachers():
    return jsonify(teachers), 200

# Adding a new user
@app.route('/users', methods=['POST'])
def add_users():
    new_user = request.json
    new_user['id'] = users[-1]['id'] + 1 if users else 1
    users.append(new_user)
    return jsonify(new_user), 201

# Updating existing user data
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_users(user_id): 
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user.update(data)  
    return jsonify(user), 200

#Deleting the data
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id']!=user_id]
    return jsonify({'message': f'User with id {user_id} deleted'}),200
if __name__ == '__main__':
    app.run(port=5000)
