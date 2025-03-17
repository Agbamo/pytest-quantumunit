import pytest
from src.quantumunit.assertions import assertStatevectorEqual, assertDensityMatrixEqual
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

class QuantumAssertions:
    def assert_statevector_equal(self, circuit, expected_statevector, epsilon=0.05):
        """
        Verifica si el statevector del circuito cuántico coincide con el esperado.
        """
        return assertStatevectorEqual(circuit, expected_statevector, epsilon)
    
    def assert_density_matrix_equal(self, circuit, expected_density_matrix, epsilon=0.05):
        """
        Verifica si la matriz de densidad del circuito cuántico coincide con la esperada.
        """
        return assertDensityMatrixEqual(circuit, expected_density_matrix, epsilon)

@pytest.fixture
def qt():
    """
    Fixture that provides assertions of QuantumUnit for tests with pytest.
    """
    return QuantumAssertions()

def pytest_assertrepr_compare(op, left, right):
    """
    Mejora la salida de error de pytest al fallar assertions de QuantumUnit.
    """
    if isinstance(left, QuantumAssertions) and isinstance(right, QuantumAssertions):
        return [
            "QuantumUnit Assertion Failed:",
            f"   Left:  {left}",
            
            f"   Right: {right}",
        ]
