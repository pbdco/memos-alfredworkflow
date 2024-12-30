# Alfred Memos Workflow

An [Alfred](https://alfred.app/) workflow for quickly creating notes in your [Memos](https://www.usememos.com/) ([usememos.com](https://www.usememos.com/)) instance.

![image](https://github.com/user-attachments/assets/51682501-47d6-4511-b52d-e259ca605b11)

![image](https://github.com/user-attachments/assets/768e0129-8f40-4c2d-ab2b-e2b90e11f07f)

## Download

**[Download workflow from here](https://github.com/pbdco/memos-alfredworkflow/releases/latest/download/Memos.alfredworkflow)**

## Features

- [x] Quickly create new memos from Alfred
- [x] Optional and default tag support

Coming Soon:

- [ ] List recent memos
- [ ] Search memos

## Installation

1. Download the latest release from the [releases page](https://github.com/pbdco/memos-alfredworkflow/releases)
2. Double click the downloaded `.alfredworkflow` file to install it in Alfred

## Configuration

After installation, you'll need to configure:

1. Your Memos instance URL
2. Your access token (if required)
3. (Optional) Default tag(s) via `MEMOS_DEFAULT_TAG` environment variable
   - Single tag: `MEMOS_DEFAULT_TAG=CLI`
   - Multiple tags: `MEMOS_DEFAULT_TAG=CLI,Alfred,Quick`

These can be configured in Alfred's workflow configuration panel.

## Usage

In Alfred, type:
- `m` or `memo` or `memos` followed by your note text to create a new memo
- Optionally, add tags with -t (Separate by comma multiple tags)

Notes:
- Default tags from `MEMOS_DEFAULT_TAG` optional workflow setting will be automatically appended to all memos
- You can combine default tags with command-line tags

## Example:

- Create memo:

`memo Hi! From Alfred`

- Create memo with tags:

`memo Hi! From Alfred -t HelloWorld,Testing`

*If MEMOS_DEFAULT_TAG=Alfred, tags will be: #Alfred #HelloWorld #Testing*

- Open your memo webpage in the browser with:

`memos open`

## Requirements

- Alfred 5 with Powerpack
- Python 3.x (included with macOS)
- Internet connection to access your Memos instance

## License

MIT License 
