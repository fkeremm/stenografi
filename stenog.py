import os
print("""
**************************
*			 *
*          SAEP          *
*       STENOGRAFİ       *
*			 *
**************************

Resim içine yazı gizleme toolu

""")

yazi = input("Gizlenecek yazıyı gir ==> ")
resim = input("resim dosyasını gir (ornek.png) ==> ")

os.system("echo -n "+yazi + " >> "+resim)
