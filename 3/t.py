with open("t", "r") as f:
    o = f.read().strip().split("\n")
    x = list(map(list, zip(*o)))
    #gamma = int("".join([max(set(r), key=r.count) for r in x]), 2)
    #epsilon = int("".join([min(set(r), key=r.count) for r in x]), 2)
    #print(gamma*epsilon)

    co2 = int("".join([[r for r in o if r[j] == max(set(r), key=r.count)] for j in range(len(o[0]))]), 2)
    oxy = int("".join([[r for r in o if r[j] == min(set(r), key=r.count)] for j in range(len(o[0]))]), 2)
    print(co2, oxy)
    print(co2*oxy)

    f.close()
