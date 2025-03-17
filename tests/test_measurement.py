import pytest
from qiskit import QuantumCircuit
from src.quantumunit.measurement import assertMeasurementDistribution

def test_balanced_distribution():
    """Prueba un circuito con distribución esperada equilibrada."""
    circuit = QuantumCircuit(1)
    circuit.h(0)
    shots = 1000
    expected_distribution = {"0": 0.5, "1": 0.5}
    assert assertMeasurementDistribution(circuit, shots, expected_distribution) == True

def test_unbalanced_distribution():
    """Prueba un circuito donde el resultado es altamente predecible."""
    circuit = QuantumCircuit(1)
    circuit.x(0)  # Aplica X, siempre debería medir "1"
    shots = 1000
    expected_distribution = {"1": 1.0}
    assert assertMeasurementDistribution(circuit, shots, expected_distribution) == True

def test_invalid_distribution():
    """Prueba un circuito donde la distribución no coincide con la esperada."""
    circuit = QuantumCircuit(1)
    circuit.h(0)
    shots = 1000
    expected_distribution = {"0": 0.8, "1": 0.2}  # Valores incorrectos
    assert assertMeasurementDistribution(circuit, shots, expected_distribution) == False
