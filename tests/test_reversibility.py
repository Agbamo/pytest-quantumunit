import pytest
from qiskit import QuantumCircuit
from src.quantumunit.reversibility import assertReversibility

def test_unitary_circuit():
    """Prueba un circuito unitario simple."""
    circuit = QuantumCircuit(1)
    circuit.h(0)  # Hadamard es una operación unitaria
    assert assertReversibility(circuit) == True

def test_non_unitary_circuit():
    """Prueba un circuito que no es unitario (medida incluida)."""
    circuit = QuantumCircuit(1)
    circuit.h(0)
    circuit.measure_all()  # Medir destruye la unitariedad
    assert assertReversibility(circuit) == False

def test_multi_qubit_unitary():
    """Prueba un circuito unitario de múltiples qubits."""
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)  # Puerta CNOT, combinación de Hadamard y CNOT es unitaria
    assert assertReversibility(circuit) == True