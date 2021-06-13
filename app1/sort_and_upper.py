def sort_upper(*args):
  args = [i.upper() for i in args ]
  return sorted(args)

args = ["lower", "upper", "right", "left"]
print(sort_upper(*args))