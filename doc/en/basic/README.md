Before written Wox, I always wanted to write a launcher. I like to using hotkeys instead of keyboards, especially after using Vim. `Win + R` inside Windows cannot search programs, not good for me. I also used [Launchy](http://www.Launchy.NET/), but it seems stopped maintanence for a long time. Back to 2011, I tried to using C-lang to make some attempts, like [fstart](https://code.Google.com/p/fstart/) and [smartrun](https://code.Google.com/p/smartrun/). Maybe I'm a new guy to coding at that time, those attempts failed at the end. Probably in November 2013, I know [Alfred](http://www.alfredapp.com/), an awesome launcher in Mac. Unfortunately, there is no such thing under Windows :(

  So, naturally, I came up an idea that making a launcher like Alfred, even the name initially was made as  WinAlfred. I made a [post](http://v2ex.com/t/93922) on V2ex, which has some of the affirmative, later some people get involved in the project. In the middle of the developing Wox, I was warned by Alfred. Because the WinAlfred name contains Alfred, and cannot be used because that's their trademark. Finally, Wox come.

  # Introduction
  -----------------------------
  Wox is a launcher. You can use to search local programs, files. It can also search web content by using plugins, such as how is the weather today, what's the score of xxx movie and so on.

  Wox is open sourced at: [http://www.github.com/qianlifeng/wox](http://www.github.com/qianlifeng/wox), any pull requests and issues are appreciate.

  # System Plugin
  ----------------------------------
  Wox plugin system is divided into two parts, the system plugins and user plugins. System plugin generally does not require keywords (except Web Search plugin) and user can't uninstall those system plugins now, they all built-in plugins. User plugin requires a action keyword. For example, I want to use the [youdao translator](https://github.com/qianlifeng/Wox.Plugin.Youdao) plugin, then you need to use the `yd` + space + words. The action keyword can be configured, and I will introduce how to use shortcuts to simplify this process in the following sections.


  * ** Program Plugin**

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrtwot5lmj20m807maas.jpg)

  Program plugin is so important that I need to introduced first. It's the basic feature of Wox.

  List of Wox search item has its own weight. Each time you select an item, the weight increases. So when user search this item next time, it will be displayed at the top of the list.

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrx1jpdrij20m807m0tg.jpg)

  Search list of Wox programs is mainly obtained from the two places.
  1. Programs in the start menu.

  Wox automatically collects start menu programs.

  2. User-defined locations.

  If users need to index program that doesn't exist on the start menu, Wox also provides a way for users spcifiy those locations. Just open setting dialog, and in the 'Setting=>Plugin=>Programs':

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrwuw8m25j20m80go76k.jpg)

  Except the program location, users can also specify file types to index. By default, Wox will index files ends with `lnk;exe;bat`.

  * ** Color plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrx7z54j7j20m803gq2y.jpg)

  When user input value that matches a specific condition, Wox will tell you what the color is.

  * ** Control Panel plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrx9znjv9j20m803g3ym.jpg)

  Wox also supports search in Control Panel. For example, after entering the firewall, Wox searches out the firewall option in the control panel.

  * ** Calculator plugin **

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrxc7incnj20m803gglq.jpg)

  Wox built-in powerful calculation plugin. Search formulas that you want to calculate in the Wox, and you are  able to get the results right away.

  * ** URL plugin **

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrxeradmpj20m803ggln.jpg)

  When you copy a website url and want to open this URL, you can open the Wox, paste, enter.  

  * **Web search plugin**

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrxsgt1drj20m80aegm7.jpg)

  Wox also offers a system called Web search plugin. So-called Web searches allows users to set a URL, Wox will then replace the searched keywords when user make a search. This is usually used in Google, Youtube search. Google is a build-in web search. Action keyword is 'g'. When you make a new web search, please remeber to replace the query to `{q}` as the placeholder, this placeholder will be replaced in the real search.

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrxwxd0xwj20m80goq5o.jpg)

  In Web search, Wox also provides search suggestions feature, as indicated in the figure. Suggest sources to select Google or Baidu.

  * ** Commandline plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrtig5gbyj20m8090wez.jpg)

  Wox offers an alternative `win+r`, if you enable it, it will replace the default `win+r`. This plugin provides some additional benefits when compared to the original's:
    1. the interface is more intuitive, searching is more convenient.  
      `iisreset` in this case, it will not get any prompt if your running it in  traditional `win+r` search interface. But you can get 'iisreset' the hints in the Wox, if you have run this command before.
    2. the 5 commands that you use frequently will be displayed directly in the interface

  * ** Folder plugin **

  ![](http://ww4.sinaimg.cn/large/5d7c1fa4jw1elrxk3oir4j20m803g74c.jpg)

  Wox provides folder bookmarks function. If you frequently need to access folders, then you can add it to the list of folders. Directly after the search folder name you can quickly open the folder. Add settings at: 'Settings=>Plugin=>Folder'.

  * ** System commands plugin **

  ![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elrxgqz5n1j20m803gaa4.jpg)

  Wox integrated some system-level commands. For example, log off, shutdown, lock, and so on. Specific support matrices can be viewed from the 'Settings=>Plugin=>System Command'.

  * ** user plugins indicator **

  ![](http://ww2.sinaimg.cn/large/5d7c1fa4jw1elrtg0ec9kj20m8068jrk.jpg)

  As shown in the image above, this plug-in is used to prompt user plugin trigger keyword.

  # User plugins
  ----------------------------

  In addition to built-in system plugins, Wox also provides platform for creators to share their plugins. [http://www.getwox.com/plugin] (http://www.getwox.com/plugin)

  At present, the Wox supports plugin written by (but not limited) to 'C#' and 'Python', users can even use 'C','Ruby','Nodejs','Go' languages to write Wox plugin. If you want to know how to write Wox plugin, you can go to [here] (/en/plugin/create_plugin.html) in the Guide.

  # Theme
  -----------------------------

  ![](http://api.drp.io/files/544a461139f56.png)

  Wox supports themes. You can choose your favorite theme.

  In addition, we also offer an online theme maker [ThemeBuilder](http://www.getwox.com/theme/Builder). Once theme is configured on the Web site, click on download, and rename it as following format: `<your theme name>.xaml`. You can then put this theme file in Theme directory in the root of Wox directory and restart the Wox. After restart Wox, user can see new theme in the theme list.

  # Hotkey
  -------------------------------------

  ![](http://api.drp.io/files/544a4878cbb40.png)

  As a keyboard lover, powerful hotkey support is essential. In the Wox, hotkeys are divided into two categories. The first one is those hotkeys have been defined, and cannot be changed by the user, such as 'Ctrl + R' mentioned above. The others is those user can customize, which I will describe below.

  As shown in the image above, custom hotkeys divided into two parts.
    1. first one is the hotkey that launch Wox. Wox default primary hot key is 'Alt + space '. If you want to change this setting, you can place the cursor in hotkey input box, and then type a shortcut key.
    2. the second one is the hotkey settings for queries. For example, I often use the youdao translation plugin, so I added a hotkey `alt+t` and map it to `yd `, as shown in the following figure:

  ![](http://api.drp.io/files/544a4b2c392df.png)

  ![](http://api.drp.io/files/544a4bed8e627.png)

  After you add the hotkey succesfully. you can use `Alt + t` hotkey, Wox will be activated and enter the `yd `, you only need to input word to be translated immediately. **Note that when set hotkeys keywords, you need to insert an extra space at the end of the action keyword**, because Wox default use `key + space` as trigger.

  Another very handy custom hotkeys is [Clipboard plugin](https://github.com/qianlifeng/Wox.Plugin.ClipboardManager), I mapped it to `Ctrl + Shift + v`.

  # Proxy
  ------------------------------------

  ![](http://api.drp.io/files/544a4243dc812.png)

  In the settings window, users can set HTTP proxy for Wox. This feature may be necessary for some business users because their networks are connected through a proxy.

  If the proxy is set, then the 'wpm' commands and all system plugins will use this proxy. Note: If user plugin author did not take proxy information into account, then this user plugin is not support proxy. So, we recommend plugin author always consider proxy when you making your plugin.

  # Context menu
  -------------------------------------

  ![](http://api.drp.io/files/544a2c5b85f45.png)

  From [V1.1.0](https://github.com/qianlifeng/Wox/milestones/V1.1.0), Wox supports context menu function. If you can see a small icon on the right of search item, that means this item has context menus. In this case, you simply use the `Shift + enter` to enter the menu options. If you want to return to the search interface, just press `Esc`.

  ![](http://api.drp.io/files/544a2d1e2758a.png)

  Menu item provide some optional actions to this search item. For example, opens the file with administrator privileges or open the directory that contains the file and so on.
