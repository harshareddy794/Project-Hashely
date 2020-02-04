https://forthebadge.com/images/featured/featured-built-with-love.svg

Project hashely is mainly for hashing and dehashing a string.

In this i have used inbuilt python library called hashlib to hash a string.

For dehashing a string i have stored most commonly used 60,000 hashes in SHA256 and MD5 hash formats in xls sheet.

This script will iterate through all the hases  in the xls file and search whether the hash exist or not.

if hash exist then it will return the corresponding string if not exits it will show data not found.

Note:
Script is developed to dehash 6 lakhs hashes but because of github storage is limited to 25mb per file.
So it is decreased to only 60,000 hashes

==============Steps to follow before running the script==========

1.Open terminal/cmd.

2.Navigate to folder where you downloaded the hashely script.

3.Enter the following command.

    pip3 install -r"requirements.txt"

4.After all the required libraries are installed sucessfully we can run script.
 
============================THANK YOU=========================

copyright @harshareddy794
