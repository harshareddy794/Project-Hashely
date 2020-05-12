[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-150x25.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

## Introduction
Project hashely is mainly for hashing and dehashing a string.

In this i have used inbuilt python library called hashlib to hash a string.

For dehashing a string i have stored most commonly used 60,000 hashes in SHA256 and MD5 hash formats in xls sheet.

This script will iterate through all the hases  in the xls file and search whether the hash exist or not.

if hash exist then it will return the corresponding string if not exits it will show data not found.

Note:
Script is developed to dehash 6 lakhs hashes but because of github storage is limited to 25mb per file.
So it is decreased to only 60,000 hashes

## Setup

1.Open terminal/cmd.

2.Navigate to folder where you downloaded the hashely script.

3.Enter the following command.

    pip3 install -r"requirements.txt"

4.After all the required libraries are installed sucessfully we can run script.

## Aknowladegment
Thank you everyone for making this happen

copyright @harshareddy794
