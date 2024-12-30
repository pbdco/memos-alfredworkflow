# Alfred Memos Workflow

An Alfred workflow for quickly creating notes in your Memos instance.

## Features

[x] Quickly create new memos from Alfred
[x] Direct integration with your Memos instance

Coming Soon:

[ ] List recent memos
[ ] Search memos

## Installation

1. Download the latest release from the [releases page](../../releases)
2. Double click the downloaded `.alfredworkflow` file to install it in Alfred

## Configuration

After installation, you'll need to configure:

1. Your Memos instance URL
2. Your access token (if required)
3. (Optional) Default tag via `MEMOS_DEFAULT_TAG` environment variable

These can be configured in Alfred's workflow configuration panel.

## Usage

In Alfred, type:
- `m` or `memo` or `memos` followed by your note text to create a new memo
- Optionally, add tags with -t (Separate by comma multiple tags)

Notes:
- If `MEMOS_DEFAULT_TAG` is set, it will be automatically added to all memos
- Additional tags specified with `-t` will be combined with the default tag

## Example:

- Create memo:

`memo Hi! From Alfred`
# If MEMOS_DEFAULT_TAG=CLI, tags will be: #CLI

- Create memo with tags:

`memo Hi! From Alfred -t HelloWorld,Testing`
# If MEMOS_DEFAULT_TAG=CLI, tags will be: #CLI #HelloWorld #Testing

- Open your memo webpage in the browser with:

`memos open`

## Requirements

- Alfred 5 with Powerpack
- Python 3.x (included with macOS)
- Internet connection to access your Memos instance

## License

MIT License 