import textwrap

def query_yes_no(question, default='yes'):
    valid = {"yes" : True, "y": True, "no" : False, "n" : False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        choice = input(question + prompt)
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print('Please respond with "yes" or "no" ("y", "n").\n')

def query_values(question, default):
    prompt = ' [f(' + str(default[0]) + ') = ' + str(default[1]) + '] '
    while True:
        value = input(question + prompt)
        if value == '':
            return default
        else:
            try:
                value = float(value)
                return [default[0], value]
            except:
                print('Please enter a valid float value. \n')

def query_points(DuhCurve):
    fitpoints = []

    for points in DuhCurve:
        fitpoints.append(query_values('f(x) = y', points))

    return fitpoints
