# Industrial Computer Vision & Deep Learning Anomaly Detection Pipeline for Microprocessors

## 📌 Project Overview
This repository contains an end-to-end Machine Learning Operations (MLOps) pipeline designed for automated hardware quality control in semiconductor manufacturing. 

Transitioning from traditional, error-prone human microscope inspections, this software-driven architecture automates the detection of microscopic structural anomalies (e.g., scratches, center faults, location defects) on microprocessor silicon surfaces and integrated circuits (ICs). 

The framework bridges an Electronics & Communication Engineering (ECE) hardware foundation with Tier-1 enterprise software principles by stringing together data normalization, relational database tracking, deep learning classification, and cloud deployment registries.

---

## 🏗️ System Architecture & Data Flow

1. **Phase 1: Automated Data Wrangling (Pandas & NumPy)** – Microchip pixel arrays are systematically scraped from local ingestion directories, cataloged via Pandas DataFrames, and normalized into floating-point multidimensional matrices utilizing NumPy vector scaling.
2. **Phase 2: Relational Infrastructure Logging (SQL/SQLite)** – Standardized asset paths, UUIDs, and category labels are stream-ingested into a local relational database ledger. High-risk defect clusters are isolated via targeted SQL compliance audit queries to shape focused deep learning pipelines.
3. **Phase 3: Deep Learning Training Core (PyTorch)** – A custom-tailored Convolutional Neural Network (CNN) architecture handles multi-class visual feature map optimization, computing spatial loss variances to classify structural component degradation.
4. **Phase 4: Cloud Model Registry Deployment (AWS boto3)** – Final optimized neural network parameter binary sets (`.pth` files) are programmatically verified and uploaded directly to global Amazon S3 secure storage infrastructure for real-time deployment across global manufacturing facilities.
