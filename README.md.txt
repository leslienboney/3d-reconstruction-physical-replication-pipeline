# 3D Reconstruction & Physical Replication Pipeline

Multi-view computer vision pipeline using COLMAP to reconstruct real-world objects from image data, with a focus on understanding reconstruction success vs failure.

---

## Overview

This project compares reconstruction performance across two datasets:

- A well-lit architectural dataset (South Building)
- A low-light, real-world dataset (car)

The goal was to understand how image quality affects feature matching, camera pose estimation, and 3D reconstruction.

---

## Key Insight

Reconstruction quality is driven far more by input data than algorithm choice.

- Clean dataset → full reconstruction, dense point cloud
- Poor dataset → low registration, sparse and incomplete geometry

---

## Results Summary

### South Building
- 127 / 127 images registered
- ~216,000 points (exhaustive)
- ~85,000 points (sequential)
- clean, complete reconstruction

### Car Dataset
- 155 input images
- 83 max registered
- ~6,600 points best case
- severe failure due to:
  - low light
  - motion blur
  - reflective surfaces
  - weak feature overlap

---

## Example Reconstructions

### South Building — Exhaustive Matching
![South Exhaustive](outputs/south-exhaustive.png)

### South Building — Sequential Matching
![South Sequential](outputs/south-sequential.png)

### Car Dataset — Exhaustive Matching
![Car Exhaustive](outputs/car-exhaustive.png)

### Car Dataset — Sequential Matching
![Car Sequential](outputs/car-sequential.png)

### Car Dataset — Guided Matching
![Car Guided](outputs/car-guided.png)

---

## Repository Structure

- `sample-images/` — representative input images  
- `outputs/` — reconstruction visualizations  
- `notes/analysis.md` — detailed analysis  
- `notes/pipeline.md` — pipeline breakdown  
- `scripts/` — supporting code and pipeline representation  

---

## What This Demonstrates

- Understanding of multi-view geometry pipelines  
- Knowledge of feature detection and matching limitations  
- Ability to analyze failure cases in real-world data  
- Practical insight into computer vision system behavior  