# Author RTS 1/23/22

grades = {"End s1 labs": 100, "Start s2 labs": 100,  "Cycle 10 Labs": 0, "Mid-year Project Proposal": 80, "Cycle 10 Practice Quiz": 0, "Cycle 10 Quiz": 0}
print(grades.values())
for v in grades:
    print(v)
for k, v in grades:
    if v == 100:
        print(k)
