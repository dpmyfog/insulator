import numpy as np
import pylab
np.set_printoptions(linewidth = 300)

i = 1j

def buildHamiltonian(hopping, size, type = 'tb'): #tightbinding by default
    if(type == 'tb'):
        hamiltonian = np.array([])
        hamiltonian.resize((size, size))

        for row in range(size):
            for col in range(size):
                if(row == col): hamiltonian[row,col] = 0
                elif(abs(row-col) == 1): hamiltonian[row,col] = hopping
                elif(abs(row-col) == size-1): hamiltonian[row,col] = hopping
                else: hamiltonian[row,col] = 0
        
        #print(hamiltonian)
    return hamiltonian


def buildMomentum(size):
    kArr = range(size)
    for idx in range(len(kArr)):
        kArr[idx] = kArr[idx]*2*np.pi/size
    
    #print kArr

    kMatrix = np.zeros((size,size), complex)
    
    rotation = np.zeros((size, size), complex)
    
    for row in range(size):
        for col in range(size):
            element = 0
            rotation[row, col] = np.exp(1j*row*col*2*np.pi/size)
            for idx in range(len(kArr)):
                element += kArr[idx]*np.exp(1j*(col - row)*kArr[idx])
            kMatrix[row,col] = element
            
            

    print "KMatrix: "
    print kMatrix
    print "Rotation: "
    print rotation
    return kMatrix, rotation



def testHamiltonian(hopping, size, type = 'tb'):
    hamiltonian = buildHamiltonian(hopping, size, type)
    (e,v) = np.linalg.eigh(hamiltonian)
    
    print "eivenvalues:"
    print e
    print "eigenvectors:"
    print v

    pylab.plot(v[:,0])
    pylab.plot(v[:,1])
    pylab.show()
    


    
hamiltonian = buildHamiltonian(-1, 5)
momentum, rotation = buildMomentum(5)

num = np.dot(hamiltonian, momentum)-np.dot(momentum, hamiltonian)

diagonalK = np.dot(np.dot(np.matrix(rotation).getH(), np.matrix(momentum)), np.matrix(rotation))


print num
print diagonalK
