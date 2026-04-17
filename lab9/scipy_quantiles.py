from scipy.stats import norm, chi2, t

alpha = 0.05

df = 10

q1 = norm.ppf(1 - alpha)
q2 = chi2.ppf(1 - alpha, df)
q3 = t.ppf(1 - alpha, df)

print(q1)
print(q2)
print(q3)