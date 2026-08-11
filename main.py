import functions


def main():
    while True:
        directory = input("Target directory: ")
        try:
            files = functions.scan(directory)
        except FileNotFoundError:
            print("This folder does not exist.")
            continue

        print(f"Found {len(files)} files:")
        print("__________________________")
        for i, file in enumerate(files):
            print(f"{i + 1}.{file}")
        print("__________________________")

            

        stats = functions.organize(directory, files)
        if stats:
            print(f"Organized {stats["moved"]} files in '{directory}' successfully:")
            
            for category, count in stats.items():
                print(f"{count} {category.capitalize()}")

            input("Press enter to exit.")
            break

if __name__ == "__main__":
    main()