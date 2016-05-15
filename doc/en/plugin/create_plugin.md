Before writing the Wox plugin, we need to understand Wox plugin mechanism.

In simple terms, Wox make communications with the plugins through standard input and output, and use [JSONRPC](http://www.jsonrpc.org/specification) to complete this.Using this approach, Wox will greatly improve the supported plugin types. **Almost** any language can be used to write the Wox plugin.

The diagram below shows how Wox communicate with plugins:

![JsonRPC](images\JSONRPC.png)
