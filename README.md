# Social-Media-Logger
<h3>An application created as part of learning to work with the Selenium automation tool.</h3> <br>

<b>It allows you to fill in forms on the given pages</b>:
- Facebook<br>
- TikTok<br>
- Instagram<br>
- Youtube<br>
- LinkedIn<br>
- Reddit<br>

The data is taken from the <b>configuration file</b>, where the header corresponds to the name of the page, followed by its url, login and password.<br>
Example of stored data in file:<br>
```python
    [Facebook]
    url=https://www.facebook.com  
    email=test@gmail.com
    password=testing123
```
There is a separate module for each page, which handles its automation.<br>

In addition to this, there is also a separate module which is responsible for reading the browser used by the user,<br> <b>i.e. the browser:</b><br>
- Google Chrome<br>
- Mozilla Firefox<br>
- Microsoft Edge<br>
and extracting the relevant login data for it (ConfigHandling.py).
<br>
To choose browser, just pass one of this three values into config file (Located at bottom of it):<br>

```python
  [Browser]
  name=Mozilla Firefox
```
<br><br>
Unfortunately, the captcha restrictions were not exceeded, but as it is created to consolidate and test Selenium, the application finds and fills in the required forms to log in anyway.
