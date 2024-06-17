import math
import numpy as np


c = 3 * 10 ** 8
eps_0 = 8.85 * 10 ** (-12)
mu_0 = 4 * math.pi * 10 ** (-7)
E_prob = 3 * 10 ** 6
f_min_after = 0
f_max_after = 0
band_width_min_after = 0
band_width_max_after = 0
def solve_task4():
    a = float(input("Введите радиус a в см: "))
    a = a / 100
    f = float(input("Введите частоту f в ГГц: "))
    f = f * (10**9)
    k_sh=float(input("Введите коэффициент шероховатости "))
    sigma=float(input("Введите Сигму "))
    prymoy(a,f,k_sh,sigma)
    krugliy(a,f,k_sh,sigma)
def prymoy(a,f,k_sh,sigma):


    b = a / 2.1
    f_min = c / (2 * a)
    f_max = c / a

    band_width_min = 1.25 * c / (2 * a)
    band_width_max = 1.98 * c / (2* a)
    if f >= f_min and f <= f_max:
        print("Частота входит в диапазон рабочих частот.")
    else:
        a_optimal = (0.63 * c) / f
        a_optimal2 = (0.99 * c) / f
        a_optimal = (a_optimal + a_optimal2) / 2
        f_min_after = c / (2 * a_optimal)
        f_max_after = c / a_optimal
        band_width_min_after = 1.25 * c / (2 * a_optimal)
        band_width_max_after = 1.98 * c / (2 * a_optimal)
        b_optimal=a_optimal/2.1

    f_cr = band_width_min if band_width_min_after==0 else band_width_min_after
    aperture = (1 - (f_cr / f)**2)**0.5

    vg = c * aperture

    vp = c / aperture

    beta = aperture * 2 * math.pi * f / c

    wavelength = c / f

    lambda_v = wavelength / aperture
    Z_v = 120 * math.pi / aperture
    delta = 1 / math.sqrt((math.pi * f * sigma * mu_0))
    k = 2 * math.pi / wavelength
    a_pr = ((k_sh * k * delta) / b_optimal) * ((1 / aperture) * ((1 / 2) + b_optimal/a_optimal * (f_cr**2/f**2)))
    P = ((a_optimal * b_optimal) / 4) * (aperture / Z_v) * E_prob**2

    print("Прямоугольный волновод")
    print("a:", a_optimal)
    print("b:", b_optimal)
    print("Левый диапазон частот одномодового режима:", f_min)
    print("Правый диапазон частот одномодового режима:", f_max)
    print("Левый диапазон частот одномодового режима оптимального волновода:", f_min_after)
    print("Правый диапазон частот одномодового режима оптимального волновода:", f_max_after)
    print("Левый диапазон полосы рабочих частот:", band_width_min)
    print("Правый диапазон полосы рабочих частот:", band_width_max)
    print("Левый диапазон полосы рабочих частот оптимального волновода:", band_width_min_after)
    print("Правый диапазон полосы рабочих частот оптимального волновода", band_width_max_after)
    print("Критическая частота:", f_cr)
    print("Апертура волновода:", aperture)
    print("Групповая скорость:", vg)
    print("Фазовая скорость:", vp)
    print("Коэффициент фазы:", beta)
    print("Длина волны:", wavelength)
    print("Длина волны в волноводе:", lambda_v)
    print("Волновое сопротивление:", Z_v)
    print("Толщина поверхностного слоя:", delta)
    print("Волновое число:", k)
    print("Коэффициент затухания волны типа H10:", a_pr)
    print("Предельная мощность:", P)
def krugliy(a,f,k_sh,sigma):

    b = a / 2.1
    f_min = 8.8 * 10**7 /  a
    f_max = 11.5* 10**7 /  a

    band_width_min = 10 * 10**7 /  a
    band_width_max = 11.4* 10**7 /  a
    if f >= f_min and f <= f_max:
        print("Частота входит в диапазон рабочих частот.")
    else:
        a_optimal = (10 * 10**7) / f
        a_optimal2 = (11.4 * 10**7) / f
        a_optimal = (a_optimal + a_optimal2) / 2
        f_min_after = 8.8 * 10**7 /  a_optimal
        f_max_after = 11.5* 10**7 /  a_optimal
        band_width_min_after = 10 * 10**7 / a_optimal
        band_width_max_after = 11.4 * 10**7 / a_optimal
        b_optimal=a_optimal/2.1
    f_cr = band_width_min if band_width_min_after==0 else band_width_min_after
    aperture = math.sqrt(1 - (f_cr / f)**2)

    vg = c * aperture

    vp = c / aperture

    beta = aperture * 2 * math.pi * f / c

    wavelength = c / f

    lambda_v = wavelength / aperture
    Z_v = 120 * math.pi / aperture
    delta = 1 / math.sqrt((math.pi * f * sigma * mu_0))
    k = 2 * math.pi / wavelength
    a_pr = ((k_sh * k * delta) / (2 * a_optimal * aperture)) * ((f_cr/f)**2 - (1 / (1.841**2 - 1)))
    P = 1.99 * 10**(-3) * a_optimal**2 * aperture * (120*math.pi / Z_v) * E_prob**2


    E_roots = np.array([
        [2.405, 3.832, 5.136, 6.380],
        [5.520, 7.016, 8.417, 9.761],
        [8.654, 10.173, 11.620, 13.015]
    ])

    H_roots = np.array([
        [3.832, 1.841, 3.054, 4.201],
        [7.016, 5.332, 6.705, 8.015],
        [10.174, 8.536, 9.965, 11.344]
    ])

    def calculate_frequency(root):
        return (c / (2 * np.pi * a)) * root

    def find_propagating_modes(roots, mode_type):
        propagating_modes = []
        for m in range(roots.shape[1]):
            for n in range(roots.shape[0]):
                frequency = calculate_frequency(roots[n, m])
                if frequency <= f:
                    propagating_modes.append((mode_type, m, n + 1, frequency))
        return propagating_modes

    E_propagating_modes = find_propagating_modes(E_roots, 'E')
    H_propagating_modes = find_propagating_modes(H_roots, 'H')

    print("Круглый волновод")
    print("a:", a_optimal)
    print("b:", b_optimal)
    print("Левый диапазон частот одномодового режима:", f_min)
    print("Правый диапазон частот одномодового режима:", f_max)
    print("Левый диапазон частот одномодового режима оптимального волновода:", f_min_after)
    print("Правый диапазон частот одномодового режима оптимального волновода:", f_max_after)
    print("Левый диапазон полосы рабочих частот:", band_width_min)
    print("Правый диапазон полосы рабочих частот:", band_width_max)
    print("Левый диапазон полосы рабочих частот оптимального волновода:", band_width_min_after)
    print("Правый диапазон полосы рабочих частот оптимального волновода", band_width_max_after)
    print("Критическая частота:", f_cr)
    print("Апертура волновода:", aperture)
    print("Групповая скорость:", vg)
    print("Фазовая скорость:", vp)
    print("Коэффициент фазы:", beta)
    print("Длина волны:", wavelength)
    print("Длина волны в волноводе:", lambda_v)
    print("Волновое сопротивление:", Z_v)
    print("Толщина поверхностного слоя:", delta)
    print("Волновое число:", k)
    print("Коэффициент затухания волны типа H10:", a_pr)
    print("Предельная мощность:", P)
    print("\nМоды E (m, n, частота), которые распространяются:")
    for mode in E_propagating_modes:
        print(f"E_{mode[1]}{mode[2]}: {mode[3]:.2e} Hz")

    print("\nМоды H (m, n, частота), которые распространяются:")
    for mode in H_propagating_modes:
        print(f"H_{mode[1]}{mode[2]}: {mode[3]:.2e} Hz")
