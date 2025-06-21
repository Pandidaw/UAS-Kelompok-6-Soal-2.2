import sys
sys.stdout.reconfigure(encoding='utf-8')

facts = {
    "M": True,   # Gerakan
    "D": False,  # Pintu terbuka
    "W": False,  # Jendela terbuka
    "N": True,   # Rumah kosong
    "S": True,   # Suara
    "T": False,  # Tekanan
    "L": False,  # Malam
}

rules = [
    (["M", "N"], "V"),
    (["D", "N"], "V"),
    (["W", "N"], "V"),
    (["V", "S"], "A"),
    (["T", "N"], "A"),
    (["M", "S", "N"], "A"),
    (["A"], "K"),
    (["V", "L", "N"], "A"),
]

def forward_chain(facts, rules):
    new_inferred = True
    while new_inferred:
        new_inferred = False
        for conditions, conclusion in rules:
            if conclusion not in facts:
                if all(facts.get(cond, False) for cond in conditions):
                    print(f"Inferensi: {conditions} → {conclusion}")
                    facts[conclusion] = True
                    new_inferred = True
    return facts

result = forward_chain(facts.copy(), rules)
print("\nStatus akhir:")
for k, v in result.items():
    print(f"{k} = {v}")