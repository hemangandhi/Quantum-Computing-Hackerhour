import qiskit as q
import json

def exec_circuit(qasm):
    circ = q.QuantumCircuit.from_qasm_str(qasm)
    sim = q.execute(circ, q.Aer.get_backend('qasm_simulator'))
    return sim.result()

def add_cors_headers(resp):
    """
    Adds headers to allow for cross-origin requests.

    Not gonna lie, stackoverflow told us to do it
    and it works. We don't know how or why.
    """
    if 'headers' not in resp:
        resp['headers'] = dict()
    resp['headers']['Access-Control-Allow-Origin'] = '*',
    resp['headers']['Access-Control-Allow-Headers'] ='Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
    resp['headers']['Access-Control-Allow-Credentials'] = True,
    return resp

def lambda_handler(event, context):
    if 'code' not in event:
        return add_cors_headers({"statusCode":400,"body":"Invalid Request"})
    else:
        try:
            res = exec_circuit(event['code'])
            j = json.loads({"result": res})
            return add_cors_headers({"statusCode":200,"body":j})
        except e:
            return add_cors_headers({"statusCode":400,"body":str(e)})
