# Imagemagick 🪄

### Introduction

Imagemagick is an incredibly powerful software resource preinstalled to our Linux OS which is used to convert between image formats, resize, blur, crop, or combine images.  It can do much more, but these are the basics that we will discuss.  Also, it does have a graphical user interface, but is not difficult to use via terminal commands, which is what we will demonstrate.

All commands in this lesson are run in the terminal.

To find out if your image format is supported, type `convert identify -list format`.

To find out the specifics of your image, type identify + yourfilename, for example, `identify calculate.png`.

For ease of use, ensure your terminal working directory is the same as the storage location of the image or images you want to modify.

### Demonstration:

#### Examples of reformat:  
Converts .png to .jpg  
`convert calculate.png calculate3.jpg`  
It can even convert to non-image formats, like .pdf. However, this will give you an error on our computers due to security policy.
`convert calculate.png calculate4.pdf`  

#### Examples of resize:  
Resizes by 50%  
`convert calculate.png -resize 50% calculate2.png`  
Or you can specify your size  
`convert calculate.png -resize 100x100 calculate3.png`  
Stretches the width while shrinking the height  
`convert calculate.png -resize 200%x50% calculate4.png`  

#### Example of both:  
Single line to convert and resize  
`convert calculate.png -resize 25% calculate.jpg`  

#### Examble of blur:  
The numbers `5x8` are {radius}x{sigma} controlling the amount of blur.  
You can experiment or look at this link [blurring and sharpening](https://legacy.imagemagick.org/Usage/blur/#blur) for an in-depth explanation.  
`convert calculate.png -blur 5x8 calculate5.png`  

#### Example of all three:  
Reformats .png to .jpg, resizes by 50% and blurs the image  
`convert calculate.png -resize 50% -blur 1x2 calculate.jpg`  

#### Example of crop:  
The first two numbers `564x83` are the resolution of the new image.  
The second two numbers identify the x,y coordinates where you want to begin the crop.  
In the example below, the crop starts `+23` pixels from the left, and `+135` pixels from the top.  
Repaging the cropped image will eliminate unneeded data in the resulting image, allowing for a smaller file size.  
`convert calculate.png -crop 564x83+23+135 +repage calculate6.png` 

#### Example of all four:
Reformats, resizes, blurs, and crops all at once.  
`convert calculate.png -crop 564x83+23+135 -resize 50% -blur 1x2 calculate.jpeg`  
Notice that by putting `-crop` before `-resize`, the cropping coordinates are relative to the original image size. The resolution of the resized image will be different, so cropping after resizing crops a different part of the image.

#### Example of combine:
Combine 2 or more images into a single image.  
`convert Player.png Enemy.png +append combined.png`  
This is useful in creating a spritesheet used by the arcade module. (images should be close to the same resolution)  
Look [here](https://api.arcade.academy/en/stable/index.html) for more information on the python arcade library.  

[imagemagick documentation](https://imagemagick.org/Usage/)

Note on documentation: On our Ubuntu distribution, you can drop the preceding `magick` command and use the commands directly: `convert a b` instead of `magick convert a b`.
