import random
from uzwords import words

def get_word():
    return random.choice(words)

def display(jami_harflar, random_soz):
    random_soz = random_soz.lower()
    jam = ''

    for n in range(len(random_soz)):
        tek = False
        for i in range(len(jami_harflar)):
            if random_soz[n] == jami_harflar[i]:
                jam += jami_harflar[i]
                tek = True
                break
        if not tek:
            jam += '-'

    return jam

def play(soz = get_word()):
    print(f"Men {len(soz)} xonali so'z o'yladim. Topa olasizmi?\n" + 
          "-" * len(soz))
    jami = ''
    tekshirish = True

    while tekshirish:
        harf = input("Harf kiriting (kirilcha): ").lower()

        takrorlangan = False
        for oldingi_harf in jami:
            if harf == oldingi_harf:
                takrorlangan = True
                break
        
        if takrorlangan:
            print("Bu harfni avval kiritgansiz, boshqa harf kiriting!")
            continue

        jami += harf

        tek = display(jami, soz)

        harf_topildi = False
        for i in range(len(soz)):
            if soz[i] == harf:
                harf_topildi = True
                break
        
        if harf_topildi:
            print(f"{harf} harfi to'g'ri.")
        else:
            print("Bunday harf yo'q!")

        hammasi_topildi = True
        for i in range(len(tek)):
            if tek[i] == '-':
                hammasi_topildi = False
                break

        if hammasi_topildi:
            tekshirish = False

        print(f"{tek}\nShu vaqtgacha kiritgan harflaringiz: {jami}")

    print (f"Tabriklayman, {soz} so'zini {len(jami)} ta urunishda topdingiz!")

play()
