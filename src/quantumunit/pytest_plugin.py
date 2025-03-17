import pytest
from .entanglement import assertEntanglement
from .measurement import assertMeasurementDistribution
from .no_cloning import assertNoCloning
from .reversibility import assertReversibility
from .assertions import assertStatevectorEqual, assertDensityMatrixEqual

# Hook para personalizar la salida de errores en pytest
@pytest.hookimpl(tryfirst=True)
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, bool) and isinstance(right, bool):
        return [f"Assertion failed in QuantumUnit: {left} {op} {right}"]

@pytest.fixture
def entanglement():
    """
    Fixture for testing entanglement in quantum circuits.
    """
    return assertEntanglement

@pytest.fixture
def measurement_distribution():
    """
    Fixture for validating probability distributions
    in quantum measurements.
    """
    return assertMeasurementDistribution

@pytest.fixture
def no_cloning():
    """
    Fixture to check for violations of the no-cloning theorem.
    """
    return assertNoCloning

@pytest.fixture
def reversibility():
    """
    Fixture to verify the reversibility of quantum operations.
    """
    return assertReversibility

@pytest.fixture
def statevector_equal():
    """
    Fixture to compare quantum statevectors within a defined margin of error.
    """
    return assertStatevectorEqual

@pytest.fixture
def density_matrix_equal():
    """
    Fixture to compare quantum density matrices within a defined margin of error.
    """
    return assertDensityMatrixEqual

#@pytest.fixture
#def general_entanglement():
#    return assertGeneralEntanglement


