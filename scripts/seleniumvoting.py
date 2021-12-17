from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import FirefoxProfile  # editible firefox profile stuff
import datetime, time, os, socket, sys

# get some external inputs and make some variables for later use
# servername = sys.argv[1]  # e.g. ragss12500
# serveradmin = sys.argv[2]  # e.g. siteadmin
# adminpassword = sys.argv[3]  # e.g. adminadmin
# authentication = sys.argv[4]  # e.g. PKI,LDAP
# vmos = sys.argv[5]  # e.g. Windows, Linux
# serverhome = "https://" + servername + ":6443/arcgis/admin/data"
serverurl = "https://voting.voot.com/vote/ec324230-02f2-11eb-bf8c-d128fef771cc?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiJzOGk0cHZvcFpNVXRicDFLTmRqWXBoVkdzNG8xIiwidXNlck5hbWUiOiIiLCJsb2dpblByb3ZpZGVyIjoiR29vZ2xlIiwibmFtZSI6IiIsImVtYWlsIjoid3JjbG91ZGRyaXZlQGdtYWlsLmNvbSIsIlVESUQiOiJzOGk0cHZvcFpNVXRicDFLTmRqWXBoVkdzNG8xIiwiZXh0cmFEYXRhIjoidm9vdCIsImlhdCI6MTYwNDA4NjU3OX0.wfcACBrpxSbvMQnSmCGfQiwO61Fo52AhwbnxnBxVHTo&uid=s8i4pvopZMUtbp1KNdjYphVGs4o1&platform=web"

# firefoxprofile


# Create a new instance of the Firefox driver
while True:
    profile = webdriver.FirefoxProfile()
    profile.default_preferences["webdriver_assume_untrusted_issuer"] = True
    profile.default_preferences["webdriver_accept_untrusted_certs"] = True
    profile.update_preferences()
    driver = webdriver.Firefox(profile)
    driver.set_window_size(1080,1080)
    # Wait for 30 seconds to locate elements before failing
    driver.implicitly_wait(30)

    # open the server admin page
    driver.get(serverurl)
    driver.find_element_by_xpath("//img[@src and @alt='Rakhi']").click()

    driver.find_element_by_xpath("//button[@class='jss190']").click()
    time.sleep(30)
    driver.quit()

