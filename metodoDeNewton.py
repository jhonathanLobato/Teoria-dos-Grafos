import numpy as np

def metodoNewton(F, J, x0, tol=1e-6, max_iter=100):
    """
    Resolve sistemas não lineares usando o método de Newton.

    Args:
    F: Função que representa o sistema F(x) = 0.
    J: Função que calcula a matriz Jacobiana de F.
    x0: Valor inicial.
    tol: Tolerância para a convergência.
    max_iter: Número máximo de iterações.

    Returns:
    x: Solução aproximada do sistema.
    """

    x = x0
    for i in range(max_iter):
        Fx = F(x)
        Jx = J(x)
        dx = np.linalg.solve(Jx, -Fx) # Calcula a atualização usando a matriz jacobiana e o negatico da função do sistema
        x = x + dx # atualização de X

        if np.linalg.norm(dx) < tol:
            print(f"Convergiu após {i+1} iterações.")
            return x

    print("O método de Newton não convergiu.")
    return None


def sistema(x):
    eq1 = x[0] + x[1]**2 - 4
    eq2 = x[0]*x[1] - 1
    return np.array([eq1, eq2])

def jacobiana(x):
    J = np.array([
        [1, 2*x[1]],
        [x[1], x[0]]
    ])
    return J

x0 = np.array([1.0, 1.0]) # Valor inicial

solucao = metodoNewton(sistema, jacobiana, x0)
if solucao is not None:
    print("Solução aproximada:", solucao)
