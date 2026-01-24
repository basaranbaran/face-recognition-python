[🇹🇷 Türkçe](#türkçe) | [🇬🇧 English](#english)

---

# <a id="türkçe"></a>TÜRKÇE

# Yüz Tanıma Sistemi (Face Recognition)

Bu proje, Python kullanarak basit, etkili ve kolay kurulabilir bir yüz tanıma sistemi sunar. `dlib` ve `face_recognition` kütüphanelerini kullanarak kişilerin yüzlerini öğrenir ve fotoğraf üzerinden kimlik tespiti yapar.

## Özellikler
*   **Otomatik Yüz Öğrenme:** Klasör isimlerinden kişi isimlerini otomatik öğrenir.
*   **Toplu Test:** `test/` klasöründeki tüm fotoğrafları tek seferde işleyebilir.
*   **Görselleştirme:** Tespit edilen yüzleri kare içine alır ve isimlerini yazar. Bilinmeyen yüzleri "Unknown" olarak işaretler.

## Nasıl Çalışır?

Proje iki ana aşamadan oluşur:

### 1. Öğrenme (`learn_faces.py`)
Bu adımda sistem, tanıması gereken kişilerin yüzlerini ezberler.
*   `photos/` klasörünün altına kişi isimleriyle klasörler açmalısınız.
*   Örnek: `photos/Baran/resim1.jpg`, `photos/Ahmet/resim2.jpg`
*   Komut çalıştığında bu fotoğraflardaki yüz özelliklerini çıkarıp `encodings.pickle` dosyasına kaydeder.

### 2. Tanıma (`main.py`)
Bu adımda sistem, yeni fotoğraflardaki yüzleri tanır.
*   **Otomatik Mod:** Programı parametresiz çalıştırırsanız, `test/` klasöründeki tüm resimleri işler.
*   **Manuel Mod:** `python main.py resim.jpg` şeklinde belirli bir dosyayı işleyebilirsiniz.
*   Bulunan yüzler `encodings.pickle` içindeki kayıtlarla karşılaştırılır.
*   Sonuçlar `result-1.jpg`, `result-2.jpg` şeklinde kaydedilir.

## Kurulum

### Gereksinimler
*   Python 3.11 veya üzeri

### Adımlar

1.  Repoyu klonlayın:
    ```bash
    git clone https://github.com/basaranbaran/face-recognition-python.git
    cd face-recognition-python
    ```

2.  Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
    *(Windows kullanıcıları için `dlib` kurulumunu kolaylaştıran `dlib-bin` paketi gereksinimlere eklenmiştir.)*

## Kullanım

1.  **Eğitim Verisi Hazırlama:**
    `photos` klasörü içine kişilerin isimleriyle klasörler oluşturun ve fotoğraflarını ekleyin.

2.  **Sistemi Eğitme:**
    ```bash
    python learn_faces.py
    ```

3.  **Test Etme:**
    Test etmek istediğiniz fotoğrafları `test` klasörüne atın ve çalıştırın:
    ```bash
    python main.py
    ```
    Sonuçlar ana dizinde `result-X.jpg` olarak oluşacaktır.

---

# <a id="english"></a>🇬🇧 ENGLISH

# Simple Face Recognition System

This project provides a simple, efficient, and easy-to-setup face recognition system using Python. It utilizes `dlib` and `face_recognition` libraries to learn faces from folders and identify them in new images.

## Features
*   **Automatic Learning:** Learns person names automatically from folder names.
*   **Batch Processing:** Can process all images in the `test/` directory at once.
*   **Visualization:** Draws bounding boxes around detected faces and labels them. Unknown faces are marked as "Unknown".

## How It Works?

The project consists of two main stages:

### 1. Learning (`learn_faces.py`)
In this step, the system memorizes the faces of the people it needs to recognize.
*   You must create subdirectories under the `photos/` folder named after the people.
*   Example: `photos/John/image1.jpg`, `photos/Doe/image2.jpg`
*   When run, it extracts facial features from these photos and saves them into a `encodings.pickle` file.

### 2. Recognition (`main.py`)
In this step, the system identifies faces in new photos.
*   **Automatic Mode:** If run without arguments, it processes all images in the `test/` folder.
*   **Manual Mode:** You can process a specific file like `python main.py image.jpg`.
*   Detected faces are compared with records in `encodings.pickle`.
*   Results are saved as `result-1.jpg`, `result-2.jpg`, etc.

## Installation

### Requirements
*   Python 3.11 or higher

### Steps

1.  Clone the repository:
    ```bash
    git clone https://github.com/basaranbaran/face-recognition-python.git
    cd face-recognition-python
    ```

2.  Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(For Windows users, `dlib-bin` package is included in requirements to simplify `dlib` installation.)*

## Usage

1.  **Prepare Training Data:**
    Create folders with people's names inside the `photos` directory and add their photos.

2.  **Train the System:**
    ```bash
    python learn_faces.py
    ```

3.  **Test:**
    Put the photos you want to test into the `test` directory and run:
    ```bash
    python main.py
    ```
    Results will be generated as `result-X.jpg` in the main directory.
