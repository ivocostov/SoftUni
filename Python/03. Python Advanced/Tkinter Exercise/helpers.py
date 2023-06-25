from canvas import frame


def clean_screen():
    frame.delete("all")
    frame.delete("error")  # Delete everything with tag "error" - present in authentication file, check registration function
