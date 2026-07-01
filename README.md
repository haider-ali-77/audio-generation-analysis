# Speech Augmentation and Acoustic Simulation Toolkit

## Overview

This repository provides a comprehensive framework for **speech data augmentation**, **acoustic environment simulation**, and **generative speech enhancement**. The project combines traditional signal processing techniques with modern deep learning approaches to generate realistic speech under diverse recording conditions.

The repository consists of two complementary research modules:

* **CodecSim** – A classical audio degradation simulator that models real-world communication channels using environmental noise, room impulse responses, telephony codecs, and bandwidth limitations.
* **GANs** – Deep learning experiments exploring speech enhancement and voice conversion using Generative Adversarial Networks (GANs), including CycleGAN and MelGAN.

Together, these modules enable the creation of robust speech datasets for training and evaluating speech recognition, speaker verification, voice conversion, and audio enhancement systems.

---

## Key Features

### Acoustic Simulation

* Environmental noise augmentation
* Room reverberation simulation
* Telephony codec simulation
* Audio codec compression
* Bandwidth filtering
* Randomized degradation pipelines
* Batch audio processing

### Deep Learning

* CycleGAN-based voice transformation
* MelGAN neural vocoder experiments
* Speech enhancement research
* Voice conversion pipelines

---

## Repository Structure

```text
speech-augmentation-toolkit/
│
├── README.md
│
├── CodecSim/
│   ├── generator.py
│   ├── degrade-audio-safe-random__.py
│   ├── degrade-audio-list-safe-random__.py
│   ├── prepare-impulse-responses.py
│   ├── prepare-impulse-responses__.py
│   ├── download-noise-db.py
│   ├── codec_configure.sh
│   ├── AMRNB.py
│   ├── aac.sh
│   ├── requirements.txt
│   ├── README.txt
│   └── src/
│       ├── FFmpeg
│       ├── SoX
│       ├── Codec2
│       ├── Opus
│       ├── LAME
│       ├── AAC
│       ├── G.191
│       └── Additional codec packages
│
└── GANs/
    ├── CycleGANs_talkbank_dataset.ipynb
    └── MelGAN_VC.ipynb
```

---

## Research Architecture

```text
                  Clean Speech
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 Classical Acoustic          Deep Learning
    Simulation                  GAN Models
        │                             │
        ▼                             ▼
 Codec Compression          Voice Conversion
 Noise Injection             Speech Generation
 Reverberation               Speech Enhancement
 Bandwidth Filtering          Neural Vocoder
        │                             │
        └──────────────┬──────────────┘
                       ▼
             Robust Speech Dataset
```

---

## Module 1: CodecSim

The **CodecSim** module simulates realistic communication channels by applying a sequence of degradations to clean speech recordings.

### Supported Acoustic Effects

* Environmental noise
* Room reverberation
* Telephone channel simulation
* Cellular communication
* Satellite communication
* Audio compression artifacts
* Playback distortion
* Band-pass filtering
* Amplitude normalization

---

### Supported Codecs

The toolkit supports numerous communication codecs, including:

* G.711
* G.722
* G.726
* G.728
* G.729
* AMR-NB
* AMR-WB
* GSM
* Opus
* Codec2
* AAC
* MP3
* SILK

Additional tools include:

* FFmpeg
* SoX
* LAME
* Opus
* Codec2

---

### Core Components

| File                                  | Purpose                         |
| ------------------------------------- | ------------------------------- |
| `generator.py`                        | Single audio degradation        |
| `degrade-audio-safe-random__.py`      | Random acoustic simulation      |
| `degrade-audio-list-safe-random__.py` | Batch processing                |
| `prepare-impulse-responses.py`        | Impulse response preprocessing  |
| `download-noise-db.py`                | Environmental noise acquisition |
| `codec_configure.sh`                  | Codec installation              |

---

## Module 2: GAN Research

The **GANs** directory investigates neural approaches for speech generation and enhancement.

### CycleGAN

Notebook:

```text
CycleGANs_talkbank_dataset.ipynb
```

Research topics include:

* Non-parallel voice conversion
* Domain adaptation
* Speech transformation
* Speaker-independent conversion

---

### MelGAN

Notebook:

```text
MelGAN_VC.ipynb
```

Focus areas:

* Neural vocoding
* High-quality speech synthesis
* Voice conversion
* Waveform generation

---

## Processing Pipeline

```text
Speech Dataset
      │
      ▼
Acoustic Simulation
      │
      ▼
Codec Compression
      │
      ▼
Environmental Noise
      │
      ▼
Room Reverberation
      │
      ▼
(Optional)
GAN-based Speech Enhancement
      │
      ▼
Training Dataset
```

---

## Installation

Install dependencies:

```bash
pip install -r CodecSim/requirements.txt
```

Configure codecs:

```bash
cd CodecSim
sh codec_configure.sh
```

---

## Usage

Generate degradation for a single audio file:

```bash
python CodecSim/generator.py
```

Generate batch degradations:

```bash
python CodecSim/degrade-audio-list-safe-random__.py
```

Run predefined degradation scenarios:

```bash
python CodecSim/degrade-audio-safe-random__.py
```

GAN experiments can be executed through the notebooks in the `GANs/` directory.

---

## Applications

This toolkit can be used for:

* Automatic Speech Recognition (ASR)
* Speaker Verification
* Speaker Identification
* Voice Conversion
* Speech Enhancement
* Keyword Spotting
* Audio Classification
* Telecommunication Research
* Robust Speech Model Training
* Data Augmentation for Deep Learning

---

## Research Contributions

The repository combines **traditional digital signal processing (DSP)** and **deep learning** approaches to improve speech robustness. It supports the generation of realistic acoustic conditions through codec simulation while exploring GAN-based methods for speech synthesis and enhancement, making it suitable for benchmarking modern speech AI systems.

---

## Future Work

* Diffusion-based speech generation
* Retrieval-based Voice Conversion (RVC)
* Neural audio codecs (e.g., EnCodec)
* Self-supervised speech representations (HuBERT, Wav2Vec 2.0)
* Real-time streaming augmentation
* Multi-speaker voice conversion
* Large-scale speech augmentation pipelines

---

## Technology Stack

* Python
* NumPy
* SciPy
* FFmpeg
* SoX
* Codec2
* Opus
* PyTorch
* CycleGAN
* MelGAN
* Signal Processing Libraries

---

## License

This project is distributed under the terms specified in the LICENSE file.

