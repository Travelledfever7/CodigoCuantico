from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

q =  QuantumRegister(2, "q")
c = ClassicalRegister(2, "c")
qc = QuantumCircuit(q, c)
                                   
qc.x(q[0])                          
qc.barrier()
qc.h(q[0])                         
qc.h(q[1])
qc.cx(q[1], q[0])                  
qc.h(q[0])                         
qc.h(q[1])
qc.measure(q, c)                  

display(qc.draw(output='mpl'))

sampler = Sampler()
job = sampler.run(qc)
print(job.result().quasi_dists[0].binary_probabilities())
