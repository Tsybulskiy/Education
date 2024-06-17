import math

def solve_task1():
    f = float(input("Введите частоту в ГГц: "))
    eps = float(input("Введите эпсилон: "))
    sigma = float(input("Введите сигма: "))
    A = float(input("Введите амплитуду вектора E: "))
    z = float(input("Введите расстояние z: "))
    m = float(input("Введите число m: "))

    epsilon0 = 8.85 * 10**(-12)
    mu0 = 4 * math.pi * 10**(-7)

    tgdelta = sigma / (2 * math.pi * f * 10**9 * eps * epsilon0)
    if tgdelta >= 0.1:
        alpha = 2 * math.pi * f * 10**9 * math.sqrt(((epsilon0 * mu0) / 2) * math.sqrt(1 + tgdelta**2) - 1)
        beta = 2 * math.pi * f * 10**9 * math.sqrt(((epsilon0 * mu0) / 2) * math.sqrt(1 + tgdelta**2) + 1)
        Zv = 120 * math.pi * math.sqrt(1 / (eps * math.sqrt(1 + tgdelta ** 2)))
    else:
        alpha = 60 * math.pi * sigma * math.sqrt(1 / eps)
        beta = (2 * math.pi * f * 10**9) / 3e8 * math.sqrt(eps)
        Zv= 120*math.pi*math.sqrt(1/eps)
    lmbd = 2 * math.pi / beta
    vf = (2 * math.pi * f * 10**9) / beta
    vg = (2 * math.pi * f * 10**9) / beta

    delta = 1 / alpha
    jprm0= sigma * A
    jprm = sigma * A * math.exp(-alpha * z)
    jcmm0= epsilon0 * eps * A * 2 * math.pi * f * 10**9
    jcmm = epsilon0 * eps * A * math.exp(-alpha * z) * 2 * math.pi * f * 10**9
    P0= (A)**2 / (2 * Zv)
    PZ = (A * math.exp(-alpha * z))**2 / (2 * Zv)
    z1 = math.log(m) / alpha

    print("Вычисления для задачи 1:")
    print("tgdelta =", tgdelta)
    print("alpha =", alpha)
    print("beta =", beta)
    print("lambda =", lmbd)
    print("vf =", vf)
    print("vg =", vg)
    print("Zv =", Zv)
    print("delta =", delta)
    print("jprm0 =", jprm0)
    print("jprm =", jprm)
    print("jcmm0 =", jcmm0)
    print("jcmm =", "{:.15f}".format(jcmm))
    print("P0 =", P0)
    print("PZ =", "{:.15f}".format(PZ))
    print("z1 =", z1)


