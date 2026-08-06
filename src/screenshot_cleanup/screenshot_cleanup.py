from pathlib import Path

project_name = "Screenshot Lifecycle Manager"
author = input("What is your name? ")
version = "0.2"

screenshot_folder = Path.home() / "Pictures" / "Screenshots"

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


while True:
    print()
    print("===== Screenshot Lifecycle Manager =====")
    print("1. Screenshot report")
    print("2. Cleanup planner")
    print("3. Coffee status")
    print("4. Exit")
    print()

    choice = input("Choose an option: ")

    if choice == "1":
        screenshots = list(screenshot_folder.glob("*.png"))

        print()

        if not screenshots:
            print("📭 No PNG screenshots found.")
        else:
            oldest = min(
                screenshots,
                key=lambda file: file.stat().st_mtime
            )

            newest = max(
                screenshots,
                key=lambda file: file.stat().st_mtime
            )

            total_bytes = sum(
                file.stat().st_size for file in screenshots
            )

            total_mb = total_bytes / (1024 * 1024)

            print("📸 Screenshot Report")
            print("--------------------")
            print(f"Total screenshots: {len(screenshots)}")
            print(f"Oldest: {oldest.name}")
            print(f"Newest: {newest.name}")
            print(f"Storage used: {total_mb:.2f} MB")

    elif choice == "2":
        print("🧹 Opening cleanup planner...")

    elif choice == "3":
        print(f"Coffee Level: {coffee_level}")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")