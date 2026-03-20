import os
from Classes.ServerConnection import ServerConnection

port = int(os.environ.get("PORT", 9339))
ServerConnection(("0.0.0.0", port))
