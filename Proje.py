#Kullanılması gereken kitaplıklar;

import cv2 as cv
import pyautogui
from time import sleep
import keyboard

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






