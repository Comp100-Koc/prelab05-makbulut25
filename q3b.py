def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a = a[2:]
    b = b[2:]
    
    i = len(a) - 1
    j = len(b) - 1
    
    elde = 0
    sonuc = ""
    
    while i >= 0 or j >= 0:
        
        toplam = elde
        
        if i >= 0:
            toplam += int(a[i])
            i -= 1
            
        if j >= 0:
            toplam += int(b[j])
            j -= 1
        
        if toplam == 0:
            sonuc = "0" + sonuc
            elde = 0
        elif toplam == 1:
            sonuc = "1" + sonuc
            elde = 0
        elif toplam == 2:
            sonuc = "0" + sonuc
            elde = 1
        else:  # toplam == 3
            sonuc = "1" + sonuc
            elde = 1
    
    if elde == 1:
        sonuc = "1" + sonuc
    
    
    while len(sonuc) > 1 and sonuc[0] == "0":
        sonuc = sonuc[1:]
    
    return "0b" + sonuc