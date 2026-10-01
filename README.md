# ofs-generator

Optical flow steganography generator.

# How to use it

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Then run the generator with an image path:

```bash
python generator.py secret.png
```

The `secret.png` image must be a black-and-white image (mask). The secret is black, and the background is white.

It can be a normal RGB image in any format, but it must contain only two colors (no grays).

# How it works

## 1. Input secret

* Load the user's **secret image**: `secret.png`

  <img src="images/test.jpg" width="100">

* Convert it to an OpenCV mask image: **secret mask image**

  <img src="images/mask.png" width="100">

## 2. Main image

* Create a **random noise image** with the same dimensions as the **secret image**

  <img src="images/noise1.png" width="100">

* Extract **ALL elements inside the secret mask image**. The background is stored in the alpha channel.

  <img src="images/secret_masked.png" width="100">

## 3. Consecutive images

* Clone the original **random noise image**

  <img src="images/noise1.png" width="100">

* Clone the **secret mask image** and move it upwards slightly.

  <img src="images/mask2.png" width="100">

* Remove all pixels from the cloned **random noise image**.

  <img src="images/noise2.png" width="100">

* Fill the empty space with a translated version of the **secret mask image** to create the final image.

  <img src="images/combined.png" width="100">

## Final

We have two images (but any number of images can be used):

<img src="images/noise1.png" width="100"> <img src="images/combined.png" width="100">

Now we can create a GIF with both images to reveal the secret:

<img src="images/secret.gif" width="100">
