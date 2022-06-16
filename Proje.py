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
   #template_gray.shape şablonu kesiyoruz ve nereye bakılması gerektiğini gösteriyoruz -1 değeri tersine döndermemiz için.
# oyun penceresi genişliği (x) yüksekliği girilmesi gerekiyor.,şüs





