from qiskit import QuantumCircuit

def assertNoCloning(circuit):
    """
    Verifica si un circuito cuántico intenta violar el teorema de no-clonación.
    
    :param circuit: QuantumCircuit de Qiskit a evaluar.
    :return: True si el circuito NO intenta clonar un estado cuántico arbitrario, False si hay intento de clonación.
    """
    cnot_pairs = set()
    
    for instr in circuit.data:
        operation = instr.operation  # Forma recomendada en Qiskit 1.2+
        qargs = instr.qubits
        
        if operation.name in ["swap", "cswap"]:
            return False  # La puerta SWAP puede usarse para copiar estados, lo que viola el teorema
        
        if operation.name == "cx":
            control, target = [circuit.find_bit(q).index for q in qargs]
            pair = (control, target)
            
            if pair in cnot_pairs:
                return False  # Si un CNOT se aplica dos veces sobre los mismos qubits, hay clonación
            
            cnot_pairs.add(pair)
    
    return True