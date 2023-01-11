from sentry_sdk import capture_message
capture_message("Hello World") # Will create an event in Sentry.
