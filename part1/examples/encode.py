s = "Строка"

enc = s.encode(encoding="utf-8")
print(enc)

new_s = enc.decode(encoding="windows-1251")

print(s)

# enc = s.encode(encoding="cp1251")
# print(enc)


# smb = 'd0'
# print(int(smb, 16))
# arg1 = int('d0', 16)
# arg2 = int('a1', 16)
# print(arg1, arg2, arg1*16+arg2)
# arg3 = int('d0a1', 16)
# print(arg3)
# print(ord(s[0]))