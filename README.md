# OpenCV HSV Color Detection Project

Bu proje, OpenCV kullanılarak **webcam üzerinden gerçek zamanlı olarak**
kırmızı, yeşil ve mavi renkli nesnelerin tespit edilmesini amaçlamaktadır.

# Projenin Amacı
- Renk tabanlı nesne algılamayı öğrenmek
- HSV renk uzayının görüntü işleme uygulamalarındaki kullanımını kavramak
- Gerçek zamanlı video akışı üzerinde maskeleme ve kontur tespiti yapmak

# Kullanılan Teknolojiler
- Python
- OpenCV
- NumPy

# Yöntem
1. Webcam görüntüsü alınır.
2. Görüntü BGR renk uzayından HSV renk uzayına dönüştürülür.
3. Kırmızı, yeşil ve mavi renkler için HSV aralıkları belirlenir.
4. `inRange` fonksiyonu ile maske oluşturulur.
5. Morfolojik işlemler ile gürültü temizlenir.
6. Konturlar bulunarak nesnelerin etrafına dikdörtgen çizilir.
7.  Program çalışırken:
Algılanan renkli nesneler bounding box ile gösterilir
Maske görüntüleri ayrı pencerelerde izlenebilir
q veya ESC tuşu ile program sonlandırılır

# Çalıştırma
```bash
pip install opencv-python numpy
python main.py

