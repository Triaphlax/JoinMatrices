from scipy.optimize import linprog
import sympy
import BitOperations

startingMatrix = [
                        [1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1],
                        [2, 1, 0, 1, 0, 0],
                        [0, 1, 2, 0, 1, 0],
                        [0, 0, 0, 1, 1, 2]
                 ]

# Write matrix in RREF
rrefMatrix = sympy.Matrix(startingMatrix).rref()

print(rrefMatrix)

# Constants vector
c = [1, 1, 1, 1, 1, 1]

# Vectors for each of the variables
columns = []
onlyRrefMatrix = rrefMatrix[0]
for columnIndex in range(0, 6):
    columns.append(list(map(lambda x: x * -1, onlyRrefMatrix.col(columnIndex))))

# Set equation to minimize
c = [1, 1, 1, 1, 1, 1]

# Loop through all possible subsets that could potentially be filtered.
for subsetIndex in range(0, 64):
    # upper bounds
    Aub = [[-1, -1, -1, -1, -1, -1]]
    bub = [-0.0001]

    # equalities
    Aeq = []
    beq = []

    # assign equalities and inequalities
    filterString = ""
    digits = BitOperations.getAllDigitsB(subsetIndex)
    for varIndex, inUpperBound in enumerate(digits):
        if inUpperBound:
            Aub.append(columns[varIndex])
            bub.append(-0.0001)
            filterString += chr(varIndex + 97)
        else:
            Aeq.append(columns[varIndex])
            beq.append(0)

    # perform linear programming
    res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, options={"disp": True})
    print("-----------------------")
    print(filterString)
    #print(res["success"])
