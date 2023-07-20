# Making ASCII art with commits' messages on GitHub

## Description

Python scripts for creating ascii arts and uploading it to your GitHub repository given by url,\
so you can tweak your repo not only with excellent README but even by adding ___THIS AMAZING FEATURE___\
to impress everyone visiting your repo.

Unfortunately, font that GitHub uses have different character's width for each character so most of ASCII arts won't look good enough.\
Therefore, I made also scripts for creating ascii arts with these characters that have the same width: █ ▓ ▒ ░.

&nbsp;
## Examples

### Example with ascii art drawn by me

Result:

![01](./examples/01.png)

### Example with ascii art converted from image

Given image:

![image](./image.png)

Result:

![02](./examples/02.png)

You can (probably) see this result by yourself [here](https://github.com/bartekk2908/test_repo.git).

&nbsp;
## Usage

### Setup

To use it you have to install packages from `requirements.txt` file.

### Create ascii art

According to what I mentioned earlier, I recommend you to create new ascii art with my scripts and don't use ascii arts gotten from somewhere else.

You can use `make_ascii_art.py` to draw your simple ascii art by yourself.\
You only have to specify size of ascii art and size of window for drawing.\
Click `LMB` to draw black and `RMB` to drwa white.\
The result will be saved in `ascii_art.txt` file.\
The ascii art created this way is composed of only __two__ different characters. 

You can use `convert_image_to_ascii_art.py` to convert given image to ascii art.\
You only have to specify width of ascii art and path to the image.\
The result will be saved in `ascii_art.txt` file.\
The ascii art created this way is composed of __four__ different characters. 

### Upload ascii art to GitHub repo

Use `ascii_art_github_commits.py` to push fake commits that contain lines of ascii art from `ascii_art.txt` to remote repo.\
You only have to specify the url adres of your repo.

### Remove ascii art from GitHub repo

You can use `delete_last_x_commits.py` to delete fake commits created for ascii art and force to push changes to remote repo.\
You only have to specify the url adres of your repo and number of last commits you want to delete.\
__Please be careful to not delete other commits you don't want to delete!__

&nbsp;
## Inspiration

The project was inspired by [this repository](https://github.com/ozh/rainbow).

&nbsp;