
def ft_count_harvest_recursive(days=None, i = 1):
	if days is None:
		days = int(input("Days until harvest: ")) 
	if i == days:
		print("Harvest time!")
	else:
		print(f"Day", i)
		ft_count_harvest_recursive(days ,i + 1)
