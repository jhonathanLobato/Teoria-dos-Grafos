import numpy as np

def sistema_nao_linear(x):
    # Defina aqui o seu sistema de equações não lineares.
    # Exemplo: x^2 + y^2 = 25 e x - y = 1
    eq1 = x[0]**2 + x[1]**2 - 25
    eq2 = x[0] - x[1] - 1
    return np.array([eq1, eq2])

def jacobiano(x):
    # Defina aqui o Jacobiano do seu sistema de equações.
    # Exemplo: Jacobiano da primeira equação: [2*x[0], 2*x[1]]
    #          Jacobiano da segunda equação: [1, -1]
    jaco_eq1 = [2*x[0], 2*x[1]]
    jaco_eq2 = [1, -1]
    return np.array([jaco_eq1, jaco_eq2])

def metodo_newton_sistema_nao_linear(guess, tol=1e-6, max_iter=100):
    x = np.array(guess)
    for i in range(max_iter):
        f = sistema_nao_linear(x)
        j = jacobiano(x)
        delta_x = np.linalg.solve(j, -f)
        x += delta_x
        if np.linalg.norm(delta_x) < tol:
            return x
    raise Exception("O método de Newton não convergiu após {} iterações".format(max_iter))

# Solicitar ao usuário as estimativas iniciais para as variáveis do sistema
x1 = float(input("Digite a estimativa inicial para x: "))
x2 = float(input("Digite a estimativa inicial para y: "))

guess = [x1, x2]

# Resolver o sistema não linear usando o método de Newton
resultado = metodo_newton_sistema_nao_linear(guess)

print("Solução encontrada:")
print("x =", resultado[0])
print("y =", resultado[1])

