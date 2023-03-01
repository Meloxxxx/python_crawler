
from MeirentuNet import Meirentu
from rich.console import Console
from rich.table import Table
from pythonping import ping

def network_testing():
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
        target_add = 'https://meirentu.top/'
        target_ip = '172.67.177.44'
        packet_loss = str(text.packet_loss)
        if len(str(i)) == 17:
            status = str(i)
            packet_size = 'NaN'
            RTT = 'NaN'
            table.add_row(target_add, target_ip,
                          status, packet_loss, packet_size, RTT)
        else:
            status = str(i).split(',')[0]
            packet_size = ''.join(str(i).split(',')[1].split(' ')[1:3])
            RTT = str(i).split(',')[1].split(' ')[-1]
            table.add_row(target_add, target_ip,
                          status, packet_loss, packet_size, RTT)
    console.print(table)


if __name__ == '__main__':
    t = """           ______                    __             ___   _____ ____  ____ 
              / ____/________ __      __/ /__  _____   |__ \ / ___// __ \/ __ \\
             / /   / ___/ __ `/ | /| / / / _ \/ ___/   __/ // __ \/ / / / / / /
            / /___/ /  / /_/ /| |/ |/ / /  __/ /      / __// /_/ / /_/ / /_/ / 
            \____/_/   \__,_/ |__/|__/_/\___/_/      /____/\____/\____/\____/ """
    print(t)
    print('网络测速结果:')
    network_testing()
    mrt = Meirentu()
    while True:
        choice = str(input('请选择按人爬取或按机构爬取(a->人, b->机构, q->退出):'))
        if choice == 'a':
            mrt.person_clawer()
        elif choice == 'b':
            mrt.institute_clawer()
        elif choice == 'q':
            print('已选择退出!')
            break
        else:
            print('无效输入!请重新输入选择!')
