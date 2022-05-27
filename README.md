# MODNet Background Remover

**Fork only for image removal with output cli option**

## Application

A deep learning approach to remove background and adding new background image

- Remove background from **images**

### Demo

<table>
<tr align="center">
<td><b>Before removing the background</b></td>
<td><b>After replacing the background with new image</b></td>
</tr>
<tr align="center">
<td><img src="assets/sample_image/male.jpeg" alt="Male.jpg" width="460" height="500"/></td>
<td><img src="output/male.png" alt="Male.png" width="460" height="500"/></td>
</tr>
<table>

## Installation

### Python Version

- Python == 3.9

### Virtual Environment

#### Linux

- `python -m venv venv`
- `source venv/bin/activate`

### Library Installation

- Library Install
  - `pip install --upgrade pip`
  - `pip install --upgrade setuptools`
  - `pip install -r requirements.txt`
  - To run in **web interface**
    - `pip install -r web_requirements.txt`

### Pretrained Weights Download
- [Weights Detail](pretrained/README.md)

## Inference

### Image

#### Single image

It will generate the output file in **output/** folder

- `python inference.py --image image_path --output output_path`
- Example:
  - `python inference.py --image assets/sample_image/female.jpeg --output /usr/src/app/output`

## Reference

- [A Trimap-Free Solution for Portrait Matting in Real Time under Changing Scenes](https://github.com/ZHKKKe/MODNet)
- Sample Female photo by <span><a href="https://unsplash.com/@michaeldam?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Michael Dam</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- Sample Male photo by <span> <a href="https://unsplash.com/@erik_lucatero?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Erik Lucatero</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
