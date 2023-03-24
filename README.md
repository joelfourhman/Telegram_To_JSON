# Telegram To JSON

Telegram To JSON is a simple Telegram bot written in Python that saves every incoming message as a JSON object. The bot uses the python-telegram-bot library to interact with the Telegram API.

## How it Works

When the bot receives a new message, it creates a dictionary to store information about the message, including the chat ID, message ID, user who sent the message, date and time the message was sent, and the message text. It then converts this dictionary to a JSON object and saves it to a file called `messages.json`.

## Dependencies

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Installation

1. Clone this repository:
```
git clone https://github.com/joelfourhman/Telegram_To_JSON.git
cd Telegram_To_JSON
```

2. Install the required dependencies:
```
pip install python-telegram-bot
```

3. Create a new Telegram bot and obtain its API token. You can follow the instructions in the [Telegram Bot API documentation](https://core.telegram.org/bots#6-botfather) to do this.

4. Replace `'YOUR_API_TOKEN_HERE'` in the code with your actual Telegram bot API token.

5. Run the script:
```
python telegram_to_json.py
```

## Usage

To use the bot, simply start a chat with it on Telegram and send a message. The bot will automatically save the message as a JSON object in the `messages.json` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

