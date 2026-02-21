# 🚀 Fahlawi AI Multi-Pro

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CUDA](https://img.shields.io/badge/CUDA-Enabled-green)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![Status](https://img.shields.io/badge/Production-Ready-brightgreen)

> Automated Egyptian Marketing Ad Production Engine\
> Generate fully voiced Arabic video ads from product images in seconds.

------------------------------------------------------------------------

# 🎥 Demo

## 🧠 Input

-   Upload product images\
-   Enter product name\
-   Add optional marketing keywords (e.g., "Free delivery", "Limited
    time discount")

## 🎬 Output

-   Professionally edited multi-image montage\
-   Egyptian Arabic neural voiceover\
-   GPU-polished audio\
-   Arabic RTL headline overlay\
-   Auto-exported `.mp4` file

------------------------------------------------------------------------

# ✨ Features

✅ Dynamic AI Script Generation\
✅ Egyptian Neural Voice (ar-EG-SalmaNeural)\
✅ GPU Audio Normalization (CUDA)\
✅ Multi-Image Cinematic Montage\
✅ Arabic RTL Text Rendering Fix\
✅ Automatic Export Folder Management\
✅ Sequential File Naming (No Overwrites)\
✅ Modular Architecture

------------------------------------------------------------------------

# 🏗 Architecture Overview

    User Input (Images + Product + Keywords)
                │
                ▼
          brain.py (AI Script Generator)
                │
                ▼
       Edge TTS (Neural Voice Generation)
                │
                ▼
     CUDA Audio Normalization (Torch GPU)
                │
                ▼
     MoviePy Multi-Image Montage + RTL Text
                │
                ▼
         Generated_Ads/Ad_Product_1.mp4

------------------------------------------------------------------------

# 📂 Project Structure

    .
    ├── main.py          # Production pipeline + Gradio interface
    ├── brain.py         # Dynamic ad script generation engine
    ├── config.py        # GPU validation + export management
    ├── Generated_Ads/   # Auto-created export directory
    └── README.md

------------------------------------------------------------------------

# 🛠 Installation

## 1️⃣ System Requirements

-   Python 3.10+
-   CUDA-enabled GPU (Recommended)
-   ImageMagick (required for MoviePy)

### Install ImageMagick (Linux / WSL2)

``` bash
sudo apt install imagemagick
```

------------------------------------------------------------------------

## 2️⃣ Install Python Dependencies

``` bash
pip install torch torchaudio soundfile edge-tts gradio moviepy arabic-reshaper python-bidi
```

------------------------------------------------------------------------

# 🚀 Running the Application

``` bash
python main.py
```

Then open the Gradio interface in your browser.

------------------------------------------------------------------------

# 🎬 Production Pipeline Phases

### Phase 1 --- AI Script Generation

Generates Egyptian marketing copy dynamically based on product +
keywords.

### Phase 2 --- Neural Voiceover

Uses Microsoft Edge TTS:

    ar-EG-SalmaNeural

### Phase 3 --- GPU Audio Polish

CUDA-accelerated peak normalization using PyTorch.

### Phase 4 --- Video Montage

-   Even duration per image\
-   Crossfade transitions\
-   Arabic reshaped RTL headline\
-   Export as H.264 `.mp4`

------------------------------------------------------------------------

# 📦 Output Example

    Generated_Ads/
        Ad_Pepsi_1.mp4
        Ad_Pepsi_2.mp4
        Ad_Perfume_1.mp4

------------------------------------------------------------------------

# 🔥 Why This Is Production-Ready

✔ Modular design\
✔ GPU-accelerated processing\
✔ Automatic export management\
✔ Clean UI interface\
✔ Arabic marketing optimized\
✔ Expandable architecture

------------------------------------------------------------------------

# 📈 Future Roadmap

-   Batch campaign generation\
-   AI image enhancement\
-   Background music auto-selection\
-   Docker deployment\
-   REST API version

------------------------------------------------------------------------
# 💡 Fahlawi AI Multi-Pro

Drag. Type. Generate. Publish.

Your automated Egyptian marketing studio powered by AI.
