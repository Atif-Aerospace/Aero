from flask import Flask, render_template, jsonify, request, make_response
import models

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/aircadia')
def aaa():
    return "Hello, AirCADia!"

@app.route('/ExecuteModel', methods=["POST"])
def ExecuteModels():
	if request.is_json:
		req_json = request.get_json()

		modelName = req_json.get("name")
		print(req_json["name"])
		args = ()
		for input in req_json["inputs"]:
			print(str(input["name"]) + " = " + str(input["value"]))
			args += (float(input["value"]),)
		
		outputs = ()
		for output in req_json["outputs"]:
			print(str(output["name"]) + " = " + str(output["value"]))
			outputs += (output["value"],)
		
		y1 = getattr(models, modelName)(*args)
		print(y1)

		response_body = {
            "ModelName": modelName,
			"inputs": [],
			"outputs": []
        }
		for input in req_json["inputs"]:
			response_body["inputs"].append({"name": input["name"], "value": input["value"]})
		for output in req_json["outputs"]:
			response_body["outputs"].append({"name": output["name"], "value": y1})

		res = make_response(jsonify(response_body), 200)
		return res
	else:
		print("Error")
		return make_response(jsonify({"message": "Request body must be JSON"}), 400)


if __name__ == '__main__':
    app.run(debug=True)