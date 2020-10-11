rows = int(input("How many rows? "))

def pascal(var) :
    if var == 0 :
        print([1])
        return [1]

    else :
        l = [1]
        p = pascal(var - 1)

        for i in range(len(p) - 1):
            l.append(p[i] + p[i + 1])

        l += [1]
    print(l)
    return l


pascal(rows)