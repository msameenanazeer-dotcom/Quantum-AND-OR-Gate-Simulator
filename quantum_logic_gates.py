from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


simulator = AerSimulator()


def AND_gate(a, b):
    circuit = QuantumCircuit(3, 1)

    # Input A
    if a == 1:
        circuit.x(0)

    # Input B
    if b == 1:
        circuit.x(1)

    # Toffoli gate
    circuit.ccx(0, 1, 2)

    # Measure output
    circuit.measure(2, 0)

    result = simulator.run(circuit, shots=1).result()
    output = int(list(result.get_counts())[0])

    return output, circuit


def OR_gate(a, b):
    circuit = QuantumCircuit(3, 1)

    # Input A
    if a == 1:
        circuit.x(0)

    # Input B
    if b == 1:
        circuit.x(1)

    # OR = NOT(NOT A AND NOT B)
    circuit.x(0)
    circuit.x(1)

    circuit.ccx(0, 1, 2)

    circuit.x(2)

    # Restore inputs
    circuit.x(0)
    circuit.x(1)

    # Measure output
    circuit.measure(2, 0)

    result = simulator.run(circuit, shots=1).result()
    output = int(list(result.get_counts())[0])

    return output, circuit


print("=" * 45)
print("      QUANTUM AND / OR GATE SIMULATOR")
print("=" * 45)

print("\nAND GATE")
print("A  B  |  Output")
print("----------------")

for a in [0, 1]:
    for b in [0, 1]:
        output, circuit = AND_gate(a, b)
        print(f"{a}  {b}  |    {output}")


print("\nOR GATE")
print("A  B  |  Output")
print("----------------")

for a in [0, 1]:
    for b in [0, 1]:
        output, circuit = OR_gate(a, b)
        print(f"{a}  {b}  |    {output}")


print("\nAND Circuit (A=1, B=1):")
_, and_circuit = AND_gate(1, 1)
print(and_circuit.draw())


print("\nOR Circuit (A=0, B=1):")
_, or_circuit = OR_gate(0, 1)
print(or_circuit.draw())
