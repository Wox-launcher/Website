与其他插件不同的是，c#编写的插件能够直接与Wox通信，能利用的API也最多。因为Wox本身就是c#写的，所以在插件方面有先天优势。  

创建C#插件的步骤如下：  

* [创建`plugin.json`文件](plugin_json.html)
* 创建插件项目
  1. 创建插件C#类库（.net framework 选择 3.5）
  2. 通过Nuget添加[Wox.Plugin](http://www.nuget.org/packages/Wox.Plugin/)引用
  3. 创建一个类并继承`IPlugin`接口，像这样
    ```csharp
    public class Main : IPlugin
    {
      public void Init(PluginInitContext context){}
      public List<Result> Query(Query query){}
    }
    ```  
    `Init`方法会在Wox加载这个插件的时候被调用。你可以在这里执行一些准备工作。`PluginInitContext`对象
    包含了Wox提供的公共API和其他一些对象。
    `Query`方法会在用户激活了该插件并执行搜索的时候调用。你应该返回一个`Result`的对象链表。下面是一个
    简单的Query方法示例：

    ```csharp
    public List<Result> Query(Query query){
      List<Result> results = new List<Result>();
      results.Add(new Result()
      {
        Title = "标题",
        SubTitle = "副标题",
        IcoPath = "Images\\plugin.png",  //相对于插件目录的相对路径
        Action = e =>
        {
          // 处理用户选择之后的操作

          //返回false告诉Wox不要隐藏查询窗体，返回true则会自动隐藏Wox查询窗口
          return false;
        }
        });
        return results;
      }
    ```  
* 测试插件  
  在开发插件的过程中，经常需要测试实际运行效果。推荐将当前插件项目添加到Wox的解决方案中，
  然后直接启动Wox调试，这是最简单的调试方法。
