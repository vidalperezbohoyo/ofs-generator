# ofs-generator
Optical flow stenography generator

# How to use it

Install the Python dependency:

```
python -m pip install -r requirements.txt
```

Then run the generator with an image path:

```
python generator.py secret.jpg
```
Image "secret.jpg" must be a Black & White image (mask). Secret is black, background is white. Can be a normal RGB image in wathever format but only with two colors (no grays).

