import numpy as np
import scipy.stats as si


#S = Stock Price
#K = Strike Price
#t = Time to Maturity
#r = Risk Free Rate
#vol = Asset Volatility


S = 100.00
K = 85.00
t = 0.25
r = 0.0125
vol = 0.20


d1 = (np.log(S / K) + (r + vol ** 2 / 2) * t) / (vol * np.sqrt(t))
d2 = d1 - vol * np.sqrt(t)
normal_pdf = 1 / np.sqrt(2 * np.pi) * np.exp(-d1 ** 2 / 2)


#Call option
def bsm_callprice(S,K,t,r,vol):
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * t) * si.norm.cdf(d2, 0.0, 1.0))
    return call
cpx = bsm_callprice(S,K,t,r,vol)
print("Theoretical call option price=",cpx)

#Put option
def bsm_putprice(S,K,t,r,vol):
    put = (K * np.exp(-r * t) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    return put
ppx = bsm_putprice(S,K,t,r,vol)
print("Theoretical put option price=",ppx)



#Delta call
def bsm_deltacall(S,K,t,r,vol):
    delta_call = si.norm.cdf(d1, 0.0, 1.0)
    return delta_call
dc = bsm_deltacall(S,K,t,r,vol)
print("Delta call =",dc)

#Delta put
def bsm_deltaput(S,K,t,r,vol):
    delta_put = si.norm.cdf(d1, 0.0, 1.0) - 1
    return delta_put
dp = bsm_deltaput(S,K,t,r,vol)
print("Delta put =",dp)



#Gamma
def bsm_gamma(S,K,t,r,vol):
    gamma = normal_pdf / (S * vol * np.sqrt(t))
    return gamma
g = bsm_gamma(S,K,t,r,vol)
print("Gamma =",g)



#Theta call
def bsm_thetacall(S,K,t,r,vol):
    theta_call = (-vol * S * normal_pdf) / (2 * np.sqrt(t)) - r * K * np.exp(-r * t) * si.norm.cdf(d2, 0.0, 1.0)
    return theta_call
tc = bsm_thetacall(S,K,t,r,vol)
print("Theta call =",tc)

#Theta put
def bsm_thetaput(S,K,t,r,vol):
    theta_put = (-vol * S * normal_pdf) / (2 * np.sqrt(t)) + r * K * np.exp(-r * t) * si.norm.cdf(-d2, 0.0, 1.0)
    return theta_put
tp = bsm_thetaput(S,K,t,r,vol)
print("Theta put =",tp)



#Vega
def bsm_vega(S,K,t,r,vol):
    vega = S * normal_pdf * np.sqrt(t)
    return vega
v = bsm_vega(S,K,t,r,vol)
print("Vega =",v)



#Rho call
def bsm_rhocall(S,K,t,r,vol):
    rho_call = t * K * np.exp(-r * t) * si.norm.cdf(d2, 0.0, 1.0)
    return rho_call
rc = bsm_rhocall(S,K,t,r,vol)
print("Rho call =", rc)

#Rho put
def bsm_rhoput(S,K,t,r,vol):
    rho_put = -t * K * np.exp(-r * t) * si.norm.cdf(-d2, 0.0, 1.0)
    return rho_put
rp = bsm_rhoput(S,K,t,r,vol)
print("Rho put =", rp)














                        