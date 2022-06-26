from qiskit.circuit.library import XGate
from qiskit.circuit.library import ZFeatureMap
from qiskit.circuit.library import RealAmplitudes
from qiskit.circuit import QuantumCircuit

circuit = QuantumCircuit(3, 3)

circuit.x(1)
circuit.h(range(3))
circuit.cx(0, 1)
circuit.measure(range(3), range(3));
circuit.draw(output='mpl')

# print(gate.power(1/2).to_matrix())  # √X gate
# print(gate.control(1).to_matrix())

#https://qiskit.org/documentation/apidoc/circuit_library.html