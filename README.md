# 🧠 Parkinson's Disease Detection — Voice & Handwriting Data

> Early-stage project exploring Parkinson's disease detection from **voice measurements** and **handwriting (spiral and wave drawings)**.

🚧 **Status: work in progress.** This repository currently holds the prepared datasets, including augmented drawing images. The model-training code and results will be added next.

---

## 📊 Datasets in this repository

### 1. Voice measurements: `Parkinson's/parkinsons.data`
- **195 voice recordings:** 147 Parkinson's, 48 healthy
- 22 acoustic features per recording (fundamental frequency, jitter, shimmer, noise-to-harmonics ratio, RPDE, DFA, PPE, …) and a `status` label (1 = Parkinson's, 0 = healthy)
- Source: UCI Machine Learning Repository, *Parkinsons Data Set* (Little et al.)

### 2. Handwriting tablet recordings: `Parkinson's/hw_dataset/`, `Parkinson's/new_dataset/`
- Pen-tablet traces from control and Parkinson's subjects
- Each row: `X; Y; Z; Pressure; GripAngle; Timestamp; Test ID`
- Tests: 0 = static spiral, 1 = dynamic spiral, 2 = circular motion
- Source: UCI Machine Learning Repository, *Parkinson Disease Spiral Drawings Using Digitized Graphics Tablet* (Isenkul et al.)

### 3. Drawing images: `Parkinson's/hw_drawings/`, `Parkinson's/augmented_hw_dataset/`
- Static and dynamic spiral drawings, plus **augmented spiral and wave images** split for training:

| Split | Spiral (per class) | Wave (per class) |
| :--- | :---: | :---: |
| Training | 144 | 144 |
| Validation | 36 | 36 |
| Testing | 75 | 75 |

Classes: `healthy`, `parkinson`

---

## 🎯 Planned approach

| Data | Planned model |
| :--- | :--- |
| Voice features | Scikit-learn classifiers (e.g. SVM, Random Forest, XGBoost) with scaling and cross-validation |
| Tablet traces | Engineered features (speed, pressure variation, tremor) + classical ML |
| Drawing images | CNN / transfer learning (e.g. ResNet) on the augmented spiral and wave images |

---

## 📁 Repository Structure

```
parkinson-prediction/
└── Parkinson's/
    ├── parkinsons.data            # UCI voice dataset
    ├── readme.txt                 # Tablet data format
    ├── hw_dataset/                # Tablet traces (control / parkinson)
    ├── new_dataset/               # Additional tablet traces
    ├── hw_drawings/               # Spiral drawing images
    └── augmented_hw_dataset/      # Augmented spiral & wave images (train/val/test)
```

---

## 📚 Dataset credits

- Little, M. A. et al. *Suitability of dysphonia measurements for telemonitoring of Parkinson's disease.* IEEE Transactions on Biomedical Engineering, 2009. UCI Machine Learning Repository.
- Isenkul, M. E., Sakar, B. E., Kursun, O. *Improved spiral test using digitized graphics tablet for monitoring Parkinson's disease.* 2014. UCI Machine Learning Repository.
<!-- TODO: add the source of the spiral/wave drawing image dataset -->
