When compared to other plugins, plugins written in c# is able to communicate with the Wox directly. Wox itself is written in c#, so it has the advantage.

Steps for creating a c# plugin:  

* [create `plugin.json` file](plugin_json.html)
* Create plugin solution
  1. Create C# library for plugin（.net framework 3.5）
  2. Add refrence [Wox.Plugin](http://www.nuget.org/packages/Wox.Plugin/) by Nuget
  3. Create a class that implement `IPlugin`:
    ```csharp
    public class Main : IPlugin
    {
      public void Init(PluginInitContext context){}
      public List<Result> Query(Query query){}
    }
    ```  
    * `Init` method will be invoked when Wox loading this plugin. You can do some preparations here. `PluginInitContext` paramter will provide some public API you can use and other userful objects.  

    * `Query` method will be invoked when user acivate this plugin and did search on that. You should return a List of `Result` object. Here is an example of Query method:

    ```csharp
    public List<Result> Query(Query query){
      List<Result> results = new List<Result>();
      results.Add(new Result()
      {
        Title = "Title",
        SubTitle = "Sub title",
        IcoPath = "Images\\plugin.png",  //relative path to your plugin directory
        Action = e =>
        {
          // after user select the item

          // return false to tell Wox don't hide query window, otherwise Wox will hide it automatically
          return false;
        }
        });
        return results;
      }
    ```  
