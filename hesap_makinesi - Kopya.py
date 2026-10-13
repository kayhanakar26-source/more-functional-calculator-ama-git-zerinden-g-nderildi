import difflib
geçerli_işlemler=["toplama","çikarma","çarpma","bölme","üs alma","karekök"]
def en_yakın_işlem(işlem):
    en_yakın= difflib.get_close_matches(işlem,geçerli_işlemler,n=1,cutoff=0.6)
    if en_yakın:
        return en_yakın[0]
    else:
        return None


while True:
    x=int(input("ilk sayiyi girin:"))
    işlem=en_yakın_işlem(input("işlemi girin toplama , çikarma , çarpma , bölme , üs alma , karekök: (toplama , çikarma , çarpma , bölme , üs alma , karekök:"))
    y=int(input("ikinci sayiyi girin:"))
    if işlem=="toplama":
        print(x+y)
    elif işlem=="çikarma":
        print(x-y)
    elif işlem=="çarpma":
        print(x*y)
    elif işlem=="bölme":
        if y==0:
            print("lütfen 0 dan farklı bir sayi seçin")
        else:
            print (x/y)
    elif işlem=="üs alma":
        print(x**y)
    elif işlem=="karekök":
        print(x**(1/2))
    else:
        print("maalesef yapmaya çaliştiğiniz işlem hatali")
    seçim=input("devam etmek ister misniz?: (evet/hayir):")
    if seçim=="evet":
        continue
    else:break    