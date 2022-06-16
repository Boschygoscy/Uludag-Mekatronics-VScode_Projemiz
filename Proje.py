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
        cv.imshow("vision", image_mini)
        cv.waitKey(10) #10 saniye bekleme süresi.
        #cv.imshow() komutuyla görüntünün ekranda kalmasını sağlarız.

        image_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY) #template_gray = cv.cvtColor sekmesinden bire-bir aynısını kopyaladım.
           #Bu sayede burun fotoğrafını gri renginde, daha belirgin ve anlaşılabilir hale gelicek

        result = cv.matchTemplate(
           #parametre şablonuna gidiyoruz
            image = image_gray, # ilk parametremizin gri halini seçtik
            templ = template_gray, #ikinci parametremiz şablonun gri halini seçiyoruz
            method = cv.TM_CCOEFF_NORMED #TM_CCOEFF_NORMED yerine başka bir yöntem de seçebiliriz 
            # şablonlar burada: https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d
        )

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        #sonuçları: max val highest matching score / en yüksek eşleşme değeri, max loc/ kordinat lokasyonu 

        #en iyi eşleşmeyi yakaladığımızdan emin olduktan sonra;

        #Üstteki kodların eşik değerlerinin ayarlanması için if komutu ile düzenlenmesi gerekiyor.
        
        if max_val >= 0.8:
            pyautogui.click(
                x = max_loc[0] + x,
                y = max_loc[1] + y 
            )

            #pyautogui.click ile belirttiğimiz koordinatlarda tıklama işlemi yapar. 
            #max_loc ile objenin koordinatlarını buluyoruz üstüne x koordinatını ekleyerek nesnenin aranacak bölgesini oluşturuyoruz.
            
            image = cv.rectangle(   # Dörtgen çizebilmek için rectangle fonksiyonu kullanılmaktadır.
                                    # İstenilen nesneyi doğru parametrelerle kare içinde göstermek için yazdık.
                img = image,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + template_w, # = pt2 x 
                    max_loc[1] + template_h # = pt2 y
                ),
                color = (0,0,255), #Renk seçimi olarak maviyi seçtik.
                thickness = -1  # Dörtgenin kenar yoğunluğunu ayarlar -1 yaptığımız için dörtgenin içini yukarıda seçtiğimiz renkle doldurdu.
            ) # if döngüsünün sonu
            
            #  Bunu için fonksiyona sol üst köşenin ve sağ alt köşenin koordinatları, kenarlık rengi ve kalınlığı gönderilir
        
        else:
            break

         