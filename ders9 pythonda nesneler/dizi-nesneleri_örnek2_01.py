kelime = "ABCD"
print(kelime.rjust(10, "*"))
print(kelime.rjust(3, "*"))
print(kelime.rjust(15, ">"))
print(kelime.rjust(10))
print(kelime.ljust(12, ">"))
print(kelime.center(15, "*"))

# str nesnesi için yöntemler
"""
upper=Metnin tüm harflerini büyük harfe dönüştürür.
lower=Metnin tüm harflerini küçük harfe dönüştürür.
rjust=Karakter dizisini sağa yaslar.
ljust=Karakter dizisini sola yaslar.
center=Karakter dizisini ortalar.
strip=Karakter dizisinin sağında ve solunda bulunan boşluk karakterlerini yok etmemizi sağlar.
startswith=Karakter dizilerinin ön ekini sorgulamamızı sağlar.
endswith=Karakter dizilerinin ön ekini sorgulamamızı sağlar.
count=Bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgular.
find=Bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgular.
format=Bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgular.

"""