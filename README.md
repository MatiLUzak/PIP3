# Python-Data-Clustering-Analysis

## 📌 Opis projektu

**Python-Data-Clustering-Analysis** to projekt w języku **Python**, który skupia się na analizie danych, implementacji algorytmów klasteryzacji oraz innych metod numerycznych. Projekt zawiera skrypty do przetwarzania danych, klasteryzacji oraz implementacji algorytmu Sita Eratostenesa.

## 🛠 Wymagania

Aby uruchomić skrypty, potrzebujesz:

- **Python 3.8** lub nowszy
- **pip** – menedżer pakietów dla Pythona

## 🚀 Instalacja

1. **Klonowanie repozytorium:**

   ```bash
   git clone https://github.com/MatiLUzak/PIP3.git
   cd PIP3
   ```

2. **Utworzenie i aktywacja środowiska wirtualnego (opcjonalnie, ale zalecane):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # lub
   venv\Scripts\activate  # Windows
   ```

3. **Instalacja zależności:**

   Upewnij się, że masz zainstalowane następujące biblioteki:

   - **numpy**
   - **pandas**
   - **scikit-learn**
   - **matplotlib**

   Możesz je zainstalować za pomocą polecenia:

   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```

## ▶️ Uruchomienie skryptów

1. **Główny skrypt (`main.py`):**

   Skrypt ten integruje różne funkcje analizy danych i klasteryzacji.

   ```bash
   python main.py
   ```

2. **Skrypt klasteryzacji (`klustering.py`):**

   Zawiera implementację algorytmów klasteryzacji.

   ```bash
   python klustering.py
   ```

3. **Skrypt Sita Eratostenesa (`sito.py`):**

   Implementuje algorytm Sita Eratostenesa do znajdowania liczb pierwszych.

   ```bash
   python sito.py
   ```

## 📂 Struktura projektu

```
PIP3/
├── .idea/
├── Practice Datasets-20241015/
│   ├── dataset1.csv
│   ├── dataset2.csv
│   └── ...
├── klustering.py
├── main.py
├── sito.py
└── README.md
```

- **`.idea/`** – katalog konfiguracyjny środowiska IDE.
- **`Practice Datasets-20241015/`** – katalog zawierający zestawy danych do analizy.
- **`klustering.py`** – skrypt z implementacją algorytmów klasteryzacji.
- **`main.py`** – główny skrypt integrujący funkcje projektu.
- **`sito.py`** – skrypt z implementacją algorytmu Sita Eratostenesa.
- **`README.md`** – plik z dokumentacją projektu.

## ✍️ Autor

- **MatiLUzak** – [Profil GitHub](https://github.com/MatiLUzak)

## 📜 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.
