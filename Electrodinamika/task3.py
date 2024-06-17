from math import degrees, radians, asin, atan, sqrt, sin, cos, tan
def solve_task3():
    epsilon = float(input("Введите значение эпсилон: "))

    angle_brewster_rad = atan(sqrt(1 / epsilon))
    angle_brewster = degrees(angle_brewster_rad)
    print(f"Угол Брюстера: {angle_brewster} градусов ({angle_brewster_rad} рад)")

    critical_angle_rad = asin(sqrt(1 / epsilon))
    critical_angle = degrees(critical_angle_rad)
    print(f"Критический угол: {critical_angle} градусов ({critical_angle_rad} рад)")


