import numpy as np
from qiskit.quantum_info import Statevector, DensityMatrix

def assertStatevectorEqual(circuit, expected_statevector, epsilon=0.05):
    """
    Verifica si el statevector del circuito cuántico coincide con el esperado dentro de un margen de error.
    
    :param circuit: QuantumCircuit de Qiskit a evaluar.
    :param expected_statevector: Lista de complejos representando el statevector esperado.
    :param epsilon: Margen de error permitido en la comparación.
    :return: True si son equivalentes dentro del margen, False en caso contrario.
    """
    simulated_statevector = Statevector.from_instruction(circuit).data
    return np.allclose(simulated_statevector, expected_statevector, atol=epsilon)

def assertDensityMatrixEqual(circuit, expected_density_matrix, epsilon=0.05):
    """
    Verifica si la matriz de densidad del circuito cuántico coincide con la esperada dentro de un margen de error.
    
    :param circuit: QuantumCircuit de Qiskit a evaluar.
    :param expected_density_matrix: Matriz numpy representando la densidad esperada.
    :param epsilon: Margen de error permitido en la comparación.
    :return: True si son equivalentes dentro del margen, False en caso contrario.
    """
    simulated_density_matrix = DensityMatrix.from_instruction(circuit).data
    return np.allclose(simulated_density_matrix, expected_density_matrix, atol=epsilon)
