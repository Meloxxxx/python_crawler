from pythonping import ping
from prettytable import PrettyTable
from rich.console import Console
from rich.table import Column, Table

text = ping('172.67.177.44', verbose=False)
console = Console(width=200)
table = Table(show_header=True, width=120)
table.add_column('Target Address')
table.add_column('Target IP')
table.add_column('Status')
table.add_column('Packet Loss')
table.add_column('Packet Size')
table.add_column('RTT')
for i in text._responses:
    if len(str(i)) == 17:
        table.add_row('https://meirentu.top/', '172.67.177.44',
                      str(i), str(text.packet_loss), 'NaN', 'NaN')
    else:
        table.add_row('https://meirentu.top/', '172.67.177.44',
                      str(i).split(',')[0], str(text.packet_loss),
                      ''.join(str(i).split(',')[1].split(' ')[1:3]),
                      str(i).split(',')[1].split(' ')[-1])
console.print(table)
# tb = PrettyTable()
# tb.field_names = ['Target Address', 'Target IP', 'Status', 'Packet Loss', 'Packet Size', 'RTT']
# for i in text._responses:
#     tb.add_row(['https://meirentu.top/', '172.67.177.44', str(i).split(',')[0],
#                 text.packet_loss, ''.join(str(i).split(',')[1].split(' ')[1:3]), str(i).split(',')[1].split(' ')[-1]])
# print(tb)