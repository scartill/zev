# Zev 🔍

[![PyPI version](https://badge.fury.io/py/zev.svg)](https://badge.fury.io/py/zev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Zev helps you remember (or discover) terminal commands using natural language.

![Description](./.github/demo.gif)

## 🔧 Installation

```bash
pip install zev
```

This project runs on top of the OpenAI API. After your first time running it, you will be prompted to enter an OpenAI key.

## 🎮 Usage

#### Option 1: Interactive Mode

```bash
zev
```

#### Option 2: Direct Query

```bash
zev '<what you want to do>'
```

## 📝 Examples

```bash
# Find running processes
zev 'show all running python processes'

# File operations
zev 'find all .py files modified in the last 24 hours'

# System information
zev 'show disk usage for current directory'

# Network commands
zev 'check if google.com is reachable'

# Git operations
zev 'show uncommitted changes in git'
```

## ⚙️ Settings

You can update your OpenAI API key or other settings by running:

```bash
zev --setup
```

To use the OpenAI key, you must have an OpenAI account and a subscription. You can create an API key on [this page](https://platform.openai.com/settings/organization/api-keys).

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
