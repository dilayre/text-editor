# Simple Text File Editor

filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
except:
    content = ""

while True:
    print("\n1. Show records")
    print("2. Add record")
    print("3. Delete record")
    print("4. Update record")
    print("5. Exit")

    ch = input("Choose: ")

    # SHOW
    if ch == "1":
        if content.strip() == "":
            print("No records.")
        else:
            print(content)

    # ADD
    elif ch == "2":
        print("Write like: name | job | phone")
        line = input("> ")

        parts = line.split("|")
        if len(parts) != 3:
            print("Wrong format.")
            continue

        # count records
        count = 0
        for c in content.split("\n"):
            if "." in c:
                if c.split(".")[0].strip().isdigit():
                    count += 1

        num = count + 1

        line1 = str(num) + ". Ad: " + parts[0].strip()
        line2 = "Peşe: " + parts[1].strip()
        line3 = "Telefon: " + parts[2].strip()
        new_text = line1 + "\n" + line2 + "\n" + line3 + "\n"

        if content.strip() == "":
            content = new_text
        else:
            content = content + "\n" + new_text

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print("Saved.")

    # DELETE
    elif ch == "3":
        num = input("Record number: ")

        blocks = content.split("\n\n")
        new_blocks = []
        found = False

        for b in blocks:
            if b.startswith(num + "."):
                found = True
            else:
                new_blocks.append(b)

        if not found:
            print("Not found.")
            continue

        content = "\n\n".join(new_blocks)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print("Deleted.")

    # UPDATE
    elif ch == "4":
        num = input("Record number: ")

        blocks = content.split("\n\n")
        idx = -1

        for i, b in enumerate(blocks):
            if b.startswith(num + "."):
                idx = i
                break

        if idx == -1:
            print("Not found.")
            continue

        print("1. Update name")
        print("2. Update job")
        print("3. Update phone")
        up = input("Choose: ")

        lines = blocks[idx].split("\n")

        if up == "1":
            new = input("New name: ")
            lines[0] = num + ". Ad: " + new

        elif up == "2":
            new = input("New job: ")
            lines[1] = "Peşe: " + new

        elif up == "3":
            new = input("New phone: ")
            lines[2] = "Telefon: " + new

        else:
            print("Wrong choice.")
            continue

        blocks[idx] = "\n".join(lines)
        content = "\n\n".join(blocks)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print("Updated.")

    # EXIT
    elif ch == "5":
        print("Bye.")
        break

    else:
        print("Wrong choice.")
