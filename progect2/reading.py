import wfdb
annotation2 = wfdb.rdann('I13', 'atr', pb_dir='incartdb')
qrs_locs = []
i, j = 0, 0
while annotation2.fs * 300 > annotation2.sample[j]:
    # вычисляем в пятиминутном интервале RR-интервалы
    if annotation2.symbol[j] in ['N', 'L', 'R', 'B', 'A', 'a', 'J', 'S', 'V', 'r', 'F', 'e', 'j', 'n', 'E', 'f', 'Q']:
        qrs_locs.append(annotation2.sample[i])
    i, j = i + 1, j + 1
rr_intervals = []
for i, j in zip(qrs_locs[1:], qrs_locs):
    rr_intervals.append(round((i - j)/annotation2.fs, 3))
print(rr_intervals)
