import logging
import sys
import os
from dotenv import load_dotenv

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from routers import main_routers, housework_services_routers, food_services_routers

load_dotenv()
# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv('bot_token')

# Webserver settings
# bind localhost only to prevent any external access
WEB_SERVER_HOST = str(os.getenv('WEB_SERVER_HOST'))
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = int(os.getenv('WEB_SERVER_PORT'))

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = ""
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = "my-secret"
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public DNS with HTTPS support
BASE_WEBHOOK_URL = os.getenv('BASE_WEBHOOK_URL')

# All handlers should be attached to the Router (or Dispatcher)


async def on_startup(bot: Bot) -> None:
    # If you have a self-signed SSL certificate, then you will need to send a public
    # certificate to Telegram
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)


def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(main_routers.router)
    dp.include_router(food_services_routers.router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()