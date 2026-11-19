# 学习设计与参考

只在需要参考笔记方案、示例或学习设计时选读；案例及外部网页均非每次必读。下列是把研究与写作经验用于笔记的设计取舍，不规定统一模板。

## 值得借鉴的笔记与教学材料

本轮于 2026-11-19 查阅下列原始材料，选取适合精炼笔记的做法：

| 材料 | 借鉴什么 | 在这里怎样取舍 |
| --- | --- | --- |
| [Andy Matuschak 的 evergreen notes](https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic) | 围绕一个主题写完整，用关联连接知识 | 保留理解所需上下文，粒度按复用价值判断；无需每个术语单独建页 |
| [Cornell 笔记法](https://lsc.cornell.edu/notes.html) | 提炼线索、回忆与反思 | 需要复习时加少量提示问题；普通 Markdown 无需模拟纸张双栏或每篇强制总结 |
| [The Carpentries 教学设计要点](https://carpentries.github.io/lesson-development-training/instructor/key-points.html) | 按学习目标筛选内容，删去不服务目标的负担 | 先明确这篇笔记回答什么，再决定留下什么，不铺开完整课程 |
| [Software Carpentry：变量与赋值](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html) | 具体知识点连接短代码、结果及解释 | 借鉴局部示范的组织方式，练习数量和课程栏目按笔记用途取舍 |

这些是有明确来源的实践样例和教学指导，并非对所有人的最优模板。使用时以读者能否理解、回看和复用当前知识为准。

## 从学习需要选择写法

| 读者遇到的问题 | 笔记中的处理 | 参考 |
| --- | --- | --- |
| 看懂各段却不知道整体在讲什么 | 按核心问题与知识依赖组织，用标题和承接句显出关系 | [CMU 学习原则](https://www.cmu.edu/teaching/principles/learning.html) |
| 读到新话题突然断开 | 从前文熟悉的对象接到新信息，写明具体联系 | [Harvard：Transitions](https://writingcenter.fas.harvard.edu/transitions) |
| 记住定义，却不会解释公式或方法 | 用同一个小例子连接概念、符号和关键步骤，解释每步的作用 | [IES 学习指导，建议 2、4、7](https://ies.ed.gov/ncee/WWC/PracticeGuide/1/Published) |
| 重读觉得熟悉，离开笔记却想不起来 | 需要复习时，加入一个解释、预测或变式问题；答案可从正文核对，隔一段时间再尝试回忆 | [IES 学习指导，建议 1、5](https://ies.ed.gov/ncee/WWC/PracticeGuide/1/Published) |
| 知识散在多处，不便复用 | 围绕可独立理解的概念聚合，依关系连接；粒度兼顾完整性和复用 | [Andy Matuschak：笔记粒度](https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic) |

CMU 和 IES 提供学习研究的综合指导；Harvard 提供写作指导；Andy 的笔记属于实践经验。本 skill 将其转为笔记编辑建议，复习功能仅在当前任务需要时采用。

## 示例：保留承接关系

已有材料先讲蛋白质序列中的进化信息，随后讨论六个方面。可保留导读：

> 这些进化信息可从结构、功能、相互作用、变异效应、演化历史和环境适应六个方面理解。

再进入各小节。转向文件格式时，可接：

> 前面讨论了序列中可挖掘的进化信息；实际分析还需要区分序列、序列比对和三维结构数据，以及相应的文件格式。

这两句分别交代分类关系和主题转换。分类来自当前材料；其他笔记根据自己的主线写。

## 示例：把抽象定义变成可解释的小例子

```markdown
## 1. Phred 质量分数

质量分数 $Q$ 表示碱基判读的可靠程度；$P$ 是估计的判读错误概率。

$$
Q = -10\log_{10}(P)
$$

例如 Q30 对应 $P = 0.001$，即估计错误概率约为 0.1%。分数每增加 10，估计错误概率降为原来的十分之一。
```

公式依据：[Illumina Q-score 说明](https://knowledge.illumina.com/instrumentation/general/instrumentation-general-reference_material-list/000006557)。这一例中，符号、数值和变化含义已经对应，无需再用代码重复。若用于复习，可以问：“Q20 到 Q30，估计错误概率如何变化？”读者可由公式核对。

## 适用环境

上述内容组织原则适用于普通 Markdown 与 Obsidian。平台专用语法按 [Obsidian 适配](obsidian.md) 选读。
