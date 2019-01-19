# FGO_Battle

__Check out [FGO-One](https://github.com/Meowcolm024/FGO-One) for the latest version :)__  

## About the project

In short, this project is a auto battle script for the game
Fate/Grand Order.  
The script mainly consists three parts: 
* interface recognition
* card priority calculation
* conducting

The interface recognition part is mainly related to 
OpenCV, which is the module "cv2"(or opencv-python)  
And the algorithm is mainly from this 
[picture](https://upload-images.jianshu.io/upload_images/13678149-b63bcf30df4684f2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  
The last part obviously is the part which combine the parts 
mentioned above

## How to use

1. use the following command to check whether adb is installed
    ```
    adb devices
    ```
    if not, install it via Homebrew
    ```
    brew cask install android-platform-tools
    ```

2. clone the repository
    ```
    git clone git@github.com:Meowcolm024/FGO_Battle.git
    ```
   
3. connect you Android phone with USB Debugging __ON__, then 
run _"main.py"_

## Something else

The templates are from Fate/GO(Chinese version), if you're using
other versions, please change them QWQ

The coordinates in the script ares based on screenshots from
_Huawei Mate 10 Pro_ with a resolution of 2160x1080, you may 
need to change some parameters if your phone is not this resolution. QAQ  
Just run _"test.py"_ then you could get the coordinates of the cards
and compare it with the existed data to check whether a modification is needed

## Known issues

Recognition may not be 100% correct. Thus, the action the script has
taken may not be the best choice(especially in complicated scenarios)
