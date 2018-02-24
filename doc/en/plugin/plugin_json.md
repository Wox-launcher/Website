When creating Wox, users must create a 'plugin.json' file in the root of plugin folder. This file contains some basic information about the plugin. When user upload plugin to [wox.one](http://www.wox.one),
We will read the information in that file.

The format of `plugin.json` file：  
**Please remove the comments and replace related infos when you copy following config**
```
{
  "ID":"D2D2C23B084D411DB66FE0C79D6C2A6H",   //Plugin ID，32 bit UUID
  "ActionKeyword":"wpm",                     //Plugin default action keyword
  "Name":"WPM",                              //Plugin name
  "Description":"Wox Package Management",    //Plugin description
  "Author":"qianlifeng",                     //Plugin Author
  "Version":"1.0.0",                         //Plugin version，must be x.x.x format
  "Language":"csharp",                       //Plugin language，we support csharp,python and executable now
  "Website":"http://www.wox.one",         //Plugin website or author website
  "IcoPath": "Images\\pic.png",              //Plugin icon, relative path to the pluign folder
  "ExecuteFileName":"PluginManagement.dll"   //Execution entry. Dll name for c# plugin, and python file for python plugin
}
```
