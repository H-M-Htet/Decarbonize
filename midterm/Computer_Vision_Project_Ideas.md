# Master's Computer Vision Project Ideas & Thesis Connection

This document summarizes potential project ideas for a Master's level Computer Vision course, with a specific focus on connecting the project to a thesis in the field of self-driving vehicles.

## Core Requirement

The project must go beyond simply using a pre-trained model (like YOLO). The goal is to **modify or improve** a model's architecture, loss function, or training methodology to solve a specific, challenging task.

---

## Idea 1: All-Weather Semantic Segmentation via Domain Adaptation

*   **High-Level Concept:** Train a model to understand road scenes (e.g., identify drivable areas, pedestrians, lane lines) in adverse conditions (rain, fog, night) when it has only been trained on clear, sunny daytime data.

*   **The Self-Driving Problem:** An autonomous vehicle's perception system must be robust to all weather and lighting conditions. A model trained only on "perfect" data is a major safety risk. This "domain shift" is a critical, unsolved problem in the industry.

*   **Your Technical Task (The "Modification"):**
    1.  **Baseline:** Use a standard semantic segmentation model (e.g., DeepLabv3) trained on a labeled "source" dataset (like Cityscapes or a synthetic one like GTA-V).
    2.  **Target:** Use an **unlabeled** "target" dataset of adverse conditions (e.g., Foggy Cityscapes, ACDC).
    3.  **Improvement:** Implement an **unsupervised domain adaptation (UDA)** technique. The most common method is adversarial training:
        *   Add a "domain discriminator" network that tries to guess if features are from a source or target image.
        *   Modify the main segmentation model's loss function to encourage it to **fool** the discriminator. This forces the model to learn **domain-invariant features**—features that capture the essence of a "road" or "car" regardless of the weather.

*   **Connection to Master's Thesis:**
    *   This project serves as a perfect foundational chapter.
    *   **Thesis Expansion:** You could develop a more advanced UDA technique, explore source-free domain adaptation, or apply the concepts to other sensor modalities like LiDAR.

---

## Idea 2: Robust Traffic Sign Recognition using Guided Attention

*   **High-Level Concept:** Make a model that not only classifies traffic signs but also learns *which part* of the sign is most important, making it more accurate and robust, especially with visually similar signs.

*   **The Self-Driving Problem:** Misclassifying a "Speed Limit 80" sign as a "Speed Limit 30" sign, or a "Stop" sign as a "Do Not Enter" sign, is a critical failure. The model must be robust to occlusions, bad lighting, and distractions.

*   **Your Technical Task (The "Modification"):**
    1.  **Baseline:** Start with a standard classification model (e.g., ResNet).
    2.  **Improvement:** Introduce a **self-correcting attention module**.
        *   The module generates a heatmap highlighting the most important image regions for its decision.
        *   You will design a novel **loss function** that penalizes the model if it's "looking" at the wrong place (e.g., focusing on the sign's border instead of the number). This forces the model to learn the truly discriminative features.

*   **Connection to Master's Thesis:**
    *   Demonstrates your ability to build more interpretable and reliable models.
    *   **Thesis Expansion:** Handle partially occluded or damaged signs, incorporate temporal information (tracking a sign over multiple frames), or build a multi-task model for both signs and traffic lights.

---

## Idea 3: Monocular Depth Estimation with Uncertainty Quantification

*   **High-Level Concept:** Create a model that estimates the distance to objects using only a single camera, and crucially, also reports **how confident** it is about its own predictions.

*   **The Self-Driving Problem:** Depth perception is fundamental for collision avoidance. While LiDAR is good, it's expensive. Camera-based depth is a key area of research. A model that knows what it doesn't know is significantly safer and allows for better sensor fusion.

*   **Your Technical Task (The "Modification"):**
    1.  **Baseline:** Implement a standard monocular depth estimation network (often a U-Net-like architecture).
    2.  **Improvement:** Modify the model's output and loss function to predict a **probability distribution** for the depth of each pixel, not just a single value.
        *   The model will output two values per pixel: the **mean** (the depth) and the **variance** (the uncertainty).
        *   Use a specialized loss function (like Gaussian Negative Log-Likelihood) to train the model to be accurate when its uncertainty is low, and to correctly report high uncertainty in ambiguous regions (e.g., a textureless wall or a highly reflective surface).

*   **Connection to Master's Thesis:**
    *   This is a research-heavy topic at the forefront of safe perception systems.
    *   **Thesis Expansion:** Use the uncertainty map to intelligently fuse camera data with sparse LiDAR data, develop novel architectures for better uncertainty estimation, or integrate the uncertainty-aware depth into downstream motion planning modules.

---
### Key Term Explained: Domain Adaptation

*   **Analogy:** You've mastered Shakespearean English (Source Domain) and are dropped into modern Los Angeles to understand teenage text messages (Target Domain). The underlying language is the same, but the vocabulary, slang, and grammar are different. Domain adaptation is the process of applying your core knowledge to the new "dialect" without an explicit dictionary.
*   **In CV:** It's a set of techniques to make a model trained on a labeled **source domain** (e.g., synthetic data) work well on an **unlabeled target domain** (e.g., real-world rainy data) where the data distribution has shifted.
*   **Main Strategy (Adversarial Training):** A task model learns to perform its job (e.g., segmentation) while simultaneously trying to produce features that are so generic that a second "discriminator" model cannot tell if they came from the source or target domain. This results in robust, domain-invariant features.
