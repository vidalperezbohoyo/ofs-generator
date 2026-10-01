# ofs-generator
Optical flow stenography generator

# How to use it

Install the Python dependency:

```
python -m pip install -r requirements.txt
```

Then run the generator with an image path:

```
python generator.py secret.png
```
Image "secret.png" must be a Black & White image (mask). Secret is black, background is white. Can be a normal RGB image in wathever format but only with two colors (no grays).

# How works
## 1. Input secret
- Load the user **secret image**: "secret.png"  
<img src="images/test.jpg" width="100">
- Converts to open cv mask image: **secret mask image**  
<img src="images/mask.png" width="100">
## 2. Main image
- Creates **random noise image** with the same dimensions as **secret image**  
<img src="images/noise1.png" width="100">
- Extract ALL elements inside the **secret mask image**. Background is alpha channel  
<img src="images/secret_masked.png" width="100">
## 3. Conscutive images
- Clones the original **random noise image**  
<img src="images/noise1.png" width="100">
- Clone the **secret mask image** and move it upwards a little bit  
<img src="images/mask2.png" width="100">  
- Remove all pixels from the cloned **random noise image**  
<img src="images/noise2.png" width="100">
- Fill that empty space with a translated version of **secret mask image** to have the final image  
<img src="images/combined.png" width="100">

## Final
We have 2 images (can be wathever number of images):  
<img src="images/noise1.png" width="100"> <img src="images/combined.png" width="100">

Now we can make a gif with both and reveal the secret:  
<img src="images/secret.gif" width="100">