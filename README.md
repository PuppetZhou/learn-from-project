# Research Skill Kit

面向科研学习与知识积累的个人 skill 集合。每个 skill 独立完成一种任务，统一源码、安装与维护方式；只加载当前任务需要的指引。

## 选择 skill

| Skill | 主要交付 | 示例 |
| --- | --- | --- |
| [learn-from-project](skills/learn-from-project/SKILL.md) | 根据当前问题和基础，讲清知识、公式、代码与项目设计，按需引导实操 | “用 $learn-from-project 带我读懂这个 ESM 项目的数据流。” |
| [obsidian-knowledge-curator](skills/obsidian-knowledge-curator/SKILL.md) | 整理可持续查阅的笔记与知识库，统一排版、精简内容、保留逻辑衔接 | “用 $obsidian-knowledge-curator 整理 PLM 笔记，保留公式和承接句。” |

学习知识或代码由教学 skill 处理；整理笔记由 Obsidian skill 处理。用户要求“教会我，并保存为笔记”时，先教学，再把已解释的内容、来源和未决问题交给笔记 skill。两者可以独立安装，没有相互依赖；纯教学不自动写入 vault，纯格式整理不自动扩展为课程。

## 目录与维护原则

```text
research-skill-kit/
├── skills/
│   ├── learn-from-project/
│   └── obsidian-knowledge-curator/
├── scripts/                 安装、状态与结构检查
├── tests/                   管理脚本的文件操作检查
├── docs/                    维护规范与来源记录
├── AGENTS.md                修改本仓库时的约定
└── README.md                面向使用者的索引
```

每个 skill 以 `SKILL.md` 为入口，使用 `references/` 放按需指导，`assets/` 放输出范例，`scripts/` 放必要工具，`agents/openai.yaml` 放界面元数据。按需创建目录，不要求每个 skill 都有脚本或模板。统一的是封装方式，教学过程和笔记结构各自维护。

根目录不是第三个 skill；不为每次调用加载整个 kit，也没有必须读取的公共教学总纲。各 skill 的运行资源都位于自己的目录内，单独复制仍可使用。

## 本地安装

需要 Python 3.10+。在仓库根目录执行：

```sh
python3 scripts/manage.py list
python3 scripts/manage.py install
python3 scripts/manage.py status
```

默认安装到 `${CODEX_HOME:-~/.codex}/skills`，沿用此环境的 skill-installer 位置；其他宿主可指定已支持的发现目录，例如 `--dest ~/.agents/skills`。同一宿主只安装一份，避免重复发现。

安装使用符号链接，指向仓库里的实际目录；源码只有一份，修改后无需复制同步。Codex 支持链接目录并自动检测变化，见[官方 skill 文档](https://learn.chatgpt.com/docs/build-skills)。下个回合可使用新增 skill；若列表未刷新，重启 Codex。

可以只安装一个：

```sh
python3 scripts/manage.py install learn-from-project
```

遇到同名目录时默认停止，不覆盖。确认迁移现有本地安装时执行：

```sh
python3 scripts/manage.py install --replace
```

原目录或旧链接会被移动到安装目录之外的 `skill-kit-backups/<时间戳>/`，终端显示具体位置。重复安装正确链接不产生新备份。仓库移动后，在新位置重新运行 `install --replace` 修复链接。要恢复旧安装，先确认目标是本 kit 的符号链接，仅删除该链接，再把对应备份移回原路径。

## 本机配置

笔记、学习记录、vault 路径和备份不进入本仓库。Obsidian 默认路径保存在 `~/.config/research-skill-kit/local.json`，可选结构为：

```json
{
  "obsidian": {
    "vault": "/absolute/path/to/your/vault"
  }
}
```

用户当次指定的路径优先。没有配置时询问目标；教学 skill 不读取无关的 Obsidian 配置。

## 检查与新增

结构检查需要 PyYAML；建议使用独立环境：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
python3 -m unittest discover -s tests -v
```

新增时在 `skills/<skill-name>/` 创建独立入口和必要资源，更新本页索引及来源记录，然后检查、安装。管理脚本自动发现新的 `SKILL.md`，无需再维护一份机器清单。具体规范与行为验收见[维护指南](docs/maintaining.md)。结构检查不能证明教学效果或科学结论正确。

## 版本与上游

本 kit 从原教学仓库克隆，保留完整 Git 历史，在 `kit/initial` 分支完成目录迁移。来源版本见[来源记录](docs/provenance.md)。当前 Git 远端 `origin` 仍是原教学仓库，尚未创建或推送新的远端。

后续以本 kit 中的 `skills/` 为维护源。原教学仓库继续独立更新时，先 `git fetch origin`，比较对应改动后移植到 `skills/learn-from-project/`；不要直接用原单 skill 根目录覆盖整个 kit。决定将原仓库升级为 kit 或另建 kit 仓库后，再配置正式远端和发布分支。
