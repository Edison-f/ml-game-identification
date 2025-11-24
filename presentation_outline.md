# Final Project Presentation Outline  
### CS 171 – Predicting Video Game Genres from Screenshots  
**Authors:** Angie Avalos Joel & Edison Fuh  
**Presentation Length:** 8 minutes (4 minutes each)

---

## 1. Introduction (Angie)
- Research question:
  - Can a CNN correctly identify the genre of a video game based only on gameplay screenshots?
  - Which genres are easiest or hardest to classify?
  - What visual features seem to influence correct vs. incorrect predictions?
- Overview of approach:
  - Build a custom dataset of game screenshots  
  - Train a CNN classifier  
  - Analyze model performance and mistakes  

---

## 2. Dataset Overview (Edison)
- How we collected screenshots manually  
- Each genre represented with 10 images (initial dataset)
- Five genres chosen:
  - Shooter  
  - Puzzle  
  - RPG  
  - Racing  
  - Strategy  
- Dataset split into:
  - Training set  
  - Test set  
  - Validation set  
- Image resolution normalized to 128×128  
- Small dataset → augmentation planned to improve generalization  

---

## 3. Model Architecture (Angie)
- Simple 3-layer CNN implemented in PyTorch:
  - Conv → ReLU → MaxPool  
  - Conv → ReLU → MaxPool  
  - Conv → ReLU → MaxPool  
  - Flatten → Fully Connected Layers  
- Explanation of design choices:
  - Small CNN appropriate for small-medium dataset  
  - 128×128 input size  
  - CrossEntropyLoss  
  - Adam optimizer, LR = 0.001  
- Trained on Mac MPS   

---

## 4. Training Process (Edison)
- Describe training loop:
  - For each epoch: forward → loss → backward → optimizer.step()  
- Tracking:
  - Training loss  
  - Test loss  
  - Test accuracy  
- Early results from the initial dataset  
- Use of **data augmentation** to increase variability:
  - ColorJitter  
  - Random flips  
  - Random rotations  
  - RandomApply transformations  

---

## 5. Model Performance & Visualizations (Angie)
- Plots:
  - Training vs. test loss over epochs  
- Validation results:
  - Grid of images with predicted labels  
  - Examples of correct vs. incorrect predictions  
  
---

## 6. Discussion & Conclusions (Edison)
- What worked well?
- Challenges:
  - Small dataset → risk of overfitting  
  - Some genres look visually similar  
- What features the CNN seems to rely on:
  - UI elements  
  - Color themes  
  - Camera angle  
- Overall: promising results with limited data  

---

## 7. Future Work (Both)
- Resize dataset to include more screenshots  
- Add more genres  
- Try a deeper CNN or RNN    

---

**End of presentation outline.**
