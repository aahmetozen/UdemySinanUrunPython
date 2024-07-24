dereceF = float (input ("Sıcaklığını F derece olarak girin:"))
# Dönüşümü gerçekleştirin
#dereceC = (dereceF - 32)/(1.8)
dereceC = 5/9 * (dereceF - 32)
# Sonucu bildir
print (dereceF, "derece F =", dereceC, "C derece")