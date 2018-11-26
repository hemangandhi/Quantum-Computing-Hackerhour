from flask import Flask, render_template, request, redirect
import qiskit as q

def make_circuit():
    qr = q.QuantumRegister(2)
    cr = q.ClassicalRegister(2)
    circ = q.QuantumCircuit(qr, cr)
    circ.h(qr[0])
    circ.cx(qr[0], qr[1])
    circ.measure(qr, cr)
    return circ

def exec_circuit(circ):
    sim = q.execute(circ, q.Aer.get_backend('qasm_simulator'))
    return sim.result()

app = Flask(__name__)
if __name__ == '__main__':
    # app.run(port=5000)
    print(exec_circuit(make_circuit()).get_counts())
