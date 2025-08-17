def calculateScore(instructions, values):
    inx = 0
    total_val = 0
    visited_inx = set()

    while inx < len(instructions):
        if not inx in visited_inx:
            visited_inx.add(inx)

            instruction = instructions[inx]
            value = values[inx]

            if instruction == "jump":
                inx += value
                continue

            elif instruction == "add":
                total_val += value
        else:
            break

        inx += 1

    return total_val


if __name__ == "__main__":
    instructions = ["add", "jump", "add", "jump"]
    values = [5, 2, 3, -2]

    print(calculateScore(instructions, values))
