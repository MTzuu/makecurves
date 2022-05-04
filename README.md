# Beat Saber score curve creator

Small script to create curves by fitting given functions to some preset points.

### Requirements
 - Python
 - Lmfit (https://lmfit.github.io/lmfit-py/)

## Usage

You can run the script via

$ python main.py

It will then ask you for y values at given points x (It prints the values for the DuhRamen curve for reference). Press enter to use the DuhRamen reference points for fitting. You can enter up to 3 curves per session. After this it will output the fit report from lmfit and then show a plot of the generated curve(s) along with fern curve and DuhRamen curve for reference.
