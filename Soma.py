x = [5, 2, 1, 3, 4]
y = [600, 1200, 1000, 700, 300]


def Minimos_Quadrados(x, y):

    n = len(x)

    X_vezes_y = (x[0] * y[0]) + (x[1] * y[1]) + (x[2] * y[2]) + (x[3] * y[3]) + (x[4] * y[4])

    x_aoQuarado = (x[0] ** 2) + (x[1] ** 2) + (x[2] ** 2) + (x[3] ** 2) + (x[4] ** 2)

    soma_x = x[0] + x[1] + x[2] + x[3] + x[4]

    soma_y = y[0] + y[1] + y[2] + y[3] + y[4]


    a = ((n * X_vezes_y) - (soma_x * soma_y)) / ((n * x_aoQuarado) - (soma_x * soma_x))
    b1 = (soma_y) - (a) * (soma_x)
    b = b1 / n
    print('y=',a,'x +',b )


Minimos_Quadrados(x, y)
