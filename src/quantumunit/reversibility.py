from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import numpy as np

def assertReversibility(circuit, epsilon=1e-5):
    """
    Verifica si un circuito cuántico es unitario, es decir, si U * U† = I.
    
    :param circuit: QuantumCircuit de Qiskit a evaluar.
    :param epsilon: Margen de error permitido en la comparación con la identidad.
    :return: True si el circuito es unitario, False en caso contrario.
    """
    # Detectar si el circuito contiene medidas
    if any(instr.operation.name == "measure" for instr in circuit.data):
        return False  # Un circuito con medidas no es unitario
    
    unitary = Operator(circuit).data  # Obtiene la matriz unitaria del circuito
    identity = np.eye(unitary.shape[0])  # Matriz identidad del mismo tamaño
    
    # Verifica si U * U† ≈ I
    return np.allclose(unitary @ unitary.conj().T, identity, atol=epsilon)