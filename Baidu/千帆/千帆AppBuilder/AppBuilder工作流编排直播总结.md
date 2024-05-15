# 千帆 AppBuilder 工作流编排功能直播总结

​	上个月，千帆AppBuilder推出了一项引人瞩目的新功能——工作流编排。在官方直播中，百度产品经理不仅深入介绍了这项功能，而且还通过创建多个组件，生动展示了AppBuilder组件工作流的强大功能。今天，我想通过文字的形式，将直播中学习到的宝贵知识记录下来，以便大家能够方便地学习和参考。

> 直播链接：[AppBuilder又上新能力了？直播帮你get工作流编排新功能 - 百度智能云千帆社区 (baidu.com)](https://cloud.baidu.com/qianfandev/live/e69b4777bd)
>
> 官方文档：[工作流创建组件 - 千帆AppBuilder | 百度智能云文档 (baidu.com)](https://cloud.baidu.com/doc/AppBuilder/s/glv0f48qe)

​	官方分别通过创建 菜谱查询组件 与 中考政策查询组件，主要介绍了组件的 API节点 与 知识库节点。

## 1 API节点使用——菜谱查询组件

​	本章介绍通过 聚合平台 的 菜谱API 来构建菜谱查询组件。

1. 创建组件

   输入组件名称与组件描述，选择空画布，进行组件创建。

   ![image-20240514213612753](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514213612753.png)

2. 添加API节点

   菜谱查询组件主要通过调用API完成，首先将节点按下图顺序搭建。

   ![image-20240514213817276](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514213817276.png)

   其中直播中选择了采用 [聚合平台](https://www.juhe.cn/) 的 [菜谱API](https://www.juhe.cn/docs/api/id/733) 来进行调用，构建组件。菜谱API相关参数如下。

   ![image-20240514215506991](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514215506991.png)

3. 编辑API节点

   API节点需要填写基本信息、请求参数、返回参数3栏内容。

   - 基本信息

     接口地址：在这里，我们使用了[聚合api平台](https://www.juhe.cn/)的菜谱api (http://apis.juhe.cn/fapigx/caipu/query) 

     Headers列表：根据要调用的API文档进行设置。

     鉴权方式：采用API Key

     密钥位置：Query

     ![image-20240514214729261](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514214729261.png)

   - 请求参数

     这里的三个请求参数 `word` 、`num`、`page` 也是根据API文档进行设置的。

     ![image-20240514215725374](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514215725374.png)

   - 返回参数

     这里选择了 `object` 类型的 `result` 参数，指获取API的所有返回值，没有进行筛选。

     ![image-20240514215852893](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514215852893.png)

   - API调试

     这里选择通过表单填写进行API调试，在 `word` 中输入"麻婆豆腐"来查找麻婆豆腐的菜谱。

     ![image-20240514220105752](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514220105752.png)

     可以看到接口请求成功，说明API调用成功。

4. 编辑开始节点

   这里是作为API节点的输入来设置参数，通过查询API文档，设置了以下参数。

   ![image-20240514220325981](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514220325981.png)

   设置开始节点参数名后，再修改API节点输入的参数名。

   ![image-20240514220456462](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514220456462.png)

5. 编辑结束节点

   因为调用组件后，大模型会根据组件内容再次优化，这里我们直接返回API输出参数 `result` 即可。

   ![image-20240514220629896](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514220629896.png)

6. 组件调试

   将所有的节点配置完成后，点击调试，填写必要参数，查看组件是否能成功运行。

   ![image-20240514220831589](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514220831589.png)

   发现组件可以成功运行，发布组件即可。

7. 创建应用

   通过AI自动配置创建应用，调用菜谱查询组件，完成菜谱查询应用。

   ![image-20240514223310489](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514223310489.png)

   可以看到，通过调用菜谱查询组件，成功通过提问激活组件，查询到了5种做鱼的菜谱。

## 2 知识库节点使用——中考政策查询组件

​	本章通过构建的 北京中学资料知识库 来构建中考政策查询组件。

1. 知识库建立

   知识库可以通过 **导入网页** 和 **导入文件** 两种方式构建，导入后会根据规则进行分片，用于知识匹配。

   ![image-20240514221513570](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514221513570.png)

   直播中，百度工作人员通过 网页[怎么改？为何改？——北京“新中考”政策解读-新华网 (news.cn)](http://news.cn/2023-09/27/c_1129887730.htm)，与docx文档 北京市教育委员会关于做好2023年高级中等学校考试招生工作的意见 两份文件构建了知识库。

   ![image-20240514221820831](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514221820831.png)

   传入到知识库后，可以看到其自动的切片信息。

2. 组件构建

   输入组件名称与组件描述，选择空画布，设定头像，创建中考政策查询组件。

   ![image-20240514221928994](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514221928994.png)

3. 编辑知识库节点

   通过调整检索策略、召回数量、匹配分，完成知识库参数的设置。其中这三个值的含义如下：

   - **检索策略**：按照指定的检索策略从知识库中寻找匹配的片段，不同的检索策略可以更有效地找到正确的信息，提高最终生成的答案的准确性和可用性。
   - **召回数量**：设置从知识库中召回与输入Query匹配的知识片段的个数，设定的数量越大，召回的片段越多
   - **匹配分**：在检索过程中，用来计算输入Query和知识库片段的相似度，高于匹配分数的片段将会被检索召回

   ![image-20240514222243825](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514222243825.png)

4. 编辑开始节点

   知识库查询有必要让组件看到原始提问，于是勾选了 "包含原始对话" 选项。

   ![image-20240514222530526](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514222530526.png)

5. 编辑结束节点

   同样直接返回参数值，只需要输出的内容，所以设置为知识库输出 `OutputList` 的 `content` 参数。

   ![image-20240514222718606](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514222718606.png)

6. 组件调试

   填写必要参数，进行组件调试。

   ![image-20240514222925069](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514222925069.png)

   可以看到，组件能够回答我们的提问，调用知识库成功。

7. 痛点与解决方案

   AppBuilder 在选择知识库时，只能选择一个知识库，但是可以通过组件的方式，来获取多个知识库的回答。方法就是构建如下工作流，利用分支器做选择，当第一个知识库查询失败时，查询第二个知识库。

   ![image-20240514223107144](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514223107144.png)

8. 创建应用

   通过AI自动生成应用，添加中考政策查询组件，实现中考查询应用。

   ![image-20240514223542745](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240514223542745.png)

   可以看到，应用可以通过相关提问，激活中考政策查询组件，根据知识库回复相关问题。

