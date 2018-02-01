# Slack Client

In this project,  you can get member list or channel list. Moreover you can post message to member / channel as a Bot.

### Installation

```
# pip3 install -r requirements.txt
```

### Usage

1. Get slack legacy token from https://api.slack.com/custom-integrations/legacy-tokens .
2. Copy token to token in slack.py.

```
# python3 index.py cmd [options]
  cmd: command (member, channel, post)
  member: get member list
  channel: get channel list
  post: post message to specified member / channel as a bot
    python3 index.py post member_id / channel_id message
```

### License

This project is licensed under the terms of the MIT License.
