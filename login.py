from getpass import getpass


def login(users: dict[str, str]) -> bool:
	"""Prompt for a username and password and check them against users."""
	username = input("Username: ").strip()
	password = getpass("Password: ")

	if users.get(username) == password:
		print("Login successful.")
		return True

	print("Invalid username or password.")
	return False


if __name__ == "__main__":
	login({"aria": "change-me"})
