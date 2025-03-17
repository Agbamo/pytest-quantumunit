from qiskit.quantum_info import Statevector, partial_trace, DensityMatrix
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
import numpy as np

def concurrence(rho):
    """
    Calcula la concurrencia de Wootters para determinar entrelazamiento en dos qubits.
    """
    if rho.shape != (4, 4):
        return 0  # Si la matriz no es 4x4, no hay entrelazamiento
    pauli_y = np.array([[0, -1j], [1j, 0]])
    yy = np.kron(pauli_y, pauli_y)
    rho_tilde = yy @ rho @ yy.conj().T
    
    # Asegurar que los valores propios sean >= 0
    eigvals = np.real(np.linalg.eigvals(rho @ rho_tilde))
    eigvals = np.where(eigvals < 0, 0, eigvals)  # Reemplazar negativos con 0
    sqrt_eigvals = np.sort(np.sqrt(eigvals))[::-1]  # Raíz cuadrada de valores positivos
    
    concurrence_value = max(0, sqrt_eigvals[0] - sum(sqrt_eigvals[1:]))
    return concurrence_value

def partial_transpose(rho, dim, qubits):
    """
    Aplica la transposición parcial a una matriz de densidad.
    """
    rho = rho.reshape([dim] * 2 * len(qubits))
    perm = list(range(len(qubits))) + [i + len(qubits) for i in qubits]
    rho_T = rho.transpose(perm)
    return rho_T.reshape((dim**len(qubits), dim**len(qubits)))

def negativity(rho):
    """
    Calcula la negatividad de la transposición parcial como métrica de entrelazamiento multipartito.
    """
    eigvals = np.linalg.eigvals(rho)  # Obtener autovalores
    negative_eigvals = eigvals[eigvals < 0]  # Filtrar negativos
    return -np.sum(negative_eigvals)  # Sumar en valor absoluto

"""
def assertGeneralEntanglement(circuit, qubits, shots=1024, epsilon=0.05):
    """"""
    Verifica el entrelazamiento de múltiples qubits analizando la paridad de los resultados tras aplicar puertas CNOT.
    
    Args:
        circuit (QuantumCircuit): El circuito cuántico a verificar.
        qubits (list): Lista de índices de los qubits a analizar.
        shots (int): Número de ejecuciones en el simulador.
        epsilon (float): Margen de error para la correlación de paridad.

    Returns:
        bool: True si se detecta entrelazamiento, False en caso contrario.
    """"""

    # Copiar el circuito original para no modificarlo
    test_circuit = circuit.copy()
    
    # Aplicar una cadena de puertas CNOT para correlacionar los qubits
    for i in range(len(qubits) - 1):
        test_circuit.cx(qubits[i], qubits[i + 1])
    
    # Agregar mediciones
    test_circuit.measure_all()
    
    # Simulación con Qiskit Aer
    simulator = Aer.get_backend("qasm_simulator")
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit, shots=shots).result()  # ✅ DIRECTO, SIN `assemble()`

    # Obtener conteo de mediciones
    counts = result.get_counts()

    # Análisis de paridad: Contamos cuántos resultados tienen un número par/impar de '1s'
    paridad_par = sum(count for outcome, count in counts.items() if outcome.count("1") % 2 == 0)
    paridad_impar = sum(count for outcome, count in counts.items() if outcome.count("1") % 2 == 1)
    
    # Se considera entrelazado si una de las paridades domina significativamente
    total_shots = paridad_par + paridad_impar
    correlacion = max(paridad_par, paridad_impar) / total_shots  # Probabilidad de la paridad más dominante
    
    print("Entanglement check:")
    print(f"Counts: {counts}")
    print(f"Paridad Par: {paridad_par}")
    print(f"Paridad Impar: {paridad_impar}")
    print(f"Total shots: {total_shots}")
    print(f"Correlación calculada: {correlacion}")
    print(f"Condición de entanglement: {correlacion > (0.5 + epsilon)}")
    print("Simulated counts:", counts)  # Ver los resultados obtenidos en la simulación
    print("Measured bitstrings:", list(counts.keys()))  # Ver qué estados medidos se observaron

    return correlacion > (0.5 + epsilon)
"""

def assertEntanglement(circuit, qubit_1, qubit_2, epsilon=1e-5):
    """
    Verifica si dos qubits en un circuito cuántico están entrelazados usando concurrencia.
    """
    state = Statevector.from_instruction(circuit)
    num_qubits = circuit.num_qubits

    # Si hay más de dos qubits, hacer la traza parcial de los otros qubits
    if num_qubits > 2:
        remaining_qubits = list(set(range(num_qubits)) - {qubit_1, qubit_2})
        reduced_state = DensityMatrix(partial_trace(state, remaining_qubits))
    else:
        reduced_state = DensityMatrix(state)

    rho_matrix = reduced_state.data
    concurrence_value = concurrence(rho_matrix)
    return concurrence_value > epsilon