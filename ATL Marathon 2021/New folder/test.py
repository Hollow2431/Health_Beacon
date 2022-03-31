"""from time import time

def print_after(text):
  start = int(time())
  print(f'Starting: {start}')
  printed = 0
  print(f'Hacker will come at {start + 10}')
  while printed == 0:
    if int(time()) == (start + 10):
      print(text)
      printed = 1
  

print('Hacker is coming.')
print_after('Hacker has come.')
"""

"""
from pywebio import start_server
from pywebio.output import clear, put_buttons, put_markdown, put_table


def program():
  clear()
  put_markdown("# Vital Sign Viewer")
  put_markdown('### Choose an option')
  put_buttons(['View Vital Signs'], onclick=options)


def options(button):
  if button == 'View Vital Signs':
    vital_signs()


def vital_signs():
  clear()
  put_markdown("# Vital Sign Viewer")
  put_markdown("### The details of the Patient are given below")
  put_markdown("**Name of the patient:** {name}")
  table = [
    ['Time', 'Blood pressure', 'Pulse Rate', 'Temperature', 'Breathing Rate']
  ]
  # Bring data from database and add in 'table'
  put_table(table)


if __name__ == "__main__":
  start_server(program, port=1025)
"""

from pywebio.output import put_html
from pywebio import start_server

"""
def program():
  put_html('''
    <table>
      <tr>
        <th><font color="red">Row 1</font></th>
        <th>Row 2</th>
      </tr>
      <tr>
        <td style="color:blue;">Content 1</font></td>
        <td>Content 2</td>
      </tr>
    </table>
  ''')

if __name__ == "__main__":
  start_server(program, port=1025)
"""

'''
def add_row(command, row):
  # '<tr></tr>'
  # row = ['abc', ['123','Red']]
  command += '\n<tr>'

  for i in row:
    if type(i) == str:
      data = '\n<td>'+i+'</td>'
    elif type(i) == list:
      data = f'\n<td style="color:{i[1].lower()};">{i[0]}</font></td>'
    command += data
  
  command += '\n</tr>'
  
  return command

c = '<table>'
c = add_row(c, ['Content 1', 'Content 2', ['Content 3', 'blue']])
c += '\n</table>'

print(c)
'''

reading = int(input('Enter a reading: '))
def check_with_threshold(threshold_value, reading):
  if (threshold_value - 10) < reading and reading < (threshold_value + 10):
    return 'Good'
  elif (threshold_value - 20) < reading and reading < (threshold_value + 20):
    return 'Moderate'
  else:
    return 'Critical'
