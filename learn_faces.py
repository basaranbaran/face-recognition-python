import face_recognition
import os
import pickle

# --- CONFIGURATION ---
dataset_path = "photos"
encoding_file = "encodings.pickle"

# Listeler
known_encodings = []
known_names = []

# Dataset klasörü var mı kontrol et
if not os.path.exists(dataset_path):
    print(f"HATA: '{dataset_path}' klasörü bulunamadı. Lütfen oluşturun ve içine fotoğrafları koyun.")
    exit()

print("Yüzler taranıyor ve öğreniliyor...")

# Klasörleri gez
for person_name in os.listdir(dataset_path):
    person_dir = os.path.join(dataset_path, person_name)

    # Sadece klasörleri işleme al
    if not os.path.isdir(person_dir):
        continue

    print(f" -> {person_name} işleniyor...")

    # Klasör içindeki resimleri gez
    for filename in os.listdir(person_dir):
        image_path = os.path.join(person_dir, filename)

        # Sadece resim dosyaları
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        try:
            # Resmi yükle
            image = face_recognition.load_image_file(image_path)

            # Yüz kodunu çıkar
            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                # İlk bulunan yüzü al
                known_encodings.append(encodings[0])
                known_names.append(person_name)
            else:
                print(f"    UYARI: {filename} dosyasında yüz bulunamadı.")
        except Exception as e:
            print(f"    HATA: {filename} işlenirken sorun oluştu: {e}")

print(f"\nToplam {len(known_encodings)} adet yüz hafızaya alındı.")
print("Veriler kaydediliyor...")

# Verileri dosyaya yaz
data = {"encodings": known_encodings, "names": known_names}
with open(encoding_file, "wb") as f:
    f.write(pickle.dumps(data))

print("Tamamlandı! Şimdi 'main.py' dosyasını çalıştırabilirsin.")