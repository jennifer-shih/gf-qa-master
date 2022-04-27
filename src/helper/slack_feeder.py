import slack

from src.helper.log import Logger


class SlackFeeder:

    TOKEN = "xoxb-7139829557-2061060582739-gaiSJLDyGstCq5ZNFtHwqufg"

    @staticmethod
    def send(channels: str, msg: str, token=TOKEN):
        Logger.getLogger().debug("Send message to Slack")
        client = slack.WebClient(token=token)
        response = client.chat_postMessage(channel=channels, text=msg)
        Logger.getLogger().debug("Response from Slack: {}".format(response))
        return response

    @staticmethod
    def post_file(
        path,
        channels: str,
        file_title: str = "",
        filename: str = "",
        msg: str = "",
        token=TOKEN,
    ):
        """
        Comma-separated list of channel names or IDs where the file will be shared.
        feed-qa,qa-channel,test
        """
        Logger.getLogger().debug("Post image to Slack")
        client = slack.WebClient(token=token)
        response = client.files_upload(
            file=path,
            title=file_title,
            filename=filename,
            initial_comment=msg,
            channels=channels,
        )
        Logger.getLogger().debug("Response from Slack: {}".format(response))
        return response
