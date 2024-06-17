from decimal import Decimal, getcontext
import math
def solve_task2():
    getcontext().prec = 28
    f = float(input("Введите частоту в МГц: "))
    mu = float(input("Введите мю: "))
    sigma = float(input("Введите сигма: "))
    A = float(input("Введите амплитуду вектора E: "))
    z = float(input("Введите расстояние z в мм: "))
    m = float(input("Введите число m: "))
    freq = f * 10**6
    z_m = z / 1000

    mu0 = 4 * math.pi * 10**(-7)
    epsilon0 = 8.85 * 10 ** (-12)
    tgdelta = sigma / (2 * math.pi * freq * 1 * epsilon0)
    alpha = math.sqrt(math.pi * freq * sigma * mu * mu0)
    beta = alpha
    lmbd = 2 * math.pi / beta
    vf = (2 * math.pi * freq) / beta
    Zv = math.sqrt((2 * math.pi * freq * mu * mu0) / sigma)
    delta = 1 / alpha
    jprm0= sigma * A
    jprm = sigma * A * math.exp(-alpha * z_m)
    jcmm0 = epsilon0 * 1 * A * 2 * math.pi * freq
    jcmm = epsilon0 * 1 * A * math.exp(-alpha * z) * 2 * math.pi * freq
    P0= (A)**2 / (2 * Zv)
    PZ = (A * Decimal(math.exp(-alpha * z))) ** 2 / (Decimal(2) * Zv)
    z1 = math.log(m) / alpha

    print("Вычисления для задачи 2:")
    print("tgdelta =", tgdelta)
    print("alpha =", alpha)
    print("beta =", beta)
    print("lambda =", lmbd)
    print("vf =", vf)
    print("Zv =", Zv)
    print("delta =", delta)
    print("jprm0 =", jprm0)
    print("jprm =", jprm)
    print("jcmm0 =", jcmm0)
    print("jcmm =", jcmm)
    print("P0 =", P0)
    print("PZ =", PZ)
    print("z1 =", z1)


