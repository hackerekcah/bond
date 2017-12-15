
def calc_p0(p1, c, ytm, n, t):
    '''
        p0 = c*p1 / (1+ytm)^t + c*p1 / (1+ytm)^(t+1) +.... + c*p1 / (1+ytm)^(t+n) + p1 / (1+ytm)^(t+n)
    '''

    p0 = 0

    for year in range(0,n+1):
        if t == 0 and 0 == year:
            continue
        p0 += c*p1 / pow(1+ytm, t+year)

    p0 += p1 / pow(1+ytm, t+n)

    return round(p0,3)


def calc_p1(p0, c, ytm, n, t):
    """
    p1 = p0 / (c / (1+ytm)^t + c / (1+ytm)^(t+1) +.... + c / (1+ytm)^(t+n) + 1 / (1+ytm)^(t+n))

    """

    alpha = 1 / pow(1+ytm, t+n)
    for year in range(0, n+1):
        if t == 0 and 0 == year:
            continue
        alpha += c / pow(1+ytm, t+year)

    p1 = p0 / alpha

    return round(p1,3)

def calc_c(p0, p1, ytm, n, t):
    """
    c = (p0/p1 - 1 / (1+ytm)^(t+n)) / (1 / (1+ytm)^t + 1 / (1+ytm)^(t+1) +.... + 1 / (1+ytm)^(t+n))
    """

    numrator = float(p0)/p1 - 1 / pow(1+ytm, t+n)
    denumrator = 0
    for year in range(0, n+1):
        if t == 0 and 0 == year:
            continue
        denumrator += 1 / pow(1+ytm, t+year)

    c = numrator / denumrator
    return round(c,5)


def calc_ytm(p0, p1, n, c, t):

    #initialize to coupon rate and adjust gradually
    ytm = c

    p0_tolerance = 1e-2
    lr = 1e-6

    while True:

        p0_est = calc_p0(p1, c, ytm, n, t)

        if p0_est - p0 > p0_tolerance:
            # should increase ytm
            ytm += lr
            print "p0_est is %3.1f, ytm is %3.2f" % (p0_est, ytm*100)
        elif p0 - p0_est > p0_tolerance:
            # should decrease ytm
            ytm -= lr
            print "p0_est is %3.1f, ytm is %3.2f" % (p0_est, ytm*100)
        else:
            print "Finally p0_est is %3.1f, ytm is %3.2f" % (p0_est, ytm*100)
            break

    return round(ytm,5)


