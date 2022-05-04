# Beat Saber score curve creator

Small script to create curves by fitting given functions to some preset points (only in the 90 - 100% accuracy range atm). The idea of this tool is to make curve generation as quick as possible to iterate through different fit points. It should also make it fairly easy to iterate through different function types, as you would only need to change the function `curve` and the start values of the fit in main.py.

### Requirements
 - Python
 - lmfit (https://lmfit.github.io/lmfit-py/)

## Usage

You can run the script via
```
$ python main.py
```
It will then ask you for y values at given points x (It prints the values for the DuhRamen curve for reference). Press enter to use the DuhRamen reference points for fitting. You can enter up to 3 curves per session. After this it will output the fit report from lmfit and then show a plot of the generated curve(s) along with fern curve and DuhRamen curve.
If you get too crazy with input values the curve fitting goes wild so best be careful.
