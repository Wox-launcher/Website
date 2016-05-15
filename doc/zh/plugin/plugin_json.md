在创建Wox的时候，用户必须在插件的根目录方式一个名为`plugin.json`的文件。该文件中包含了该插件的一些基本信息。在用户上传插件到[getwox.com](http://www.getwox.com)的时候，
我们会读取这个文件中的信息。  

`plugin.json`的格式如下：
**请在粘贴下面代码的时候移除其中的注释**
```
{
  "ID":"D2D2C23B084D411DB66FE0C79D6C2A6H",   //插件ID，32位的UUID
  "ActionKeyword":"wpm",                     //插件默认的触发关键字
  "Name":"WPM",                              //插件名字
  "Description":"Wox Package Management",    //插件介绍
  "Author":"qianlifeng",                     //作者
  "Version":"1.0.0",                         //插件版本，必须是x.x.x的格式
  "Language":"csharp",                       //插件语言，目前支持csharp,python
  "Website":"http://www.getwox.com",         //插件网站或者个人网站
  "IcoPath": "Images\\pic.png",              //插件图标，路径是相对插件根目录的路径
  "ExecuteFileName":"PluginManagement.dll"   //执行文件入口，如果是C#插件则填写DLL路径，如果是pyhton则填写python文件路径
}
```
