import pytest
from qiskit import QuantumCircuit
from src.quantumunit.no_cloning import assertNoCloning

def test_valid_circuit():
    """Prueba un circuito que NO intenta clonar un estado."""
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)  # Esta CNOT no es suficiente para una clonación completa
    assert assertNoCloning(circuit) == True

def test_swap_violation():
    """Prueba un circuito con una puerta SWAP, que puede usarse para copiar información."""
    circuit = QuantumCircuit(2)
    circuit.swap(0, 1)
    assert assertNoCloning(circuit) == False

def test_cnot_violation():
    """Prueba un circuito que usa CNOT para intentar copiar información."""
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)  # Intento de clonar estado
    circuit.cx(0, 1)  # Aplicado de nuevo, lo que indica posible clonación
    assert assertNoCloning(circuit) == False
