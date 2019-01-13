def dispersion():
    dispersion = 0
    for i in range(1, len(points)):
        dispersion += integrate(x ** 2 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                                (x, points[i - 1][0], points[i][0]))
    dispersion -= expvalue ** 2
    return dispersion
