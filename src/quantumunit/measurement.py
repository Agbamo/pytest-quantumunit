from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import numpy as np

def assertMeasurementDistribution(circuit, shots, expected_distribution, epsilon=0.05):
    """
    Verifica si la distribución de medidas de un circuito cuántico coincide con la esperada.
    
    :param circuit: QuantumCircuit de Qiskit a evaluar.
    :param shots: Número de ejecuciones para obtener estadísticas.
    :param expected_distribution: Diccionario con la distribución esperada de resultados {"00": 0.5, "11": 0.5}.
    :param epsilon: Margen de error permitido en la comparación de probabilidades.
    :return: True si la distribución medida está dentro del margen de error, False en caso contrario.
    """
    simulator = AerSimulator()
    circuit.measure_all()
    compiled_circuit = transpile(circuit, simulator)
    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts()
    
    # Convertir los conteos en una distribución de probabilidades
    measured_distribution = {state: count / shots for state, count in counts.items()}
    
    # Comparar con la distribución esperada
    for state, expected_prob in expected_distribution.items():
        measured_prob = measured_distribution.get(state, 0)  # 0 si el estado no se midió
        if not np.isclose(measured_prob, expected_prob, atol=epsilon):
            return False
    return True