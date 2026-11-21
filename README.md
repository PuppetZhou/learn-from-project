# Research Skill Kit

面向科研学习与知识积累的个人 skill 集合。每个 skill 独立完成一种任务，通过简短入口按需读取参考资料。

## Skill 索引

| Skill | 用途 | 调用示例 |
| --- | --- | --- |
| [learn-research-paradigm](skills/learn-research-paradigm/SKILL.md) | 调研新领域，讨论学习路线，再讲授研究范式与工作流 | “用 $learn-research-paradigm 带我入门一个新领域，先调研并讨论适合我的学习路线。” |
| [learn-from-project](skills/learn-from-project/SKILL.md) | 从已有代码和项目理解原理与实现，通过 demo 上手 | “用 $learn-from-project 带我读懂这个项目。” |
| [obsidian-knowledge-curator](skills/obsidian-knowledge-curator/SKILL.md) | 制作通用 Markdown 笔记、补足理解、建立知识关联 | “用 $obsidian-knowledge-curator 整理 PLM 笔记。” |

按学习起点选择：尚未开展项目、需要调研领域时用 `learn-research-paradigm`；已有项目或代码要读懂时用 `learn-from-project`。前者也可解读论文配套代码，无需因此切换 skill。需要“学习后保存为笔记”时，再把主线、例子和来源整理成笔记。三个 skill 均可独立使用。

两个教学 skill 都先按需澄清目标、讨论路线，再逐阶段教学。较长课程可在学习目录保存简短的 `learning-goals.md`，记录目标、进度和支线返回点，帮助跨轮续学；课程记录保存在实际学习目录中。

## 组织方式

```text
research-skill-kit/
├── README.md
├── AGENTS.md
└── skills/
    ├── learn-research-paradigm/
    │   ├── SKILL.md
    │   ├── references/
    │   └── agents/openai.yaml
    ├── learn-from-project/
    │   ├── SKILL.md
    │   ├── references/
    │   ├── assets/
    │   └── agents/openai.yaml
    └── obsidian-knowledge-curator/
        ├── SKILL.md
        ├── references/
        └── agents/openai.yaml
```

`SKILL.md` 写目标和按需索引；`references/` 写分任务指导；`assets/` 存有用的输出案例。只有实际需要自动化时才在相应 skill 下增加 `scripts/`。各 skill 自己选择合适的工作方式和输出结构。

## 使用与维护

当前三个 skill 已通过 `~/.codex/skills/` 下的符号链接安装；直接编辑本仓库即可更新。其他环境可把所需的整个 skill 目录复制或链接到宿主的技能目录，参见 [Codex skill 文档](https://learn.chatgpt.com/docs/build-skills)。

新增 skill 时创建 `skills/<名称>/SKILL.md`，在 YAML 中写 `name` 和 `description`，添加必要参考并更新本页索引。用一个真实任务查看输出，再据反馈调整。无需安装依赖或运行测试框架。

笔记 skill 支持普通本地或服务器目录，历史调用名 `obsidian-knowledge-curator` 保留，便于继续使用。Obsidian 的本机默认库位于 `~/.config/research-skill-kit/local.json` 的 `obsidian.vault` 字段；当次指定的路径优先。

## 来源与版本

项目教学 skill 来自 [PuppetZhou/learn-from-project](https://github.com/PuppetZhou/learn-from-project)，导入提交为 `8bffd4f58935b589b42c99d60acc169b3022029d`，保留原有教学正文、参考、案例与 Git 历史。Obsidian skill 来自本机已有版本，按实际笔记使用反馈迭代；`learn-research-paradigm` 为新领域学习新增。各 skill 的参考来源记在各自目录内。

当前远端 `origin` 仍指向原教学仓库，kit 已合入 `main`。以 `skills/` 为维护源；原教学仓库后续更新可按差异移植。仓库尚未指定开源许可证。
