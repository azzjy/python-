'''
字典推导式面试题
'''

counts = {'MBP':268,'HP':125,'DELL':201,'Lenovo':199,'ACER':99}

counts = {key:value for key,value in counts.items() if value >= 200}

print(counts)