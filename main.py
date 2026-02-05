# קוד המכונה שמדפיס "HI" ועוצר
# B4 0E = פקודת הדפסה | B0 48 = האות H | B0 49 = האות I | CD 10 = קריאת BIOS
code = bytes([
    0xB4, 0x0E,              # mov ah, 0x0e
    0xB0, 0x48, 0xCD, 0x10,  # mov al, 'H' | int 0x10
    0xB0, 0x49, 0xCD, 0x10,  # mov al, 'I' | int 0x10
    0xEB, 0xFE               # jmp $ (לולאה אינסופית)
])

# יצירת הקובץ בגודל של 512 בתים בדיוק
with open("boot.img", "wb") as f:
    f.write(code)                          # כותב את הקוד
    f.write(b'\x00' * (510 - len(code)))   # ממלא באפסים עד בית 510
    f.write(b'\x55\xAA')                   # חתימת הבוט (חובה!)

print("הקובץ boot.img נוצר בהצלחה!")
