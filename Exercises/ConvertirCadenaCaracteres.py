import re
t = "La 1 - en  + la () de su LYA1 con el LYA1 final 3 5 puntos MO"
nc = re.sub(r"\b1\b", "primera", t)
nc = re.sub(r"-", "persona", nc)
nc = re.sub(r"\+", "mandarme", nc)
nc = re.sub(r"\(\s*\)", "foto", nc)
nc = re.sub(r"LYA1", "programa", nc)
nc = re.sub(r"\b3\b", "obtiene", nc)
nc = re.sub(r"\bMO\b", "extra", nc)
print(nc)
