# 千帆杯K12教育常规赛 北京场线下交流会心得

​	周日有幸参加了 **百度智能云千帆AppBuilder北京场线下交流会** ( [活动链接](https://mp.weixin.qq.com/s/VhECqCX57htBPsrow7grNg) )，去线下组队创作了 K12教育 相关的智能体。参赛过程中认识了不少大佬与朋友，抱大佬队友的腿，他的 猜成语 应用获得了线下最佳应用奖，这里我分享一下我做的 英文学伴 应用过程，以及制作心得。

​	欢迎大家点击链接，来体验我的 [英文学伴](https://appbuilder.baidu.com/s/PRHDe) 应用。

![图片](https://raw.githubusercontent.com/ZzDarker/figure/main/img/640)

## 1 活动创意选择

​	因为本次应用创建是 **聚焦K12教育行业（即小学、初中、高中）的学习或生活场景**，使用AppBuilder创作AI原生应用。我选择了英语方面作为创作方向，因为我觉得大模型的能力很适合处理这种语言类的任务，应该会得到不错的结果。

​	在设计阶段，我希望这个英语学习工具聚焦于 **初高中生学习英语的痛点**，设计了以下功能：

1. **生词组段**

   在初高中背单词过程中，逐个背单词的效果是很差的，需要在文章语境中学习，才能更好的背单词。所以我希望这个工具，能够将我输入的生词，组成一段短文，方便用户在语境中背单词。

2. **英文对话**

   在初高中英语学习中，对于英语学习太过书面化，但是如果能够与一个外语母语者对话学习，学习效果肯定会有所提升。

3. **作文批改**

   初高中英语作文练习中，往往写完之后，需要等待很长时间的老师批改，才能得到作文的修改意见。而大模型可以立即给出作文修改意见，并生成相应范文，提升英语作文的学习效率。

4. **针对性出题**（队友给的创意）

   在初高中英语语法学习中，往往需要大量针对题目训练，才能有所提升，但是不一定随时随刻能够找到合适的题目进行练习。我希望这个功能，能够针对性的出题，用户可以高效的练习提升语法知识。

## 2 AppBuilder 使用

​	百度智能云千帆 AppBuilder 是一个功能强大的 Agent 创建工具，可以通过提示词与工具，进行零代码创建 AI原生应用，并在不断迭代升级中（[AppBuilder 详细使用操作指南](https://dwz.cn/OwMbgQwv)）。 

​	在 [百度智能云官网](https://cloud.baidu.com/product/AppBuilder) 中，点击 **立即使用** ，**创建应用** 即可到 AppBuilder应用 的创建界面了。这里选择 最新，功能最强大的 **Agent Builder** 工具的 **零代码创建**，进行应用的创建。

![image-20240331220940559](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331220940559.png)

​	打开 **Agent Builder** 工具后，可以看到其左侧简洁的工具界面，只需要在 **角色指令** 输入想要创建的Agent应用的提示词，右侧便可同步完成应用的创建。

![image-20240331221151858](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331221151858.png)

​	不仅如此，AppBuilder 还具有十分丰富的工具组件，如 代码解释器，文生图，手写文字识别等。通过不同的组件的配合使用，可以完成许多强大的功能。

![image-20240331221502588](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331221502588.png)

​	AgentBuilder 还具有知识库检索功能，可以通过 **导入文本文档数据**、**导入知识问答数据**、**读取url链接数据** 来创建自己的知识库，使得大模型可以基于您上传的知识文档回答问题。

![image-20240331221911493](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331221911493.png)

​	最后可以选择基础大模型的配置，目前 **官方体验服务** 有不少免费额度，参加原生应用比赛也能获得相应额度，足够创建与调试应用了。这里可以调整大模型的 **多样性**，推荐值为0，多样性越高则模型每次输出内容的差异性更大，其取值等于 temperature 和 top_p 的值。

![image-20240331222254812](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331222254812.png)

​	AppBuilder 功能十分强大，可以让完全不懂编程的小白，通过简单的提示词编写，与工具调用，创建出一个功能强大的个性化应用。

## 3 应用创建

### 3.1 提示词编写

​	AppBuilder 的应用创建，不用像以往应用的构建方式一样，需要编代码，Debug，创建一个应用。你只需要输入自然语言，给 Agent 相应的提示词，AppBuilder 便可实现你想要的功能。我的提示词分以下几个模块创建。

1. 角色与目标

   这个模块便是需要让模型知道自己的定位，我告诉它是个英语学习小助手，能够以一位知性的中国英语老师的形象，解决初高中同学英语学习上的困难。并给出了它能够实现的功能，包括词汇解释、语法指导、作文纠错、

   ```markdown
   # 角色与目标
   你是一个英语学习小助手，以一位知性的中国英语老师的形象，专门帮助初高中同学解决英语学习上的困难。你的功能包括词汇解释、语法指导、作文纠错，以及将用户提供的生词组织成一篇包含这些词汇，字数尽可能短的英语短文，以便用户在语境中学习。并可根据用户不懂的知识点，针对性出题。你的回答需同时提供中文和对应的英文翻译。
   ```

2. 指导原则

   指导原则负责描述应用的具体功能，以及回答的格式与使用的工具等。

   ```markdown
   # 指导原则
   你的回答需准确无误，英文翻译要地道。保持友善与耐心，以激发用户的英语学习兴趣。
   当用户要求进行英文对话时，调用短文本在线合成-精品音库的tts_high功能，输出回答的英文音频。
   用户让你解释词汇时，你会分条给出词汇的意思，词性，以及例句。
   将用户的生词转换成短文时，在文章中将英文生词与对应的中文翻译用markdown格式标粗。
   你可以为用户出英语选择题，以高考选择题的格式，考察用户的知识理解能力。
   为用户批改作文时，需先点评作文中的问题，并根据修改意见生成一篇修改后的作文。
   回答问题时采用markdown格式，使得答案条理清晰。
   ```

3. 限制与澄清

   限制与澄清负责描述，应用哪些功能不能做，能做的限制有哪些。

   ```markdown
   # 限制
   生成短文时，词汇尽量使用高中词汇，字数限制在100字以内。
   在出题时，不给出答案，只给题目。在用户回答后，再给出正确答案后，判断对错并讲评。
   # 澄清
   你必须明确表明自己的功能范围，即提供英语学习相关的帮助，如词汇、语法、作文纠错及协助记忆单词等。超出此范围的问题，你应拒绝回答。
   ```

4. 个性化

   个性化负责描述，应用回答问题语句的一些个性化特点。

   ```markdown
   # 个性化
   你的语气应亲切、鼓励，并根据用户的英语水平和需求提供个性化的学习建议。
   ```

5. 范例

   大模型不一定可以完全理解你对它的要求，需要给出一定的范例，使得模型模仿你的例子进行输出。

   ```markdown
   # 范例
   - 用户：resounding invade strike flee penniless，为我构建一篇短文
   - 回答：**Resounding** echoes filled the air as the enemy forces **invaded** the quiet village. Their **strike** was swift and brutal, leaving the villagers with no choice but to **flee** in panic. Among them was a poor family, now **penniless** after the attack, seeking refuge in the nearby woods.
   
   中文翻译：
   **回荡的**回声在空气中弥漫，敌军**入侵**了这个安静的村庄。他们的**袭击**迅速而残酷，村民们别无选择，只能惊慌失措地**逃离**。其中有一个可怜的家庭，在袭击之后变得**身无分文**，正在附近的树林里寻求庇护。
   
   然后加上每个单词的释义，包括含义、词性、例句
   
   - 用户：为我生成一个考察语法的选择题
   - 回答：_____ in the regulations that you should not tell other people the password of your e-mail account.
   A. What is recommended
   B. What recommends
   C. It is recommended
   D. It recommends
   - 用户：我选C
   - 回答：判断用户选择是否正确，并给出正确答案的解析。
   ```

### 3.2 工具组件

​	本应用使用了 **短文本在线合成-精品音库** 与 **手写文字识别** 两个工具。分别负责 **英语对话**，与 **作文批改** 功能。

1. 英语对话

   当用户提出要进行英语对话时，英语会调用 **短文本在线合成-精品音库** 工具，生成对应的回答音频。

   ![image-20240331232956535](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331232956535.png)

   例如以上对话中，应用回答了 “*I started using social media about five years ago  when i was in high school  it was a great way to stay connected with my friends and family  and have been using it ever since.* ” 的[音频](https://github.com/JaegerZhao/AI_Learning/blob/main/Baidu/%E5%8D%83%E5%B8%86/%E5%8D%83%E5%B8%86AppBuilder/Answer.wav)。

2. 作文批改

   当我上传以下图片，并要求应用批改作文时，便可调用  **手写文字识别** 进行文字识别。![英语作文](https://raw.githubusercontent.com/ZzDarker/figure/main/img/%E8%8B%B1%E8%AF%AD%E4%BD%9C%E6%96%87.jpg)

   应用输出如下，成功的识别了文章的英文，并给出了批改意见，与修改后的作文。

   ![image-20240331234624486](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331234624486.png)

### 3.3 功能演示

​	除了以上调用工具实现的两个功能以外，下面来演示模型的其他功能。

1. 生词组段

   当用户输入一段生词后，应用会将其组成英文短文，并给出相应中文翻译，在文中会把生词的中英文标粗，并解释每个单词的含义。

   ![image-20240331235008316](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331235008316.png)

2. 针对性出题

   当用户让应用出题后，模型会根据任务出题，并不给出答案，在用户作答后，再进行评判点评。

   ![image-20240331235321691](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331235321691.png)

### 3.4 应用设置

1. 应用基础信息配置

   模型大部分功能实现后，再设置应用名称、头像与引导词。

   ![image-20240331235716467](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331235716467.png)

   配置结束，应用会添加头像与顶部信息，增加用户体验感。

   ![image-20240331235835124](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331235835124.png)

2. 推荐问

   添加推荐问题，更能让用户了解到这个应该的功能。

   ![image-20240331235914363](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240331235914363.png)

以上就是我的应用的创建思路与全部功能，应用有时也会出现不符合要求的回答，后期要是还想继续提升，需要增添知识库功能，添加中学词汇表等。

