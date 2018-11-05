Wox supports plugin development using Python. Wox comes with a Python environment and its standard library, so the user doesn't need to install a dedicated python environment anymore.

Wox has the `requests` and `beautifulsoup4` library built-in, so plugin makers can use them to access web contents.

You can refer to this project when making a python plugins：[Wox.Plugin.HackerNews](https://github.com/qianlifeng/Wox.Plugin.HackerNews)

Steps to make a python plugin：  

* [Create `plugin.json` file](plugin_json.html)

* Create a python file, here is a simple example:  

```python
#encoding=utf8
import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox,WoxAPI

#Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#The wox class here did some works to simplify the communication between Wox and python plugin.
class Main(Wox):

  def request(self,url):
    #If user set the proxy, you should handle it.
    if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
      proxies = {
        "http":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        "https":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))}
      return requests.get(url,proxies = proxies)
    else:
      return requests.get(url)

  # A function named query is necessary, we will automatically invoke this function when user query this plugin
  def query(self,key):
    r = self.request('https://news.ycombinator.com/')
    bs = BeautifulSoup(r.text)
    results = []
    for i in bs.select(".comhead"):
      title = i.previous_sibling.text
      url = i.previous_sibling["href"]
      results.append({
        "Title": title ,
        "SubTitle":title,
        "IcoPath":"Images/app.ico",
        "JsonRPCAction":{
          #You can invoke both your python functions and Wox public APIs .
          #If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
          #you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
          #just replace xxx with the name provided in this url
          "method": "openUrl",
          #you MUST pass parater as array
          "parameters":[url],
          #hide the query wox or not
          "dontHideAfterAction":True
        }
      })

    return results

  def openUrl(self,url):
    webbrowser.open(url)
    WoxAPI.change_query(url)

  #Following statement is necessary
  if __name__ == "__main__":
    Main()
```

* After you create a plugin, you can copy the plugin to `<WoxDirectory>\Plugins\<YourPluginDirectory>` and restart Wox. You can also upload the plugin to [Wox Plugin](http://www.wox.one/plugin), so other users can find and install your plugin.
