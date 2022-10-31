from kubiya import ActionStore
from helpers import action1, action2, action3, action_any

actionstore = ActionStore("sample_action_store", "0.0.1")
actionstore.register_action("action1", action1)
actionstore.register_action("action2", action2)
actionstore.register_action("action3", action3)
actionstore.register_action("action_any", action_any)
