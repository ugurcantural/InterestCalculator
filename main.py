print("......................................................")
print(".*.*.*.*.*Welcome to the Interest Calculator*.*.*.*.*.")
print("......................................................")

isim = str(input("Please enter your name: "))
kredi_tutari = float(input("Loan Amount: "))
faiz_orani = float(input("Interest Rate (per year): "))

print("->TIME LENGTH")

max_yil = int(input("    Loan term in years: "))
max_ay = int(input("    Loan term in months: "))
yineleme = int(input("    İteration in months: "))


def duration(toplamay):
    if (toplamay == 0):
        return max_ay
    else:
        return (max_yil * 12) + max_ay


def money(para):
    print(str(round(para, 1)) + "$")


aygoster = 0
yilgoster = 0

print("\nReport For " + isim)
i = yineleme
while i <= duration(max_ay):
    print("----------------------------")
    toplamfaiz = (kredi_tutari / 100) * (faiz_orani / 12) * i
    toplamtutar = kredi_tutari + toplamfaiz
    aylıkodeme = toplamtutar / i

    if i < 12:
        aygoster = i
        print("Year: " + str(yilgoster))
        print("Month: " + str(aygoster))
    elif i >= 12:
        if i % 12 == 0:
            yilgoster += 1
        aygoster = i - (yilgoster * 12)
        print("Year: " + str(yilgoster))
        print("Month: " + str(aygoster))

    # money(toplamfaiz)
    print("Total Payment: ")
    money(toplamtutar)
    print("Monthly Payment: ")
    money(aylıkodeme)
    i += yineleme