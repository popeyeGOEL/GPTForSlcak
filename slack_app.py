import logging 
import os

from slack_bolt import App, BoltContext
from slack_sdk.web import WebClient
from slack_sdk.http_retry.builtin_handlers import RateLimitErrorRetryHandler


from slack.bolt_listeners import before_authorize, register_listeners
from slack.env import (
    SLACK_APP_TOKEN,
    SLACK_BOT_TOKEN,
    USE_SLACK_LANGUAGE,
    SLACK_APP_LOG_LEVEL,
    AI_MODEL
)

from slack.slack_ops import(
    build_home_tab,
    DEFAULT_HOME_TAB_MESSAGE,
    DEFAULT_HOME_TAB_CONFIGURE_LABEL
)

from slack.i18n import translate


if __name__ == "__main__":
    from slack_bolt.adapter.socket_mode import SocketModeHandler

    logging.basicConfig(level=SLACK_APP_LOG_LEVEL)

    app = App(
        token=SLACK_BOT_TOKEN,
        before_authorize=before_authorize,
        process_before_response=True,
    )

    app.client.retry_handlers.append(RateLimitErrorRetryHandler(max_retry_count=2))

    register_listeners(app)

    @app.event("app_home_opened")
    def render_home_tab( client: WebClient, context: BoltContext ):
        text = translate(
            context=context,
            text=DEFAULT_HOME_TAB_MESSAGE
        ),

        configure_label= translate(
            context=context,
            text=DEFAULT_HOME_TAB_CONFIGURE_LABEL
        )
        client.views_publish(
            user_id=context.user_id,
            view=build_home_tab(text,configure_label)
        )

    if USE_SLACK_LANGUAGE is True:
        @app.middleware
        def set_locale(
            context: BoltContext,
            client: WebClient,
            next_,
        ):
            user_id = context.actor_user_id or context.user_id
            user_info = client.users_info(user=user_id, include_locale=True)
            context["locale"] = user_info.get("user", {}).get("locale")
            next_()

    
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
