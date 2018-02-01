import json
from slackclient import SlackClient

token = 'copy your token here'
client = SlackClient(token)
def post_message(text, channel, username):
    print('Posting Message to Slack')
    client.api_call('chat.postMessage',
        channel=channel,
        text=text,
        username=username,
        unfurl_links='true')

def get_channel_list():
    print('Print Channel List')
    channels = client.api_call('channels.list')
    channels = json.dumps(channels)
    channels = json.loads(str(channels))

    print('index | channel name | channel id')
    for index, channel in enumerate(channels['channels']):
        print(str(index) + ' | ' + channel['name'] + ' | ' + channel['id'])

def get_member_list():
    print('Print Member List')
    members = client.api_call('users.list')
    members = json.dumps(members)
    members = json.loads(str(members))

    print('index | member name | member id')
    for index, member in enumerate(members['members']):
        print(str(index) + ' | ' + member['name'] + ' | ' + member['id'])
