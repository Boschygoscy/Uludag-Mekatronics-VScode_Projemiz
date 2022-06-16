#https://www.classicgame.com/game/Whack+a+Mole

#Kullanılması gereken kitaplıklar;

import cv2 as cv
#Ana kütüphanemiz olan opencv kütüphanesini çağırdık ve cv2 yerine cv olarak adlandırdık.
import pyautogui
#Klavye ve mouse hareketini kontrol etmemizi sağlayan kütüphanedir. Mouse hareketi ve tıklama için kullandık
from time import sleep
#Kodun işleyişini belli bir süre bekletmek için kullanılır.
import keyboard
#Programı başlatıp durdurmak için kullandığımız bir kütüphane.

pyautogui.PAUSE = 0  
  # Her pyautogui çağrısı arasında beklenilecek süredir. Şuan 0 olduğu için bekleme zamanı yok.


print("Başlatmak için 's' tuşuna basınız.")
print("Çıkmak için 'q' tuşuna basınız.")
keyboard.wait('s')
# "s" tuşuna basarak program başlatılır. 
# "q" tuşuna basarak programdan çıkış yapılır. 


#template (Şabonun seçimi(Burun) ve dosya merkezi burada, eğer çalışmazsa ekran görüntüsünü değiştir)
template = cv.imread("foto/burun.png") #Şablon==template, klasör/png dosyasının ismini target gösteriyor
   #cv.imread belirtilen dosyadan bir görüntü yüklüyor.
template_gray = cv.cvtColor(template, cv.COLOR_RGB2GRAY) #görüntünün gri tonlama modunda yüklenmesini belirtir.
   #cv.COLOR_RGB2GRAY ile kırmızı mavi yeşil renklerini gri olarak görecek.
template_w, template_h = template_gray.shape[::-1] #w=genişlik, h=yükseklik (opencv'de wide'ı  ilk almamız gerekiyor)
   #template_gray.shape şablonu kesiyoruz ve nereye bakılması gerektiğini gösteriyoruz -1, değeri tersine döndermemiz için.

# oyun penceresi genişliği,yüksekliği ve (x,y) girilmesi gerekiyor;
x, y, w, h = 523, 247, 875, 679 #Ekranın kordinatları, capture'laması gereken ekranın yüzeyini belirlemek zorundayız.
  #Yukarıdaki ekran kordinatları nasıl belirlenir;
     #İlk önce tüm ekranımızı Paint'e aktarıyoruz, bu sayede ekranın sol alt'da px örneğin(212,899) 212=x 899=y olarak oyunun açıldığı yerdeki ekran kordinatlarını alıyoruz.
     #(!!!) Ekran çözünürlüğüne göre bu değer değişir. Manuel olarak ayarlanması gerekebilir. 
sleep(3) #Aktif etme tuşuna bastığımızda beklememiz gereken süre (3) bu 3 saniyelik aralıkta durumumuz: False 

while True:

    pyautogui.screenshot("foto/image.png", (x, y, w, h))
    #Ekran görüntüsü almak için kullanılan method.Klavyedeki ekran görüntüsü alma tuşunu çalıştırıyor
    image = cv.imread("foto/image.png")
    #cv2. imread() komutu belirtilen dosyadan bir görüntü yükler

   while True:

        # Bilgisayarın ne gördüğünü göstermek için küçük bir pencere açar
        
        image_mini = cv.resize(
            src = image,
            dsize = (450,350)
        # cv.resize() komutuyla yeniden boyutlandırmak istediğimiz nesneyi ve piksel büyüklüğünü(x,y) seçiyoruz bunun için daha öncesinde aldığımız
        #ekran görüntülerini kullanıcağız ve anlık olarak bilgisayarın gözünden nesneleri göreceğiz
        )