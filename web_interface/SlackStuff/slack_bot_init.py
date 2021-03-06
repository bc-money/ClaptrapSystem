import re
from slackclient import SlackClient
from slack_commands import slack_bot_commands
import bot as bt
import numpy as np 
import tflearn as tflearn
from bot import categories
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

if __name__ == '__main__':
    slack_client = SlackClient("xoxb-151134378128-381943266085-Rq687iYzMdRVNK98SQThzwQ9")
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command: #if command exists
                print("You sent the command [", command, "] in channel [", channel, "]")
                slack_bot_commands.handle_command(command, channel, slack_client)

                model = bt.mlmodel.model
                # model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
                # model.fit(train_x, train_y)
                # model.save('model.tflearn')

                index = np.argmax(model.predict([bt.get_tf_record(command)]))
                list_test = command.split()
                #print(bt.category())
                #print(list_test[index])
                #print(list_test)
                print(categories[np.argmax(model.predict([bt.get_tf_record(command)]))])
                #print(list_test)
