def float_to_time(value):
    if value >= 0.0:
        ivalue = int(value)
        return "%02d:%02d" % (ivalue, (value - ivalue) * 60)
    else:
        value = abs(value)
        ivalue = int(value)
        return "-%02d:%02d" % (ivalue, (value - ivalue) * 60)