print("py42")
sh=input("Enter Hours: ")
sr=input("Enter Hours: ")
try:
    fr=float(sr)
    fh=float(sh)
except:
    print("Tlqkf")
    quit()

print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh-40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp= fh * fr
print("Pay:",xp)
