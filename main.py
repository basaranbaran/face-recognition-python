import face_recognition
import cv2
import pickle
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

# --- YAPILANDIRMA ---
encodings_path = "encodings.pickle"
tolerance = 0.5


# 1. Dosya Seçtirme Fonksiyonu
import sys

def select_image_file():
    # Komut satırından dosya yolu verildiyse onu kullan
    if len(sys.argv) > 1:
        return sys.argv[1]

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Tanınacak Fotoğrafı Seçin",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path


# 2. Dosya Adı Oluşturucu
def get_next_filename(base_name="result", ext=".jpg"):
    i = 1
    while True:
        file_name = f"{base_name}-{i}{ext}"
        if not os.path.exists(file_name):
            return file_name
        i += 1


import glob

# ... (Previous code remains the same up to helper functions) ...

# 3. Tekil Resim İşleme Fonksiyonu
def process_and_save(image_path, data, tolerance=0.5):
    if not os.path.exists(image_path):
        print(f"HATA: '{image_path}' bulunamadı.")
        return

    print(f"İşleniyor: {image_path}")
    
    try:
        # Resmi yükle
        image = face_recognition.load_image_file(image_path)
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    except Exception as e:
        print(f"HATA: Resim yüklenemedi ({image_path}): {e}")
        return

    print("  Yüzler taranıyor...")
    face_locations = face_recognition.face_locations(image, model="hog")
    face_encodings = face_recognition.face_encodings(image, face_locations)

    found_names = []

    for face_encoding in face_encodings:
        name = "Unknown"
        # Veri tabanı boşsa karşılaştırma yapma
        if data["encodings"]:
            matches = face_recognition.compare_faces(data["encodings"], face_encoding, tolerance=tolerance)
            face_distances = face_recognition.face_distance(data["encodings"], face_encoding)
            
            best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else None

            if best_match_index is not None and matches[best_match_index]:
                name = data["names"][best_match_index]

        found_names.append(name)

    # Çizim İşlemleri
    for (top, right, bottom, left), name in zip(face_locations, found_names):
        if name == "Unknown":
            color = (0, 0, 255) # Kırmızı
            label = "Unknown"
        else:
            color = (0, 100, 0) # Koyu Yeşil
            label = name.upper()

        cv2.rectangle(bgr_image, (left, top), (right, bottom), color, 2)
        
        # Etiket arka planı ve yazı
        # (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_DUPLEX, 0.8, 1) # Font boyutu hesaplama (opsiyonel)
        cv2.rectangle(bgr_image, (left, top - 35), (right, top), color, cv2.FILLED)
        cv2.putText(bgr_image, label, (left + 6, top - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

    # Sonucu Kaydet
    output_filename = get_next_filename()
    cv2.imwrite(output_filename, bgr_image)
    
    print(f"  Tamamlandı. Kaydedilen: {output_filename}")
    print(f"  Bulunanlar: {', '.join(found_names)}")
    print("-" * 30)
    return output_filename # Test için dosya adını döndür


# --- ANA İŞLEM ---

# Verileri yükle 
if not os.path.exists(encodings_path):
    print("HATA: 'encodings.pickle' bulunamadı. Önce 'learn_faces.py' çalıştırın.")
    # Veri tabanı yoksa boş bir yapı oluşturarak devam et (Test amaçlı)
    data = {"encodings": [], "names": []} 
else:
    print("Veriler 'encodings.pickle' dosyasından yükleniyor...")
    try:
        data = pickle.loads(open(encodings_path, "rb").read())
    except:
        print("HATA: Pickle dosyası bozuk veya okunamadı.")
        data = {"encodings": [], "names": []}


# 1. Komut satırı argümanı kontrolü
if len(sys.argv) > 1:
    target_path = sys.argv[1]
    process_and_save(target_path, data, tolerance)

else:
    # 2. 'test' klasörü kontrolü
    test_folder = "test"
    if os.path.exists(test_folder) and os.path.isdir(test_folder):
        print(f"'{test_folder}' klasöründeki görseller taranıyor...")
        
        # Desteklenen uzantılar
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(test_folder, ext)))
            
        if files:
            for file_path in files:
                process_and_save(file_path, data, tolerance)
        else:
            print(f"UYARI: '{test_folder}' klasöründe işlenecek resim bulunamadı.")
            print("Lütfen içine resim ekleyin veya programı bir resim dosyası argümanıyla çalıştırın.")
    
    else:
        # 3. Klasör yoksa GUI ile dosya seçtirme (Fallback)
        print("Dosya argümanı yok ve 'test' klasörü bulunamadı.")
        print("Lütfen manuel seçim yapın...")
        secilen_dosya = select_image_file()
        if secilen_dosya:
            process_and_save(secilen_dosya, data, tolerance)
        else:
            print("İşlem iptal edildi.")

print("\nTüm işlemler tamamlandı.")