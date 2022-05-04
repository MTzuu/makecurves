import numpy as np
import matplotlib.pyplot as plt
import lmfit
from curve import *
from query import *

def curve(x, x1, b1, b2, c1, c2, d1):
    y = np.piecewise(
            x,
            [x <= x1, x > x1],
            [
                lambda x: np.power((b2-0.95)/(b2-x), c2),
                lambda x: np.power((b2-0.95)/(b2-x1), c2)*np.power((b1-x1)/(b1-x), c1)*np.exp(d1*(x-x1))
                ])
    return y

def fit(fitpoints):
    x = fitpoints[:, 0]
    y = fitpoints[:, 1]
    curvemodel = lmfit.Model(curve)
    params = curvemodel.make_params()
    params.add('delta', value = 0.15, min = 0.005)
    params.add('c1', value = 0.90, min = 0.2)
    params.add('c2', value = 1)
    params.add('x1', value = 0.925, min=0.9, max=0.99)
    params.add('b1', value = 1.01, min = 1.000001)
    params.add('b2', expr = 'delta + x1')
    params.add('d1', expr = 'c2/(b2-x1) - c1/(b1-x1)')
        
    result = curvemodel.fit(y, x=x, params=params)

    print(result.fit_report())

    return result

def main():
    x = np.array([0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.955, 0.96, 0.965, 0.97, 0.9733, 0.9766, 0.98, 0.9825, 0.985, 0.9875, 0.99])
    curve_colors = ['blue', 'green', 'black']

    print("You'll now be prompted to enter y values for given x values so that the generated curve goes through f(x) = y\n(This also prints the values of DuhHelloRamen Curve for reference) \n")

    FitDict = {}
    askAgain = True
    i = 0

    while askAgain and i < 3:
        fitpoints = np.array(query_points(DuhFit))
        FitDict[str(i)] = fitpoints
        askAgain = query_yes_no("Do you want to add another curve? (currently supports up to 3 curves at a time)", default = 'no')
        i += 1

    for number, points in FitDict.items():
        result = fit(points)
        params = list(result.params.valuesdict().values())[:-1]
        plt.plot(x, curve(x, *params), marker = 'None', color = curve_colors[int(number)], linewidth = 1)
        plt.plot(points[:-1, 0], points[:-1, 1], marker = '+', linestyle = 'None', color = curve_colors[int(number)], markersize = 10, label = 'Fit Points for Curve ' + number)
    
    plt.plot(DuhCurve[8:26, 0], DuhCurve[8:26, 1], marker = 'None', color = 'red', linewidth=1, label = 'DuhHelRamen')
    plt.plot(OldCurve[1:9, 0], OldCurve[1:9, 1], marker = 'None', color = 'orange', linewidth=1, label = 'Old Curve')
    plt.legend(loc = 'upper left')

    plt.show()

if __name__ == '__main__':
    main()
