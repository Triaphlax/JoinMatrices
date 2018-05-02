from scipy.optimize import linprog


startingMatrix = [
                        [1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1],
                        [2, 1, 0, 1, 0, 0],
                        [0, 1, 2, 0, 1, 0],
                        [0, 0, 0, 1, 1, 2]
                 ]

c = [1, 1, 1, 1]
Aub = [[0, -1, 0, 0], [0, 0, 0, -1], [0, 2, -1, -2], [-1, -1, -1, -1]]
bub = [-0.001, -0.001, -0.001, -0.001]
Aeq = [[-1, 0, 0, 0], [0, 0, -1, 0], [0, 1, -1, -1]]
beq = [0, 0, 0]
res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, options={"disp": True})

print(res)