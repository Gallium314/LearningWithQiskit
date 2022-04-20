import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

simulator = QasmSimulator()

circuit = QuantumCircuit(2, 2)

#H gate on the first qubit (0)
circuit.h(0)

#CX/CNOT gate controlled by qb 0 and targeting qb 1
circuit.cx(0,1)

#Make the measurements from the circuits into classical bits (0,1)
circuit.measure([0,1],[0,1])

#compile the circuit
compiled_circuit=transpile(circuit, simulator)

#exicute the circuit
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()

#counts from the circuit
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11:",counts)

#circuit diagram!
circuit.draw()
