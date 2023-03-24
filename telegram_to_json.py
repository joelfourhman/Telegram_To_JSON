import json
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

def save_message(update: Update, context):
    """
    Save a message as a JSON object.

    Args:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.CallbackContext): The context object for the callback function.
    """
    # Create a dictionary to store message information
    message_data = {
        "chat_id": update.message.chat_id,
        "message_id": update.message.message_id,
        "from_user": update.message.from_user.to_dict(),
        "date": update.message.date.strftime('%Y-%m-%d %H:%M:%S'),
        "text": update.message.text,
    }

    # Convert dictionary to JSON format
    message_json = json.dumps(message_data, indent=4)

    # Save the JSON to a file
    with open('messages.json', 'a') as f:
        f.write(message_json + '\n')

if __name__ == '__main__':
    # Create a new bot object using your API token
    updater = Updater('YOUR_API_TOKEN_HERE', use_context=True)

    # Set up a message handler that will call save_message for every new message
    message_handler = MessageHandler(Filters.text, save_message)
    updater.dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()
