import mpmath

# mpmath의 임의 정밀도 부동 소수점 이란걸 사용해야 해서 불러옴
# pip install mpmath
# 적당한 순회라면 math 임포트해서 쓰면됨


def fixed_point_iteration(initial_guess, num_iterations):
    x = mpmath.mpf(initial_guess)
    for i in range(num_iterations):
        print(x)
        x = mpmath.exp(-x) - x
    return x


initial_guess = 1.0
num_iterations = 9

result = fixed_point_iteration(initial_guess, num_iterations)

print("Approximate Fixed Point:", result)


# C:\study>python tmp.py
# 1.0
# -0.632120558828558
# 2.5137169463602
# -2.43275021611185
# 13.8229146735541
# -13.8229136809308
# 1007444.4167433
# -1007444.4167433
# 3.55644302267916e+437527
# Approximate Fixed Point: -3.55644302267916e+437527
