# Research Skill Kit

面向科研学习与知识积累的个人 skill 集合。每个 skill 独立完成一种任务，通过简短入口按需读取参考资料。

## Skill 索引

| Skill | 用途 | 调用示例 |
| --- | --- | --- |
| [learn-from-project](skills/learn-from-project/SKILL.md) | 学知识、公式、代码与项目设计，按当前基础讲解和实操 | “用 $learn-from-project 带我读懂这个项目。” |
| [obsidian-knowledge-curator](skills/obsidian-knowledge-curator/SKILL.md) | 整理学习笔记、补足理解、建立知识关联 | “用 $obsidian-knowledge-curator 整理 PLM 笔记。” |

需要“学习后保存为笔记”时，先讲清知识，再把主线、例子和来源整理成笔记。各 skill 也能单独使用。

## 组织方式

```text
research-skill-kit/
├── README.md
├── AGENTS.md
└── skills/
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

当前两个 skill 已通过 `~/.codex/skills/` 下的符号链接安装；直接编辑本仓库即可更新。其他环境可把所需的整个 skill 目录复制或链接到宿主的技能目录，参见 [Codex skill 文档](https://learn.chatgpt.com/docs/build-skills)。

新增 skill 时创建 `skills/<名称>/SKILL.md`，在 YAML 中写 `name` 和 `description`，添加必要参考并更新本页索引。用一个真实任务查看输出，再据反馈调整。无需安装依赖或运行测试框架。

Obsidian 的本机默认库位于 `~/.config/research-skill-kit/local.json` 的 `obsidian.vault` 字段；当次指定的路径优先。

## 来源与版本

教学 skill 来自 [PuppetZhou/learn-from-project](https://github.com/PuppetZhou/learn-from-project)，导入提交为 `8bffd4f58935b589b42c99d60acc169b3022029d`，保留原有教学正文、参考、案例与 Git 历史。Obsidian skill 来自本机已有版本，按实际笔记使用反馈迭代；两者的参考来源记在各自目录内。

当前远端 `origin` 仍指向原教学仓库，kit 改造位于 `kit/initial` 分支。以 `skills/` 为维护源；原教学仓库后续更新可按差异移植。仓库尚未指定开源许可证。
