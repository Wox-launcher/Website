在编写Wox插件之前，需要明白Wox使用的插件机制。  

简单来说，Wox与插件之间通过标准输入输出的方式通信，使用[JSONRPC](http://www.jsonrpc.org/specification)来完成通信。使用这种方式，将极大的提高Wox支持的插件种类，
**几乎任何语言**都可以用来编写Wox插件。  

下图展示了Wox与插件之间的通信原理：  

![JsonRPC](images\JSONRPC.png)
