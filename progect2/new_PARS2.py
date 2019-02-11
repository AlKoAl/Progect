"""N3 - индекс напряжения Баевского"""  
  def PARS():

        def N1(x):
            if x <= 660:
                return 2
            elif x <= 800:
                return 1
            elif x < 1000:
                return 0
            elif 1200 >= x >= 1000:
                return abs(-1)
            elif x > 1200:
                return abs(-2)

        def N2(x):
            if x <= 20:
                return 2
            elif x <= 40:
                return 1
            elif x >= 100:
                return abs(-2)
            elif x >= 80:
                return abs(-1)
            else:
                return 0

        def N3(x):
            if x >= 500:
                return 2
            elif x >= 200:
                return 1
            elif x <= 25:
                return abs(-2)
            elif x <= 50:
                return abs(-1)
            else:
                return 0

        def N4(x):
            if x <= 15:
                return abs(-2)
            if x <= 25:
                return abs(-1)
            if x >= 43:
                return 2
            if x >= 35:
                return 1
            else:
                return 0

        def N5(x):
            if x <= 10:
                return abs(-2)
            elif x <= 15:
                return abs(-1)
            elif x >= 40:
                return 2
            elif x >= 30:
                return 1
            else:
                return 0

        return list((mean()*1000, SDNN()*1000, tension_index(),
                         norm(fft_res)[1], norm(fft_res)[0]))
    return PARS()
