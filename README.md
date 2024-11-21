# OASIS: Object-Domain Artifacts for Skin Image Segmentation - A Computational Pipeline and Synthetic Dataset

An example code to render synthetic images and their corresponding lesion segmentation masks is provided in ```code/render_example.ipynb```. The images can be rendered either without any artifacts or with artifacts, including dark frames, calibration charts, rulers, blood vessels, or hair.

## Setup

- Create and activate Python environment:
   ```
   conda create -n oasis python=3.9
   conda activate oasis
   pip install -r requirements.txt
   ```
