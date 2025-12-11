# Project Title - Predicting Video Game Genres

## Authors
Angie Avalos Joel, Edison Fuh

---

# Description of Question / Research Topic
Can the genre of a video game be predicted by screenshots taken during gameplay? Do the contents of the screenshot change the likelihood of correct identification? What are some other contributing factors to incorrect classification? Are some genres easier to confuse with other genres? What are some of the easiest to identify genres?

---

# Project Outline / Plan

---

## Data Collection Plan

### Edison
For higher quality screenshots, I will self-capture data from my own game libraries(s). Each game will have multiple screenshots taken, and proportions of genres should be roughly similar. To fill in spots of the data, screenshots from official promotional material could be used. Additionally, UI screenshots could be taken from longplay-style videos or streams, as they do not usually appear in promotional material or regular videos.


### Angie
I will help gather additional images from open datasets and online sources like Kaggle. I will organize the dataset structure (e.g., one folder per genre) and handle preprocessing: resizing, normalization, and train/test splits. If time allows, I'll implement basic data augmentation (rotations, brightness adjustments) to improve model robustness. 

---

## Model Plans

### Edison
Likely something close to being a CNN will be used, since it doesn't seem like there are any more classification models being used in class, with RNNs being the exception, though they might not be applicable. Additionally, if possible and if time permits, I will try to create a tool that automatically tries permutations on the model to create an optimal model.


### Angie
I will build and evaluate a CNN using PyTorch. I'll test different optimizers (Adam, SGD) and compare performance. I will also implement visualization tools to show sample predictions and analyze misclassifications.

---

## Project Timeline

| Week #  | Task |
|---------|------|
| Week 9  | Finalize project idea & repo setup |
| Week 10 | Data collection begins | 
| Week 11 | Data preprocessing & cleaning | 
| Week 12 | Model building & training | 
| Week 13 | Model evaluation & visualization |
| Week 14 | Write analysis notebook |
| Week 15 | Finalize README, Model Card, and presentation slides |


---

## Future Work

- Larger Models
- More data
- Pre-trained model integration
- More genres
- Better visualization utilities (HTML, Non-notebook Python Script, etc.)

---

## Requirements
- The regular CS-171 suite of Python 3.12 packages should suffice:
    - numpy
    - matplotlib
    - pytorch
    - torchvision
    - pandas
    - netCDF4
    - scipy
    - scikit-learn
    - jupyter
    - jupyterlab
    - ipykernel

---

## Data Access
- Record your own footage or take your own screenshots, the processing/processing_edison.ipynb file should be relatively straightforward to use to normalize them

### Data Structure

- input_images | This is where you should place your test and train images
    - test
    - train
- processing
    - input
        - images | Place images to be processed here, as well as images from video processing
        - video | Place videos in here
    - output

---

## License
This project is licensed under the GNU General Public License. See the LICENSE file for more details.
