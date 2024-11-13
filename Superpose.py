from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import Aer
def superpose(n: int) -> QuantumCircuit:
    qr = QuantumRegister(n)
    cr = ClassicalRegister(n)
    qc = QuantumCircuit(qr,cr)
    
    for i in range(n):
        qc.h(qr[i])
        
    qc.measure(qr,cr)
    
    return qc

n = int(input("Enter the number of qubits: "))
qc = superpose(n)

# drawing the circuit
# qc.draw(output="mpl", filename='interferometer_circuit.png')

# transpiling the circuit for Aer simulator
simulator = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, simulator)

# executing the transpiled circuit
job = simulator.run(tqc, shots=1024)

# get the counts of the measurement outcomes
counts = job.result().get_counts()

print(counts)
