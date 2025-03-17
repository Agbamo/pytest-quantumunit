import pytest
from qiskit import QuantumCircuit
from src.quantumunit.entanglement import assertEntanglement

def test_assertEntanglement():
    """Prueba la verificación de entrelazamiento entre dos qubits."""
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)  # Aplica CNOT para generar entrelazamiento
    
    assert assertEntanglement(circuit, 0, 1) == True

"""
def test_assertGeneralEntanglement():
    """"""Prueba la verificación de entrelazamiento en múltiples qubits.""""""
    circuit = QuantumCircuit(3, 3)  # Se añade un registro clásico
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    circuit.measure([0, 1, 2], [0, 1, 2])  # Se añaden mediciones
  
    assert assertGeneralEntanglement(circuit, [0, 1, 2]) == True
"""

def test_no_entanglement():
    """Prueba un caso donde no hay entrelazamiento."""
    circuit = QuantumCircuit(2)
    circuit.h(0)
    
    assert assertEntanglement(circuit, 0, 1) == False

