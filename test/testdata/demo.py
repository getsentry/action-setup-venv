from sentry_sdk import capture_message
print("Creating event in Sentry.")
capture_message("Hello World")
print("Done.")
