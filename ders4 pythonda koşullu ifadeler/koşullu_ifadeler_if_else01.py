# Kullanıcının boyunu sorgulayan program.
boy = input("Boyun kaç cm?")
if int(boy) > 150:
  print ("wow, boyun uzun demek ki!")
else:
  if int(boy) >= 56:
    print ("ne uzunsun ne de kısa")
  else:
    print ("Boyun kısa")