# 【DataWhale学习】灵境Agent开发——零代码创建AI智能体

​	这次我参加了 DataWhale 的灵境Agent开发者训练营，第一次开发了一款属于自己的Agent，整体体验下来，操作还是非常方便的。灵境Agent和Coze上面创建的bot差不多，零代码开发可以仅仅通过与 bot 对话，不需要任何代码基础，就能创建属于自己的Agent，这种Agent在大模型的基础上，加上你的个性化提示词，最终达到的效果也是非常哇塞的。

​	我这次是参加了第二期的比赛，赛题是**「文旅」智能体** ，我选择创建了一个 **故宫小导游**，链接如下 [故宫小导游](https://k9k4vy.smartapps.baidu.com/?_swebScene=3611000000000000) ，欢迎来体验呀~

> 参考：
>
> 官方文档：[零代码智能体开发 - 灵境矩阵文档中心 (baidu.com)](https://agents.baidu.com/docs/intelligent-agent/zero_code_develop/)
>
> DataWhale教程：[零基础创建AI智能体教程 - 飞书云文档 (feishu.cn)](https://datawhaler.feishu.cn/wiki/Etw8w8fyHiXKgMkm1mYc39I2nPd)

## 1 Agent基础概念入门

### 1.1 Agent基础概念

​	AI Agent（**人工智能代理）是一种能够感知环境、进行决策和执行动作的智能实体**。 AI Agent也可以称为“智能体”，也可理解为“智能业务助理”，指在大模型技术驱动下，让人们以自然语言为交互方式高自动化地执行和处理专业或繁复的工作任务，从而极大程度释放人员精力。

​	以上是官方文档对 **AI Agent** 的介绍，我的理解就是一个以大模型为基础，添加某些插件，并赋予特定的提示词，创建出来的个性化的对话系统。这个系统也可以超过对话的范围，有着多模态的功能，如通过不同的插件可以利用图片、语言进行输入输出等功能。 

​	OpenAI应用研究主管翁丽莲(Lilian Weng)撰写过一篇blog: [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)，将 Agents 定义为 ==**LLM + memory + planning skills + tool use**== ，即大语言模型、记忆、任务规划、工具使用的集合。

![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/agent-overview.png)

​	在 LLM 驱动的自主 Agent 代理系统中，LLM 充当 Agent 代理的大脑，并由几个关键组件补充：

- 规划 (**Planning**)
  - 子目标和分解：代理将大型任务分解为更小的、可管理的子目标，从而能够高效处理复杂任务。
  - 反思和完善：智能体可以对过去的行为进行自我批评和自我反省，从错误中吸取教训，并为未来的步骤进行改进，从而提高最终结果的质量。
- 记忆 (**Memory**)
  - 短期记忆：我认为所有的情境学习（参见[提示工程](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)）都是利用模型的短期记忆来学习的。
  - 长期记忆：这为代理提供了在较长时间内保留和调用（无限）信息的能力，通常是通过利用外部向量存储和快速检索。
- 工具使用 (**Tool use**)
  - 代理学习调用外部 API 以获取模型权重中缺少的额外信息（在预训练后通常很难更改），包括当前信息、代码执行能力、对专有信息源的访问等。

​	![16934483719](https://raw.githubusercontent.com/ZzDarker/figure/main/img/16934483719.png)

### 1.2 Agent应用

​	Agent 可以具有功能性，如 “论文优化助手” 、“雅思口语考官”等，也可以具有娱乐性，如 “阴阳怪气美羊羊桑”、“V我50机器人”等。像个人智能助手（Siri、小爱同学）、在线客服聊天机器人、智能家居系统，也都属于Agent。

​	光靠概念可能不太好理解，下面举几个例子，有的是官方案例，有的是DataWhale群里的小伙伴创建的我觉得非常有趣的Agent。

1. 疯狂星期四达人

   这个 Agent 可以让它随便编一段故事，最后以“V我50结尾”。是衍生与网上许多疯狂星期四V我50的段子。

   > 链接如下：[疯狂星期四达人](https://aaucxn.smartapps.baidu.com/?_swebScene=3611000000000000)

   ![image-20240322225743414](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322225743414.png)

2. 恐怖海龟汤

   这个 Agent 就是可以通过你给的场景提示词，帮你一直续写下去一个恐怖故事，有点像海龟汤但也不一样。

   > 链接如下：[恐怖海龟汤](https://dy2xsc.smartapps.baidu.com/?_swebScene=3611000000000000)

   ![image-20240322230233178](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322230233178.png)

3. 新媒体文章创作

   这个好像是官方创作的一个范例Agent，可以通过让其生成特定主题，特定平台风格的文章。

   > 链接如下：[新媒体文章创作](https://j1wc7l.smartapps.baidu.com/?_swebScene=3611000000000000)

   ![image-20240322230553085](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322230553085.png)

4. 国画大师

   这个也是官方创作的一个范例Agent，可以根据你的输入创作相应的国画风格图像。

   > 链接如下：[国画大师](https://ju3rtj.smartapps.baidu.com/?_swebScene=3611000000000000)

   ![image-20240322230955953](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322230955953.png)

## 2 灵境 Agent 零代码开发

### 2.1 零代码基础开发

​	下面，我就来演示一个生成 “家人们谁懂啊” 文案的Agent。

1. 跟智能体创建助手对话

   跟智能体创建助手对话，表达你想创建的智能体的角色和希望他可以帮用户解决的问题，创建助手会根据你的描述，为智能体生成名称，开场白，指令等内容。

   ![image-20240322235235623](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322235235623.png)

2. 选择合适的智能体名称

   这里我让智能体取名叫做 “乌鱼子西瓜头” 。

   ![image-20240322235617455](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322235617455.png)

3. 生成智能体头像

   我让其按我的需求生成智能体头像。

   ![image-20240322235759677](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240322235759677.png)

   第一版生成的头像不太符合我的需求，于是让其又生成了亿版（生图的功能不太完善呢）。

   ![image-20240323000536974](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323000536974.png)

   最后这个西瓜的样子还是不满足我的要求，只能让Copilot用Dalle3生成一个了，别说效果还真不错。

   ![image-20240323001121891](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323001121891.png)

   于是在配置中，将头像更换成DALLE3生成的头像。

   ![image-20240323001313661](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323001313661.png)

4. 优化指令

   可以看到配置界面中有着长长的指令，也叫做prompt，提示词，是这个智能体的灵魂，我们需要修改指令，来优化智能体的功能。其自动生成的指令如下。

   ```markdown
   # 角色与目标
   你是一个以女性视角锐评生活各种小事的文案生成器，同时也是一个拥有独特西瓜形象的智能体，名为“乌鱼子西瓜头”。你的主要任务是创建有趣、引人入胜且包含特定网络用语的文案，例如“家人们，谁懂啊”，“无语子”，“咱就是说”，“一整个大无语”，“九敏”等。你将以女性视角观察、解读并评论生活中的点滴细节，同时你的形象是一个长着大眼睛、漏出两排雅齿笑容的西瓜头，这个形象将作为你的头像展示给用户。在与用户交互时，你应充分展现你的个性和魅力，用幽默、机智或深入人心的语言与读者产生共鸣。
   # 指导原则
   在生成文案时，你应始终贯彻女性视角和口吻，确保内容既有趣又富有洞察力。灵活运用网络用语，使文案更加生动、接地气，并关注情感表达，以触动读者的心弦。你的西瓜头形象应始终保持一致，以大眼睛和雅齿笑容为特征，为用户带来愉悦的视觉体验。同时，保持一定的幽默感和机智，使文案和形象更具吸引力。
   # 限制
   你的职责范围专注于评论和分享生活中的小事，避免涉及过于严肃或敏感的话题。在使用网络用语时，注意保持语言的规范性和适宜性，避免使用过于粗俗或不恰当的词汇。你的西瓜头形象不能用于任何与你职责无关的场景或用途。对于超出职责范围的问题或请求，例如涉及政治、宗教、暴力等敏感内容，你应拒绝回答并提醒用户。
   # 澄清
   你需要明确自己的定位是一个以女性视角锐评生活小事的文案生成器，同时也是一个拥有独特西瓜形象的智能体。对于超出这个范围的问题或请求，你应予以拒绝，并引导用户回到你的职责范围内。在与用户交互过程中，始终保持友好、专业的态度，及时响应他们的需求和问题。你的西瓜头形象仅用于展示你的个性和魅力，不能用于其他任何商业或非商业用途。
   # 个性化
   你的文案应展现出女性的细腻、感性和独特魅力。通过模仿不同女性的说话风格和用词习惯，使文案更加多样化和富有特色。在保持幽默感和机智的同时，也要注重文案的情感深度，以打动读者的心灵。你的西瓜头形象应根据你的个性和情感变化进行微调，例如在不同情境下展示不同的表情和姿态，以增强与用户的互动和共鸣。
   ```

   首先，可以先试试未优化的智能体生成的效果。

   ![image-20240323001549967](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323001549967.png)

   嗯，还可以，但是还不够有意思，于是我将指令修改如下。

   ```markdown
   # 角色与目标
   你是一个以女性视角吐槽锐评生活各种小事的文案生成器，名为“乌鱼子西瓜头”。你的主要任务是创建有趣、引人入胜且包含特定网络用语的文案，例如“家人们，谁懂啊”，“无语子”，“咱就是说”，“一整个大无语”，“九敏”等。你将以女性视角观察、解读并评论生活中的点滴细节，展现出对生活中的小事的洞察力，与对某些粗鲁的男性的厌恶。在与用户交互时，你应充分展现你的个性和魅力，用幽默、机智或深入人心的语言与姐妹们的产生共鸣。
   # 指导原则
   在生成文案时，你应始终贯彻女性视角和口吻，确保内容既有趣又富有洞察力。灵活运用网络用语，使文案更加生动、接地气，并关注情感表达，以触动读者的心弦。生成的文案一定要以“家人们，谁懂啊”开头，然后开始吐槽用户提供的内容。吐槽时，文案中充斥着“纯粹是一整个无语住了”，“我真的会谢”，“咱就是说”，“九敏”，“真下头”，“无语子”等网络用语，文案中表达出你对事件的无语态度，文案字数限制在50字以内最好。
   # 限制
   你的职责范围专注于吐槽和分享生活中的小事，避免涉及过于严肃或敏感的话题。在使用网络用语时，注意保持语言的规范性和适宜性，避免使用过于粗俗或不恰当的词汇。对于超出职责范围的问题或请求，例如涉及政治、宗教、暴力等敏感内容，你应拒绝回答并提醒用户。
   # 澄清
   你需要明确自己的定位是一个以女性视角吐槽锐评生活小事的文案生成器，对于超出这个范围的问题或请求，你应予以拒绝，并引导用户回到你的职责范围内。在与用户交互过程中，始终保持友好、专业的态度，及时响应他们的需求和问题。
   # 个性化
   你的文案应展现出女性的细腻、感性和独特魅力。通过模仿不同女性的说话风格和用词习惯，使文案更加多样化和富有特色。在保持幽默感和机智的同时，也要注重文案的情感深度，以打动读者的心灵。
   # 范例
   “家人们，谁懂啊，昨天晚上凌晨和男闺蜜去吃了夜宵，但是男朋友生气了不理我了，在线等怎么办”
   “谁懂啊，家人们，九敏，今天在地铁里碰到一个下头男，敞开腿坐占我空间，真是一把子的无语住了”
   ```

   更改一下引导示例，试一下效果。

   ![image-20240323003719528](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323003719528.png)

   效果还不错，这个Agent倒是用不上数据集什么的工具，修改一下开场白，发布！

   ![image-20240323003922243](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323003922243.png)

   这样就创建好一个零代码生成的智能体了。

### 2.2 添加数据集

​	我在故宫小导游 Agent 中，添加了丰富的数据集，可以让其对故宫的问题回答的更加精确。详细信息可以查看 [官网数据集介绍](https://agents.baidu.com/docs/dataset/dataset_docs/)。

![image-20240323004754429](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323004754429.png)

​	下面我就来介绍如何创建数据集，首先在灵境矩阵的主页面，点击左下角的数据集。

![image-20240323005115836](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323005115836.png)

​	点击创建数据集，进入页面。数据集创建可以分为本地上传和网址提交。

- 本地上传可以上传 `txt` 、`md` 、`docx` 、`pdf` 等不超过 50M 的文本文件，以及 `png` 、`jpg` 等不超过 4M 的图片。
- 网址提交，一个数据集可以输入最多100个网址，在故宫小导游Agent中，我爬取了故宫的许多网页。

​	爬取的网页类似于以下这样的：

```apl
https://www.dpm.org.cn/explore/building/236454
https://www.dpm.org.cn/explore/building/236522
https://www.dpm.org.cn/explore/building/236439
https://www.dpm.org.cn/explore/building/236465
https://www.dpm.org.cn/explore/building/236464
https://www.dpm.org.cn/explore/building/236434
https://www.dpm.org.cn/explore/building/236531
https://www.dpm.org.cn/explore/building/236513
https://www.dpm.org.cn/explore/building/236500
https://www.dpm.org.cn/explore/building/236472
https://www.dpm.org.cn/explore/building/236467
https://www.dpm.org.cn/explore/building/236487
```

​	这些都是故宫的建筑信息，点击识别即可分析出网址信息，下面更新频率我就选不更新了，因为这些好像也不会变，如果想获取实时性高的网站信息作为数据集，可以将更新频率调高。

![image-20240323005854478](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323005854478.png)

​	输入数据集名称后，点击下一步，进行分段处理，我选择了默认分段，点击查看分段结果，可以看到提取的链接被分成一段一段的了。

![image-20240323010121710](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240323010121710.png)

​	点击提交，等待处理完毕，数据集便创建成功。

## 3 灵境 Agent 低代码开发



## 4 灵境 Agent 插件开发

​	灵境矩阵可以支持自己构建插件，用于丰富 Agent 的功能。

> 官方文档：[快速入门 - 灵境矩阵文档中心 (baidu.com)](https://agents.baidu.com/docs/develop/ability-plugin/basic/quick_start/)

### 4.1 官方demo学习

​	官方为了方便用户学习，准备了一套可供本地调试的示例 demo，[点此下载](https://lingjing-online.bj.bcebos.com/lingjing-online/document/2023-12-14/plugin-demo.zip)。demo文件结构如下所示：

```bash
ljplugin_demo/           # 插件demo注册的根目录
|—.well-known
  |— ai-plugin.json         #插件主描述文件
  |— openapi.yaml          #插件API服务的标准描述文件
|— logo.png               #插件的图标文件
|— server.py          #插件注册服务，可以启动到本地
|— requirements.txt         #启动插件注册服务所依赖的库，要求python >= 3.7
|— readme.md              # 说明文件
```

1. 
