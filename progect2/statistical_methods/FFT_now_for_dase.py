def fft(n, lenght):  # leght = len(n), n - массив данных, по длине кратный степени двойки
    answer = []
    if len(n) >= 2:
        S0 = fft([n[2*i] for i in range(round(len(n) / 2))])
        S1 = fft([n[2*i + 1] for i in range(round(len(n) / 2))])
        answer += [S0[k] + math.e ** (-1j * 2 * math.pi * k / lenght) * S1[k] for k in range(round(len(n) / 2))]
        answer += [S0[k] - math.e ** (-1j * 2 * math.pi * k / lenght) * S1[k] for k in range(round(len(n) / 2))]
        return answer
    else:
        # k  = 0
        return [n[0]]
