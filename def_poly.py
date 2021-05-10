def poly(pixel):
	#return max((1947*pixel - 11.39*pixel + 0.0169*pixel*pixel),255)
	return (1947*pixel - 11.39*pixel + 0.0169*pixel*pixel)

user_input = int(input())
print(poly(user_input))