# ---------Park-----------
PRK = 370, 345, 1502
# --------Tasadof--------
TSDF = 4500, 8700, 3600, 112, 9871
# ---------Commend--------
CMND = 120, 450, 36, 25, 0
# --------Call-----------
CLL = 1700, 550, 3300
# --------Careless-------
CRLS = 1200, 780, 666, 981, 325, 102
# -------Car Mirrors-----
CRMRRS = 784, 1350, 1298, 10, 32, 1, 87
# ---------Car Door------
CRDR = 450, 320
# ---------Lamp Door-----
LMPDR = 15780, 150, 345, 125, 998
# ---------rubber---------
RBR = 130, 48, 50, 22
# ---------brak-----------
BRK = 140, 360, 52, 48, 97


Jarime = {
    "Park": PRK,
    "Tasadof": TSDF,
    "Commend": CMND,
    "Call": CLL,
    "Careless": CRLS,
    "Car-Mirrors": CRMRRS,
    "Car-Door": CRDR,
    "Rubber": RBR,
    "Brak": BRK

}
for key, value in Jarime.items():

    print(
        f"Tedad Takhalof Shoma: {len(Jarime)} But in {key} {len(value)} -- money: {sum(value)} ")
