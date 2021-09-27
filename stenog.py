import os
print("""
**************************
*			 *
*          SAEP          *
*       STENOGRAFİ       *
*			 *
**************************

Resim içine yazı gizleme toolu

Resim içinde gizlenen yazıyı görmnek istiyorsanız cat ornek.png yapın!!!
""")

yazi = input("Gizlenecek yazıyı gir ==> ")
resim = input("resim dosyasını gir (ornek.png) ==> ")

os.system("echo -n "+yazi + " >> "+resim)
