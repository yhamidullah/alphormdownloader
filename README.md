# alphormdownloader
Automated script for downloading all course videos in Alphorm.com

# install requirements 
pip install selenium bs4

# Download and set up webdrivers
### Download your selected driver and copy it into driver folder.
You can find it on the following links :
- Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads (supported)
- Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ (not tested)
- Firefox:	https://github.com/mozilla/geckodriver/releases (supported)
- Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/ (not tested)

### Set the driver path
Edit config.py and fill out the corresponding driver path (one is enough).

# Set up credentials 
Edit config.py find the email and password line then change it to your own account.

# Set up courselist
Edit config.py find the course list line, add your course list as much as you want but beware of robot checking, better to put a reasonable number.

add the course link inside the array brackets like : https://www.alphorm.com/tutoriel/formation-en-ligne-excel-2016-niveau-expert-2-2
separate by comma.



