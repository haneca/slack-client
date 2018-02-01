import sys
import slack

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python3 index.py cmd [options]')
        print('cmd: command (member, channel, post)')
        print('\tmember: get member list')
        print('\tchannel: get channel list')
        print('\tpost: post message to specified member / channel as a bot')
        print('\t\tpython3 index.py post member_id / channel_id message')
    else:
        cmd = sys.argv[1]
        if cmd == 'member':
            slack.get_member_list()
        elif cmd == 'channel':
            slack.get_channel_list()
        elif cmd == 'post':
            slack.post_message(sys.argv[3], sys.argv[2], 'Python Bot')
        else:
            print('wrong command')
