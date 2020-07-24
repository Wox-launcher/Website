Before I wrote Wox, I always wanted to write a launcher. I like using hotkeys instead of the keyboard, especially after getting used to Vim. `Win + R` in Windows cannot search programs, and that's no good for me. I've also used [Launchy](http://www.Launchy.NET/), but it seems they stopped maintanence a long time ago. Back in 2011, I made some attempts at creating a launcher using C-lang, like [fstart](https://code.Google.com/p/fstart/) and [smartrun](https://code.Google.com/p/smartrun/). Maybe it was because I was new coding at that time, but those attempts failed in the end. Around November 2013 I found [Alfred](http://www.alfredapp.com/), an awesome launcher for Mac. Unfortunately, there is no such thing for Windows :(

  So naturally, I came up with an idea to make a launcher like Alfred. Even the name was initially WinAlfred. I made a [post](http://v2ex.com/t/93922) on V2ex, which has some of the affirmative, later some people got involved in the project. In the middle of developing Wox, I got a warning from Alfred. Because the WinAlfred name contains Alfred, it cannot be used because of their trademark. Finally, Wox come to life.

  # Introduction
  -----------------------------
  Wox is a launcher. You can use it to search local programs and files. It can also search web content by using plugins, such the weather today, what the score of a movie is and so on.

  Wox is open source, available at: [http://www.github.com/qianlifeng/wox](http://www.github.com/qianlifeng/wox), any pull requests and issues are appreciated.

  # System Plugins
  ----------------------------------
  The Wox plugin system is divided into two parts, system plugins and user plugins. System plugins generally does not require keywords (except the Web Search plugin) and the user can't uninstall those system plugins at the moment, they're all built-in plugins. User plugins requires a action keyword. For example, if I want to use the [youdao translator](https://github.com/qianlifeng/Wox.Plugin.Youdao) plugin, then I need to use the `yd` + space + words. The action keyword can be configured, I will show you how you can use shortcuts to simplify this process in the following sections.


  * ** Program Plugin**

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrtwot5lmj20m807maas.jpg)

  The program plugin is so important that I'll need to introduce it first. It's the basic feature of Wox.

  The list of Wox search item has its own weight. Each time you select an item, the weight increases. So when the user searches this item next time, it will be displayed at the top of the list.

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrx1jpdrij20m807m0tg.jpg)

  The search list of Wox programs is mainly obtained from the two places.
  1. Programs in the start menu.

  Wox automatically collects start menu programs.

  2. User-defined locations.

  If you need to index a program that doesn't exist on the start menu, Wox also provides a way for users spcifiy those locations. Just open the settings dialog, and look in 'Setting=>Plugin=>Programs':

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrwuw8m25j20m80go76k.jpg)

  Except the program location, users can also specify file types to index. By default, Wox will index files that ends with `lnk;exe;bat`.

  * ** Color plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrx7z54j7j20m803gq2y.jpg)

  When the user inputs a value that matches a specific condition, Wox will tell you what the color is.

  * ** Control Panel plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrx9znjv9j20m803g3ym.jpg)

  Wox also supports searching in the Control Panel. For example, after entering firewall, Wox finds the firewall option in the control panel.

  * ** Calculator plugin **

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrxc7incnj20m803gglq.jpg)

  Wox has a built-in powerful calculation plugin. Search for formulas that you want to calculate, and you are able to get the results right away.

  * ** URL plugin **

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrxeradmpj20m803ggln.jpg)

  When you copy a website url and want to open this URL, you can open the Wox, paste the URL, and press enter.  

  * **Web search plugin**

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrxsgt1drj20m80aegm7.jpg)

  Wox also offers a system called Web search plugin. Web searches allows users to set a URL that WOx will insert the searched keywords into when the user makes a search. This is usually used for searching Google or Youtube. Google is build-in web search with the action keyword 'g'. When you make a new web search, please remeber to replace the query with `{q}` as the placeholder, this is the placeholder that will be replaced when you do the search.

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrxwxd0xwj20m80goq5o.jpg)

  In Web search, Wox also provides a search suggestions feature, as shown in the figure. Suggestion sources you can select from include Google and Baidu.

  * ** Commandline plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrtig5gbyj20m8090wez.jpg)

  Wox offers an alternative `win+r` that, if you enable it, will replace the default `win+r`. This plugin provides some additional benefits when compared to the original:
    1. the interface is more intuitive and searching is more convenient.  
      `iisreset` for example, will not get any prompt if you're running it in the traditional `win+r` search interface. You can get 'iisreset' hints with Wox if you have run this command before.
    2. the 5 commands that you use most frequently will be displayed directly in the interface

  * ** Folder plugin **

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrxk3oir4j20m803g74c.jpg)

  Wox provides a folder bookmarks function. If you frequently need to access folders, then you can add it to the list of folders. Enter the folder name and you can quickly open the folder. Add settings at: 'Settings=>Plugin=>Folder'.

  * ** System commands plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrxgqz5n1j20m803gaa4.jpg)

  Wox has integrated some system-level commands. For example log off, shutdown, lock, and so on. Specific support matrices can be viewed from the 'Settings=>Plugin=>System Command'.

  * ** user plugins indicator **

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrtg0ec9kj20m8068jrk.jpg)

  As shown in the image above, this plug-in is used to prompt user plugin trigger keyword.

  # User plugins
  ----------------------------

  In addition to the built-in system plugins, Wox also provides a platform for creators to share their custom plugins. [http://www.wox.one/plugin] (http://www.wox.one/plugin)

  At present, Wox supports plugins written in (amongst others) C# and Python. Users can even use C, Ruby, Node.js, and Go to write Wox plugins. If you want to know how to write a Wox plugin, you can go [here] (/en/plugin/create_plugin.html) in the Guide.

  # Theme
  -----------------------------

  ![](http://api.drp.io/files/544a461139f56.png)

  Wox supports themes. You can choose your own favorite theme.

  In addition, we also offer an online theme maker [ThemeBuilder](http://www.wox.one/theme/Builder). Once a theme is configured on the Web site, click download and rename it to the following format: `<your theme name>.xaml`. You can then put this theme file in Theme directory in the root of the Wox directory and restart Wox. After restarting Wox, you can now see new theme in the theme list.

  # Hotkey
  -------------------------------------

  ![](http://api.drp.io/files/544a4878cbb40.png)

  As a keyboard lover, powerful hotkey support is essential to me. In the Wox, hotkeys are divided into two categories. The first one is the predefined hotkey that cannot be changed by the user, 'Ctrl + R' (mentioned above). The others hotkeys can be customized by the user.

  As shown in the image above, custom hotkeys are divided into two parts.
    1. first one is the hotkey that launch Wox. The default Wox primary hot key is 'Alt + space'. If you want to change this setting, you can place the cursor in hotkey input box, and type a shortcut.
    2. the second one is the hotkey settings for queries. For example, I often use the youdao translation plugin, so I added a hotkey `Alt+t` and map it to `yd `, as shown in the following figure:

  ![](http://api.drp.io/files/544a4b2c392df.png)

  ![](http://api.drp.io/files/544a4bed8e627.png)

  After you add the hotkey succesfully. you can use `Alt + t` as a hotkey to activate Wox and enter the `yd `: Then you only need to input the word to be translated. **Note that when setting hotkey keywords, you need to insert an extra space at the end of the action keyword**, because Wox default uses `key + space` as trigger.

  Another very handy custom hotkey is for the [Clipboard plugin](https://github.com/qianlifeng/Wox.Plugin.ClipboardManager), which I mapped to `Ctrl + Shift + v`.

  # Proxy
  ------------------------------------

  ![](http://api.drp.io/files/544a4243dc812.png)

  In the settings window, users can set a HTTP proxy for Wox to use. This feature may be necessary for some business users because their networks are connected through a proxy.

  If the proxy is set, then the 'wpm' commands and all system plugins will use this proxy. Note: If a user plugin author doesn't take proxy information into account, then this user plugin may not support using a proxy. We recommend plugin author always consider proxy users when making plugins.

  # Context menu
  -------------------------------------

  ![](http://api.drp.io/files/544a2c5b85f45.png)

  From [V1.1.0](https://github.com/qianlifeng/Wox/milestones/V1.1.0), Wox supports context menus. If you see a small icon on the right of a search item, that means this item has a context menu. In this case, you simply use `Shift + enter` to enter the menu options. If you want to return to the search interface, just press `Esc`.

  ![](http://api.drp.io/files/544a2d1e2758a.png)

  Menu items provide some optional actions to this search item. For example opening the file with administrator privileges or opening the directory that contains the file and so on.
