# 【SD学习】开始绘制你的第一张美图

​	去年其实我已经接触过使用StableDiffusion，但是当时是自己部署的环境，费劲在本地部署完环境后，用基础模型生成几张图之后，感觉也就是那样，就没再尝试了。最近有时间又重新尝试了一下，经过几个月的变迁，StableDiffusion已经有了非常大的变化了，除了以前常用的WebUI，现在还有功能更全面模块化的ComfiUI。

​	除此之外，还有许多插件，从让图生图更加可控的ControlNet，再到可以生成视频的AnimateDiff，还有能控制人物一致性的InstantID，这些都大大提高了StableDiffusion生产的高效性，可控性。而各路大佬们的分享，更是让大家的创意迸发，减少了学习成本，我这周末就是看了B站Nenly同学的SD入门课程，并利用秋叶大佬的启动器，进行SD的入门学习的，这些都是赛博菩萨呀。

​	下面我来记录一下，这个周末我的学习内容。

> 对了，如果你的显存没有8G，建议还是玩MJ吧。

## 1 梦的开始——安装SD的WebUI

​	之前，我安装配置SD，还是需要自己通过Conda配置环境，下载所需的库，解决好多问题，才能成功使用SD的WebUI，使用时还是个白板，也不能随着版本的变动而更新，十分的不方便。但是！有了秋叶大佬的启动器，配置环境就变得那么的简单。详细安装使用视频见 [秋叶大佬的Stable Diffusion整合包 ](https://www.bilibili.com/video/BV1iM4y1y7oA/?spm_id_from=333.788.recommend_more_video.-1&vd_source=0d9448349c913d93662ef6c2456b7d22)，大佬会随着版本的更新而更新整合包的。

​	只需要下载，解压，点击开始运行，安装完相关环境依赖后，就在浏览器中打开了你的WebUI界面。

![image-20240310150003341](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310150003341.png)

​	WebUI是方便用户使用的操作界面，实际上是代码在工作，所以打开了WebUI后记住不要关闭秋叶启动器，那里面的控制台才是你真正的操作。

![image-20240310150358588](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310150358588.png)

## 2 新手村——WebUI的使用

​	想了解WebUI的详细操作，可以去看Nenly同学的教程（[Nenly同学的SD基础教程](https://www.bilibili.com/video/BV1As4y127HW/?spm_id_from=333.999.0.0&vd_source=0d9448349c913d93662ef6c2456b7d22)），非常推荐，讲的十分详细。这里我就简单概括一下WebUI的使用，你用WebUI都能完成哪些任务，怎么完成。

### 2.0 AI绘画圣地——C站

​	在开始的开始，直接讲怎么操作SD实在是太枯燥了，只有看过使用SD能生成多么精美的图，才能有对AI绘画学习的兴趣。

![image-20240310151704287](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310151704287.png)

​	C站是个**专注于AI绘画模型分享与发现的在线平台**。你可以在上面看到大佬们的许多创作，并且想要画出和大佬们一样的作品，只需要在C站下载相应的模型，输入对应的提示词，即可完成创作。

### 2.1 AI绘画的起点——文生图

​	你要是自己输入提示词，生成图片，很有可能得到的结果并不是你想要的，最后就悻悻而归，觉得AI绘画也就这样吧（我之前就是...）。所以，第一步应该是去试验大佬们的提示词，看看他们的作品是怎么生成的。只有在自己电脑上生成了一样精美的图片，你才会提起对AI绘画的兴趣，真正的哇出来。

1. 抄参数

   可以看到上面第一张的美女十分好看，我也想生成一张一样的图片，点击这张图片，看看生图参数是怎么样的。

   ![image-20240310152434105](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310152434105.png)

   可以看到右边有几栏内容，分别是 **Promot** 、**Negativte Promot**，以及 **Model** 和相应参数。点击最底下的`Copy`，可以得到所有相关参数。

   ```
   beautiful lady, (freckles), big smile, ruby eyes, short hair, dark makeup, hyperdetailed photography, soft light, head and shoulders portrait, cover
   Negative prompt: CGI, Unreal, Airbrushed, Digital
   Steps: 5, Size: 832x1216, Seed: 4046791301, Model: Juggernaut_RunDiffusionPhoto2_Lightning_4Steps, Version: v1.7.0, Sampler: DPM++ SDE, CFG scale: 2, Model hash: c8df560d29, Hires steps: 2, Hires upscale: 1.5, Hires upscaler: 4x_NMKD-Siax_200k, Denoising strength: 0.35
   ```

   - **Model**

     ```
     Juggernaut_RunDiffusionPhoto2_Lightning_4Steps
     ```

   首先要下载对应的模型，装载到本地，具体操作看Nenly同学的视频吧。

2. 填写提示词

   下载完模型后，在WebUI选择该模型并填入相应提示词。

   - **Promot**：

     ```
     beautiful lady, (freckles), big smile, ruby eyes, short hair, dark makeup, hyperdetailed photography, soft light, head and shoulders portrait, cover
     ```

   - **Negativte Promot**：

     ```
     CGI, Unreal, Airbrushed, Digital
     ```

   ![image-20240310153029971](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310153029971.png)

3. 填写其他参数

   可以看到还有这些参数需要填写。

   ```
   Steps: 5, Size: 832x1216, Seed: 4046791301, Model: Juggernaut_RunDiffusionPhoto2_Lightning_4Steps, Version: v1.7.0, Sampler: DPM++ SDE, CFG scale: 2
   ```

   含义如下：

   - **Steps：**迭代步数。
   - **Size：**生成图片大小。
   - **Seed：**生图的随机种子。
   - **Sampler：**采样方法。
   - **CFG scale：**提示词引导系数。

   ![image-20240310153759573](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310153759573.png)

   提示词中还有的**Hires**相关参数是指放大相关，咱们先不填写那些，直接生成看看效果。点击右上角橘色的生成按钮，即可等待生成图像。经历以下的过程，即可得到最终图像。

   ![image-20240310153949314](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310153949314.png)

   最终得到如下图像，可以看到，已经非常精美了。

   ![image-20240310154019792](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310154019792.png)

   点击放大，可以看大图像质量还是很不错的，几年前谁能想到这是AI生成的图片，即使能想打，哪能知道这竟然是动动手指就可以产出的图片。

   ![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/00000-4046791301.png)

4. 图片放大

   虽然以上生成的图片，已经可以让人哇塞了，但是有些细节还是比较模糊的，可以看到原作者的参数里面还有某些放大参数。

   ```
   Hires steps: 2, Hires upscale: 1.5, Hires upscaler: 4x_NMKD-Siax_200k, Denoising strength: 0.35
   ```

   - **Hires steps：**高分迭代步数。
   - **Hires upscale：**放大倍数。
   -  **Hires upscaler：**放大算法。
   - **Denoising strength：**重绘幅度。

   填写以上参数，重新绘制，即可得到一张高清大图。

   ![image-20240310161012370](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310161012370.png)

   当然，也有办法不用直接生成，可以点击未放大的图片的右下角的小星星，可以直接放大你这张图。

   ![image-20240310154801529](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240310154801529.png)

   得到的结果十分惊艳！

   ![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/00001-4046791301.png)

这样你的第一张美图就成功生成了，现在可以去C站或其他平台，看看不同模型不同提示词生成的作品都是什么样的啦，自己摸索才是AI绘图的乐趣！

### 2.2 AI绘画出圈——图生图

​	上面咱们体验完了文生图，