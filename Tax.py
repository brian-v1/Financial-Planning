### Federal Tax 2019

fed_rate_1 = 0.15
fed_rate_2 = 0.205
fed_rate_3 = 0.26
fed_rate_4 = 0.29
fed_rate_5 = 0.33
fed_income_1 = 47630
fed_income_2 = 95259
fed_income_3 = 147667
fed_income_4 = 210371
fed_tax_1 = fed_rate_1 * fed_income_1
fed_tax_2 = fed_rate_2 * (fed_income_2 - fed_income_1)
fed_tax_3 = fed_rate_3 * (fed_income_3 - fed_income_2)
fed_tax_4 = fed_rate_4 * (fed_income_4 - fed_income_3)

def fed_tax(income):
  if income > fed_income_4:
    return (income - fed_income_4) * fed_rate_5 + fed_tax_1 + fed_tax_2 + fed_tax_3 + fed_tax_4
  elif income > fed_income_3:
    return (income - fed_income_3) * fed_rate_4 + fed_tax_1 + fed_tax_2 + fed_tax_3
  elif income > fed_income_2:
    return (income - fed_income_2) * fed_rate_3 + fed_tax_1 + fed_tax_2
  elif income > fed_income_1:
    return (income - fed_income_1) * fed_rate_2 + fed_tax_1
  else:
    return income * fed_rate_1



### Provincial Tax Ontario 2019

on_rate_1 = 0.0505
on_rate_2 = 0.0915
on_rate_3 = 0.1116
on_rate_4 = 0.1216
on_rate_5 = 0.1316
on_income_1 = 43906
on_income_2 = 87813
on_income_3 = 150000
on_income_4 = 220000
on_tax_1 = on_rate_1 * on_income_1
on_tax_2 = on_rate_2 * (on_income_2 - on_income_1)
on_tax_3 = on_rate_3 * (on_income_3 - on_income_2)
on_tax_4 = on_rate_4 * (on_income_4 - on_income_3)

def on_tax(income):
  if income > on_income_4:
    return (income - on_income_4) * on_rate_5 + on_tax_1 + on_tax_2 + on_tax_3 + on_tax_4
  elif income > on_income_3:
    return (income - on_income_3) * on_rate_4 + on_tax_1 + on_tax_2 + on_tax_3
  elif income > on_income_2:
    return (income - on_income_2) * on_rate_3 + on_tax_1 + on_tax_2
  elif income > on_income_1:
    return (income - on_income_1) * on_rate_2 + on_tax_1
  else:
    return income * on_rate_1



### Provincial Tax Newfoundland and Labrador 2019

nl_rate_1 = 0.087
nl_rate_2 = 0.145
nl_rate_3 = 0.158
nl_rate_4 = 0.173
nl_rate_5 = 0.183
nl_income_1 = 37591
nl_income_2 = 75181
nl_income_3 = 134224
nl_income_4 = 187913
nl_tax_1 = nl_rate_1 * nl_income_1
nl_tax_2 = nl_rate_2 * (nl_income_2 - nl_income_1)
nl_tax_3 = nl_rate_3 * (nl_income_3 - nl_income_2)
nl_tax_4 = nl_rate_4 * (nl_income_4 - nl_income_3)

def nl_tax(income):
  if income > nl_income_4:
    return (income - nl_income_4) * nl_rate_5 + nl_tax_1 + nl_tax_2 + nl_tax_3 + nl_tax_4
  elif income > nl_income_3:
    return (income - nl_income_3) * nl_rate_4 + nl_tax_1 + nl_tax_2 + nl_tax_3
  elif income > nl_income_2:
    return (income - nl_income_2) * nl_rate_3 + nl_tax_1 + nl_tax_2
  elif income > nl_income_1:
    return (income - nl_income_1) * nl_rate_2 + nl_tax_1
  else:
    return income * nl_rate_1



### Provincial Tax Prince Edward Island 2019

pe_rate_1 = 0.098
pe_rate_2 = 0.138
pe_rate_3 = 0.167
pe_income_1 = 31984
pe_income_2 = 63969
pe_tax_1 = pe_rate_1 * pe_income_1
pe_tax_2 = pe_rate_2 * (pe_income_2 - pe_income_1)

def pe_tax(income):
  if income > pe_income_2:
    return (income - pe_income_2) * pe_rate_3 + pe_tax_1 + pe_tax_2
  elif income > pe_income_1:
    return (income - pe_income_1) * pe_rate_2 + pe_tax_1
  else:
    return income * pe_rate_1



### Provincial Tax Nova Scotia 2019

ns_rate_1 = 0.0879
ns_rate_2 = 0.1495
ns_rate_3 = 0.1667
ns_rate_4 = 0.1750
ns_rate_5 = 0.21
ns_income_1 = 29590
ns_income_2 = 59180
ns_income_3 = 93000
ns_income_4 = 150000
ns_tax_1 = ns_rate_1 * ns_income_1
ns_tax_2 = ns_rate_2 * (ns_income_2 - ns_income_1)
ns_tax_3 = ns_rate_3 * (ns_income_3 - ns_income_2)
ns_tax_4 = ns_rate_4 * (ns_income_4 - ns_income_3)

def ns_tax(income):
  if income > ns_income_4:
    return (income - ns_income_4) * ns_rate_5 + ns_tax_1 + ns_tax_2 + ns_tax_3 + ns_tax_4
  elif income > ns_income_3:
    return (income - ns_income_3) * ns_rate_4 + ns_tax_1 + ns_tax_2 + ns_tax_3
  elif income > ns_income_2:
    return (income - ns_income_2) * ns_rate_3 + ns_tax_1 + ns_tax_2
  elif income > ns_income_1:
    return (income - ns_income_1) * ns_rate_2 + ns_tax_1
  else:
    return income * ns_rate_1



### Provincial Tax New Brunswick 2019

nb_rate_1 = 0.0968
nb_rate_2 = 0.1482
nb_rate_3 = 0.1652
nb_rate_4 = 0.1782
nb_rate_5 = 0.203
nb_income_1 = 42592
nb_income_2 = 85184
nb_income_3 = 138491
nb_income_4 = 157778
nb_tax_1 = nb_rate_1 * nb_income_1
nb_tax_2 = nb_rate_2 * (nb_income_2 - nb_income_1)
nb_tax_3 = nb_rate_3 * (nb_income_3 - nb_income_2)
nb_tax_4 = nb_rate_4 * (nb_income_4 - nb_income_3)

def nb_tax(income):
  if income > nb_income_4:
    return (income - nb_income_4) * nb_rate_5 + nb_tax_1 + nb_tax_2 + nb_tax_3 + nb_tax_4
  elif income > nb_income_3:
    return (income - nb_income_3) * nb_rate_4 + nb_tax_1 + nb_tax_2 + nb_tax_3
  elif income > nb_income_2:
    return (income - nb_income_2) * nb_rate_3 + nb_tax_1 + nb_tax_2
  elif income > nb_income_1:
    return (income - nb_income_1) * nb_rate_2 + nb_tax_1
  else:
    return income * nb_rate_1




### Provincial Tax Quebec 2019

qc_rate_1 = 0.15
qc_rate_2 = 0.20
qc_rate_3 = 0.24
qc_rate_4 = 0.2575
qc_income_1 = 43790
qc_income_2 = 87575
qc_income_3 = 106555
qc_tax_1 = qc_rate_1 * qc_income_1
qc_tax_2 = qc_rate_2 * (qc_income_2 - qc_income_1)
qc_tax_3 = qc_rate_3 * (qc_income_3 - qc_income_2)

def qc_tax(income):
  if income > qc_income_3:
    return (income - qc_income_3) * qc_rate_4 + qc_tax_1 + qc_tax_2 + qc_tax_3
  elif income > qc_income_2:
    return (income - qc_income_2) * qc_rate_3 + qc_tax_1 + qc_tax_2
  elif income > qc_income_1:
    return (income - qc_income_1) * qc_rate_2 + qc_tax_1
  else:
    return income * qc_rate_1



### Provincial Tax Manitoba 2019

mb_rate_1 = 0.108
mb_rate_2 = 0.1275
mb_rate_3 = 0.174
mb_income_1 = 32670
mb_income_2 = 70610
mb_tax_1 = mb_rate_1 * mb_income_1
mb_tax_2 = mb_rate_2 * (mb_income_2 - mb_income_1)

def mb_tax(income):
  if income > mb_income_2:
    return (income - mb_income_2) * mb_rate_3 + mb_tax_1 + mb_tax_2
  elif income > mb_income_1:
    return (income - mb_income_1) * mb_rate_2 + mb_tax_1
  else:
    return income * mb_rate_1



### Provincial Tax Saskatchewan 2019

sk_rate_1 = 0.105
sk_rate_2 = 0.125
sk_rate_3 = 0.145
sk_income_1 = 45225
sk_income_2 = 129214
sk_tax_1 = sk_rate_1 * sk_income_1
sk_tax_2 = sk_rate_2 * (sk_income_2 - sk_income_1)

def sk_tax(income):
  if income > sk_income_2:
    return (income - sk_income_2) * sk_rate_3 + sk_tax_1 + sk_tax_2
  elif income > sk_income_1:
    return (income - sk_income_1) * sk_rate_2 + sk_tax_1
  else:
    return income * sk_rate_1




### Provincial Tax Alberta 2019

ab_rate_1 = 0.1
ab_rate_2 = 0.12
ab_rate_3 = 0.13
ab_rate_4 = 0.14
ab_rate_5 = 0.15
ab_income_1 = 131220
ab_income_2 = 157464
ab_income_3 = 209952
ab_income_4 = 314928
ab_tax_1 = ab_rate_1 * ab_income_1
ab_tax_2 = ab_rate_2 * (ab_income_2 - ab_income_1)
ab_tax_3 = ab_rate_3 * (ab_income_3 - ab_income_2)
ab_tax_4 = ab_rate_4 * (ab_income_4 - ab_income_3)

def ab_tax(income):
  if income > ab_income_4:
    return (income - ab_income_4) * ab_rate_5 + ab_tax_1 + ab_tax_2 + ab_tax_3 + ab_tax_4
  elif income > ab_income_3:
    return (income - ab_income_3) * ab_rate_4 + ab_tax_1 + ab_tax_2 + ab_tax_3
  elif income > ab_income_2:
    return (income - ab_income_2) * ab_rate_3 + ab_tax_1 + ab_tax_2
  elif income > ab_income_1:
    return (income - ab_income_1) * ab_rate_2 + ab_tax_1
  else:
    return income * ab_rate_1




### Provincial Tax British Columbia 2019

bc_rate_1 = 0.0506
bc_rate_2 = 0.077
bc_rate_3 = 0.105
bc_rate_4 = 0.1229
bc_rate_5 = 0.147
bc_rate_6 = 0.168
bc_income_1 = 40707
bc_income_2 = 81416
bc_income_3 = 93476
bc_income_4 = 113506
bc_income_5 = 153900
bc_tax_1 = bc_rate_1 * bc_income_1
bc_tax_2 = bc_rate_2 * (bc_income_2 - bc_income_1)
bc_tax_3 = bc_rate_3 * (bc_income_3 - bc_income_2)
bc_tax_4 = bc_rate_4 * (bc_income_4 - bc_income_3)
bc_tax_5 = bc_rate_5 * (bc_income_5 - bc_income_4)

def bc_tax(income):
  if income > bc_income_5:
    return (income - bc_income_5) * bc_rate_6 + bc_tax_1 + bc_tax_2 + bc_tax_3 + bc_tax_4 + bc_tax_5
  elif income > bc_income_4:
    return (income - bc_income_4) * bc_rate_5 + bc_tax_1 + bc_tax_2 + bc_tax_3 + bc_tax_4
  elif income > bc_income_3:
    return (income - bc_income_3) * bc_rate_4 + bc_tax_1 + bc_tax_2 + bc_tax_3
  elif income > bc_income_2:
    return (income - bc_income_2) * bc_rate_3 + bc_tax_1 + bc_tax_2
  elif income > bc_income_1:
    return (income - bc_income_1) * bc_rate_2 + bc_tax_1
  else:
    return income * bc_rate_1




### Provincial Tax Yukon 2019

yt_rate_1 = 0.064
yt_rate_2 = 0.09
yt_rate_3 = 0.109
yt_rate_4 = 0.128
yt_rate_5 = 0.15
yt_income_1 = 47630
yt_income_2 = 95259
yt_income_3 = 147667
yt_income_4 = 500000
yt_tax_1 = yt_rate_1 * yt_income_1
yt_tax_2 = yt_rate_2 * (yt_income_2 - yt_income_1)
yt_tax_3 = yt_rate_3 * (yt_income_3 - yt_income_2)
yt_tax_4 = yt_rate_4 * (yt_income_4 - yt_income_3)

def yt_tax(income):
  if income > yt_income_4:
    return (income - yt_income_4) * yt_rate_5 + yt_tax_1 + yt_tax_2 + yt_tax_3 + yt_tax_4
  elif income > yt_income_3:
    return (income - yt_income_3) * yt_rate_4 + yt_tax_1 + yt_tax_2 + yt_tax_3
  elif income > yt_income_2:
    return (income - yt_income_2) * yt_rate_3 + yt_tax_1 + yt_tax_2
  elif income > yt_income_1:
    return (income - yt_income_1) * yt_rate_2 + yt_tax_1
  else:
    return income * yt_rate_1




### Provincial Tax Northwest Territories 2019

nt_rate_1 = 0.059
nt_rate_2 = 0.086
nt_rate_3 = 0.122
nt_rate_4 = 0.1405
nt_income_1 = 43137
nt_income_2 = 86277
nt_income_3 = 140267
nt_tax_1 = nt_rate_1 * nt_income_1
nt_tax_2 = nt_rate_2 * (nt_income_2 - nt_income_1)
nt_tax_3 = nt_rate_3 * (nt_income_3 - nt_income_2)

def nt_tax(income):
  if income > nt_income_3:
    return (income - nt_income_3) * nt_rate_4 + nt_tax_1 + nt_tax_2 + nt_tax_3
  elif income > nt_income_2:
    return (income - nt_income_2) * nt_rate_3 + nt_tax_1 + nt_tax_2
  elif income > nt_income_1:
    return (income - nt_income_1) * nt_rate_2 + nt_tax_1
  else:
    return income * nt_rate_1



### Provincial Tax Nunavut 2019

nu_rate_1 = 0.04
nu_rate_2 = 0.07
nu_rate_3 = 0.09
nu_rate_4 = 0.115
nu_income_1 = 45414
nu_income_2 = 90829
nu_income_3 = 147667
nu_tax_1 = nu_rate_1 * nu_income_1
nu_tax_2 = nu_rate_2 * (nu_income_2 - nu_income_1)
nu_tax_3 = nu_rate_3 * (nu_income_3 - nu_income_2)

def nu_tax(income):
  if income > nu_income_3:
    return (income - nu_income_3) * nu_rate_4 + nu_tax_1 + nu_tax_2 + nu_tax_3
  elif income > nu_income_2:
    return (income - nu_income_2) * nu_rate_3 + nu_tax_1 + nu_tax_2
  elif income > nu_income_1:
    return (income - nu_income_1) * nu_rate_2 + nu_tax_1
  else:
    return income * nu_rate_1



### Form import from HTML

import cgi, cgitb
form = cgi.FieldStorage()
province = form.getvalue("province")
income = form.getvalue("income")



### Tax Calculation

prov_list = ["Ontario", "Newfoundland and Labrador", "Prince Edward Island", "Nova Scotia", "New Brunswick", "Quebec", "Manitoba", "Saskatchewan", "Alberta", "British Columbia", "Yukon", "Northwest Territories", "Nunavut"]

prov_tax_list = [on_tax(income), nl_tax(income), pe_tax(income), ns_tax(income), nb_tax(income), qc_tax(income), mb_tax(income), sk_tax(income), ab_tax(income), bc_tax(income), yt_tax(income), nt_tax(income), nt_tax(income)]

prov_index = prov_list.index(province)

fed_tax = fed_tax(income)
prov_tax = prov_tax_list[prov_index]
total_tax = fed_tax + prov_tax



### Form Output to HTML
print "Content-type:text/html\r\n\r\n"
print("<html>")
print("<head>")
print("<title>Personal Tax Calculator</title>")
print("</head>")
print("<body>")
print ("<h2> Your personal income is %s</h2>" % total_tax)
print("</body>")
print("</html>")




