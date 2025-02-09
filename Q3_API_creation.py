'''
### OpenNet - Python
Question 3: API Creation

Problem Statement:
Create a simple RESTful API using Flask. 
The API should have one endpoint /greet that accepts a GET request and returns a JSON response with a greeting message.

Requirements:
- Use the Flask or Fastapi library. 
- The endpoint /greet should accept a query parameter name and return a JSON response in the format:  {"message": "Hello, 
{name}!"} . 
- If the name parameter is not provided, the response should be  {"message": "Hello, World!"} . 
'''

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)