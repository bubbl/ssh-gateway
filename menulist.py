MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"
menu_data = {
  'title': 'Gateway', 'type': MENU, 'subtitle': "----------------------------------------",
  'options':[
    { 'title': "Server nodes", 'type': MENU, 'subtitle': '', 'options': [
        { 'title': "Node 1", 'type': COMMAND, 'command': 'ssh node2"' },
        { 'title': "Node 2", 'type': COMMAND, 'command': 'ssh node1"' }
      ]
    }
  ]
}
