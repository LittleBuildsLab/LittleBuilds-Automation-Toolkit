project_name = "Screenshot Lifecycle Manager"
author = input("What is your name? ")
version = "0.2"

print("📸", project_name)
print("------------------------------")
print()

print(f"Hello, {author}!")
print()

print(f"Welcome to version {version}.")
print("Let's organize some screenshots!")

coffee_level = "☕☕☕☕☕"
print(f"Coffee Level: {coffee_level}")

screenshot_count = int(input("How many screenshots do you have today? "))

cleanup_goal = int(input("How many screenshots do you want to clean today? "))
remaining = screenshot_count - cleanup_goal

print()
print(f"You have {screenshot_count} screenshots.")
print(f"Today's cleanup goal is {cleanup_goal}.")
print(f"After cleanup, {remaining} screenshots will remain.")

if remaining == 0:
    print("🏆 Amazing! You cleaned every screenshot!")
elif cleanup_goal == 0:
    print("Maybe tomorrow then. 😄")
elif cleanup_goal <= 10:
    print("Nice! Every little bit helps.")
else:
    print("Wow! Someone is serious about organizing today! 🚀")

print(f"Thanks for organizing your screenshots, {author}!")
print("Have a great day! ☕")