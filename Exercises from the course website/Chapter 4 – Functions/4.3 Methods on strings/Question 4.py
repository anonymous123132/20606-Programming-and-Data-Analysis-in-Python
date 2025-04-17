def edit(s):
    if s.count("a") > 2:
        s = s.replace("a", "*")
    if s.find("ll"):
        s = s.replace("ll", "oo")
    s = s.replace("**", "%")
    return s

print(edit("aa"))
print(edit("aaa"))
print(edit("yellow dollar"))
print(edit("** * **"))