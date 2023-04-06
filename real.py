# 만들다 말았음, main.py가 사용된 파일



import numpy as np
import matplotlib.pyplot as plt

S = 10000000
I = 10
R = 0
N = S + I + R

beta = 0.0835  # 전파율
gamma = 0.05  # 치유율
mu = 0.01  # 회복자가 민감해지는 속도
def SIR(S ,I, R, beta, gamma, mu):
    dSdt = (-beta * S * I ) + (mu * R)
    dIdt = (beta * S * I ) - (gamma * I)
    dRdt = (gamma * I) - (mu * R)

# 시뮬레이션 설정
t = np.linspace(0, 365, 365)
S_data = []
I_data = []
R_data = []

# 초기값 설정
S_data.append(S)
I_data.append(I)
R_data.append(R)

# 시뮬레이션 실행
for i in range(1, len(t)):
    # 업데이트
    S += dSdt
    I += dIdt
    R += dRdt
    # 값 저장
    S_data.append(S)
    I_data.append(I)
    R_data.append(R)

# 결과 시각화
plt.plot(t, S_data, label='Susceptible')
plt.plot(t, I_data, label='Infected')
plt.plot(t, R_data, label='Recovered')
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Number of People')
plt.show()