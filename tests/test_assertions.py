import pytest
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, DensityMatrix
from src.quantumunit.assertions import assertStatevectorEqual, assertDensityMatrixEqual

def test_assertStatevectorEqual():
    """Prueba la verificación de statevector."""
    circuit = QuantumCircuit(1)
    circuit.h(0)  # Aplica puerta Hadamard
    expected_statevector = Statevector.from_instruction(circuit).data
    assert assertStatevectorEqual(circuit, expected_statevector) == True
    
    wrong_statevector = np.array([1, 0])  # Un estado incorrecto
    assert assertStatevectorEqual(circuit, wrong_statevector) == False

def test_assertDensityMatrixEqual():
    """Prueba la verificación de la matriz de densidad."""
    circuit = QuantumCircuit(1)
    circuit.h(0)  # Aplica puerta Hadamard
    expected_density_matrix = DensityMatrix.from_instruction(circuit).data
    assert assertDensityMatrixEqual(circuit, expected_density_matrix) == True
    
    wrong_density_matrix = np.array([[1, 0], [0, 0]])  # Matriz incorrecta
    assert assertDensityMatrixEqual(circuit, wrong_density_matrix) == False
