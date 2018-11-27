import qiskit as q
from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path="/", static_folder=".")

def exec_circuit(qasm):
    circ = q.QuantumCircuit.from_qasm_str(qasm)
    sim = q.execute(circ, q.Aer.get_backend('qasm_simulator_py'))
    return sim.result().get_counts()

@app.route('/code', methods=['POST'])
def lambda_handler():
    event = request.json
    if 'code' not in event:
        return "Invalid Request", 400

    try:
        res = exec_circuit(event['code'])
        return jsonify({"result": res})
    except Exception as e:
        return str(e), 400

@app.route('/')
def pendejo():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    # app.run(port=5000, debug=True, host='0.0.0.0')
    app.run(port=5000, debug=True)
