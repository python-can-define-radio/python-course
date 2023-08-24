# Imagemagick 🪄

### Introduction

Imagemagick is an incredibly powerful software resource preinstalled to our linux OS which is used to convert between image formats, resize, blur, crop, or combine images.  It can do much more but these are the basics that we will discuss.  Also It does have a graphical user interface but is not difficult to use via terminal commands, which is what we will demonstrate.

To find out if your image format is supported type `convert identify -list format`.

To find out the specifics of your image, type identify + yourfilename, for example, `identify calculate.png`.

For ease of use ensure your terminal working directory is the same as the storage location of the image or images you want to modify.

### Demonstration:

#### examples of reformat:  
Converts .png to .jpg  
`convert calculate.png calculate3.jpg`  
It can even convert to non-image formats like .pdf although this will give you an error due to security policy on our network  
`convert calculate.png calculate4.pdf`  

#### examples of resize:  
Resizes by 50%  
`convert calculate.png -resize 50% calculate2.png`  
Or you can specify your size  
`convert calculate.png -resize 100x100 calculate4.png`  
Stretches the width while shrinking the height  
`convert calculate.png -resize 200%x50% calculate4.png`  

#### example of both:  
Single line to convert and resize  
`convert calculate.png -resize 25% calculate.jpeg`  

#### examble of blur:  
The numbers `5x8` are {radius}x{sigma} controlling the amount of blur.  
You can experiment or look at this link [blurring and sharpening](https://legacy.imagemagick.org/Usage/blur/#blur) for an in-depth explanation.  
`convert calculate.png -blur 5x8 calculate4.png`  

#### example of all three:  
Reformats .png to .jpeg, resizes by 50% and blurs the image  
`convert calculate.png -resize 50% -blur 1x2 calculate4.jpeg`  

#### example of crop:  
The first two numbers `564x83` are the resolution of the new image.  
The second two numbers identify the x,y coordinates where you want to begin the crop.  
Starting from number of pixels from the left `+23` and the number of pixels from the top `+135`.  
Repaging the cropped image will eliminate unneeded data in the resulting image allowing for a smaller file size.  
`convert calculate.png -crop 564x83+23+135 +repage calculate4.png` 

#### example of all four:
Reformats, resizes, blurs, and crops all at once.  
`convert calculate.png -crop 564x83+23+135 -resize 50% -blur 1x2 calculate2.jpeg`  
Notice I moved crop before resize because the resolution of the resized image would be different and we would be cropping the wrong part of the image.

#### example of combine:
Combined 2 or more images into a single image.  
`convert Player.png Enemy.png +append combined.png`  
This is useful in creating a spritesheet used by the arcade module. (images should be close to the same resolution)  
Look [here](https://api.arcade.academy/en/stable/index.html) for more information on the python arcade library.  

[imagemagick documentation](https://imagemagick.org/Usage/)

Note on documentation: On our Ubuntu distribution you can drop the preceding `magick` command and use the commands directly.
