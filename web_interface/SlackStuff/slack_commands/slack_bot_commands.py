from slackclient import SlackClient


def slack_message_api(slack_client, response, channel):
    '''
    Sends message to the slack channel confirming action
    '''
    slack_client.api_call("chat.postMessage",
                          channel=channel,
                          text=response)

def handle_command(command, channel, slack_client):
    """
        Executes bot command if the command is known.
    """
    response = None
    # This is where you start to implement more commands!
    if 'pause' in command:
        pause_command(slack_client, channel)
    elif 'unpause' in command:
         unpause_command(slack_client, channel)
    elif 'issue' in command:
        print("issue")

    elif 'velocity' in command:
        #getRobotSpeed()
        print("velocity-test");


    elif 'location'  in command:
        print("location");


    elif 'battery_voltage' in command:
        print("battery_voltage");


    elif 'distance' in command:
        print("distance");


    elif 'time' in command:
        print("time");


    elif 'mission_type' in command:
        print("mission_type");
    
    else:
        unknown_command(slack_client, channel)


def pause_command(slack_client, channel):
        response = "Okay, attempting to pause!"
        slack_message_api(slack_client, response, channel)
        ####### PUT RASBERRY PI CODE HERE AND DELETE BELOW TWO LINES ########
        response = 'This command is unimplemented.'
        slack_message_api(slack_client, response, channel)


def unpause_command(slack_client, channel):
    response = "Okay, attempting to pause!"
    slack_message_api(slack_client, response, channel)
    ####### PUT RASBERRY PI CODE HERE AND DELETE BELOW TWO LINES ########
    response = 'This command is unimplemented.'
    slack_message_api(slack_client, response, channel)


def unknown_command(slack_client, channel): #this function is a wildcard for unaccepted input
    response = "Not sure what you mean. Try one of the accepted commands."
    slack_message_api(slack_client, response, channel)
