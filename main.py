from slackclient import SlackClient
import yaml
import json

slack_token = ''
DATA_PATH = 'data'


try:
    with open('.env.yml') as file:
        obj = yaml.load(file)
        slack_token = obj['SLACK_API_TOKEN']
except IOError:
    print('can not find .env.yml')
    exit(1)


sc = SlackClient(slack_token)
channels = sc.api_call('channels.list')
members = sc.api_call('users.list')


def save_json(name, json_dict):
    f = open(name, 'w')
    json.dump(json_dict, f, indent=4, ensure_ascii=False)


save_json('%s/channels.json' % DATA_PATH, channels)
save_json('%s/members.json' % DATA_PATH, members)

for channel in channels['channels']:
    history = sc.api_call('channels.history', channel=channel['id'])
    save_json('%s/history/%s.json' % (DATA_PATH, channel['id']), history)


# def find(iterable, default=None, pred=None):
#     return next(filter(pred, iterable), default)
#
#
# def serializeChannelMember(channel, members):
#     for i, userId in enumerate(channel['members']):
#         result = find(members, pred=lambda member: userId == member['id'])
#         if result is None:
#             print(userId)
#             exit(1)
#         channel['members'][i] = result
#     return channel
#
#
# for channel in channels:
#     channel = serializeChannelMember(channel, members)
