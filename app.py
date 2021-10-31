from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
  new_data = request.get_json()
  print(new_data)
  incomes.append(new_data )
  print(incomes)
  return jsonify(incomes), 204

if __name__ == '__main__':
  app.run(host='127.0.0.4', port=80, debug=True)