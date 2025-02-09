# OpenNet - Python API Creation

## Description
This project contains a simple RESTful API created using Flask. The API has one endpoint `/greet` that accepts a GET request and returns a JSON response with a greeting message.

## Directory Structure
```
OpenNet_Q3/
├── Q3_API_creation.py  
├── README.md           
├── requirements.txt
├── assets/
│   ├── OpenNet_Q3.gif 
```

## Requirements
To install the required dependencies, run:
```
pip install -r requirements.txt
```

## Running the API
To run the API, execute the following command:
```
python3 Q3_API_creation.py
```
The API will be available at `http://127.0.0.1:5000/greet`.

## Example Usage
To get a greeting message, you can use a web browser or tools like `curl` or `Postman` to make a GET request to the endpoint:
```
http://127.0.0.1:5000/greet?name=YourName
```
If the `name` parameter is not provided, it will default to "World".

## Demonstration
![API Running GIF](https://github.com/SharkBlahaj/OpenNet_Q3/blob/main/assets/OpenNet_Q3.gif)

