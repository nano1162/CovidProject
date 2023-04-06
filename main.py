# 개발 시작
import scipy.integrate as sci
import numpy as np 
import matplotlib.pyplot as plt
import random
from celluloid import Camera

def SIR(S ,I, R, beta, gamma, mu):   
    # beta : 감염의 효과율, S : 감염 취약자, I : 감염자 수 => 시간에 따른 감염자 수 증가율(dI/dt)이자 취약자 수 감소율
    # gamma : 감염 기간의 역수, 즉 회복률 I : 감염자 수 => 시간에 따른 회복자 수 증가율이자 감염자 수 감소율

    dsDdt = (-beta*S*I) + (mu * R) # 취약자 수 감소율
    diDdt = beta*S*I - gamma * I # 감염자 수 증가 및 감소율
    drDdt = gamma * I - (mu * R) # 회복자 수 증가율

    S1 = S + dsDdt  
    I1 = I + diDdt
    R1 = R + drDdt

    return S1, I1, R1


# 바로 아래 글은 최초 개발 당시 써놓은 글, 간단하게 논리 전개 과정만 보고 자세한 데이터는 무시 바람.

# 우리는 대한민국 전 국민을 대상으로 볼 것이기 때문에, 최초 S를 5000만, I를 2020년 3월 기준 데이터로 잡고 시작 할 것이다.
# diDdt, 즉 beta*S*I - gamma * I가 0보다 크다면 감염자는 계속 증가함. 이를 이항해서, beta*S*I > gamma * I로 식을 바꿔주고,
# 양변에서 I를 나눈 후, gamma로 나눠주면 beta * S / gamma > 1이라는 식이 된다. 이는 beta * S / gamma가 R0과 같다는 점을 시사한다.
# 코로나의 최초 자가격리 기간은 3주, 즉 21일이었다. gamma = 1 / 21, S = 1이라고 가정해 비율 관계로 보면, R0 =  beta * 21 라는 식을 얻을 수 있다.
# 2.7 = 21 * beta, beta = 27 / 210 이라는 결과값을 얻을 수 있다. 

#최초 감염자, 감염 취약자, 회복자 비율
I0 = 0.1 # 23,326,222명을 감염자로 가정하여 SIRS 그래프 제작.
S0 = 0.99
R0 = 0

#실제 인구
RealS = 1 

beta =  27 / 210 #0.0395라는 값을 SIRS 그래프 제작의 과정에서 얻어냄.
gamma = 0.05
mu = 0

fig, axes = plt.subplots(1)
camera = Camera(fig)

wrap = [[], [], []]
for i in range(300):
    wrap[0].append(S0*RealS)  # append 함수를 사용하여 각 시간에서의 값을 리스트에 추가함.
    wrap[1].append(I0*RealS)
    wrap[2].append(R0*RealS)

    core = SIR(S0, I0, R0, beta, gamma, mu)

    S0 = core[0]
    I0 = core[1]
    R0 = core[2]

    # plot 함수 대신 plot(x, y, '-o') 사용
    # 여기 아래 주석은 SIRS 그래프 그릴 때 주석처리 해제해주면 됨. 현재는 I 그래프 제작으로 주석처리 되어 있음.

    # axes.plot(range(i+1), wrap[0], '-o', markersize = 1, color = 'r') 
    axes.plot(range(i+1), wrap[1], '-o', markersize = 1, color = 'g')
    # axes.plot(range(i+1), wrap[2], '-o', markersize = 1, color = 'b')

    # axes.text(i, wrap[0][i], f'Sus {wrap[0][i]:.2f}')
    axes.text(i, wrap[1][i], f'Inf {wrap[1][i]:.2f}')
    # axes.text(i, wrap[2][i], f'Res {wrap[2][i]:.2f}')

    camera.snap()

animation = camera.animate(interval=10)

# 이름 설정하기
animation.save( 'R083Mu966.gif', writer = 'ffmpef', fps = 20)