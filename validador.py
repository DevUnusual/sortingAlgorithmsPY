def val(v):
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return False
    return True