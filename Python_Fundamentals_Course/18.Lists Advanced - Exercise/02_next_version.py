version = input().split('.')

version_as_digits = list(map(int, version))
version_as_digits[-1] += 1

for current_index in range(len(version_as_digits) - 1, -1, -1):
    if version_as_digits[current_index] > 9:
        version_as_digits[current_index] = 0
        if current_index - 1 >= 0:
            version_as_digits[current_index - 1] += 1

print('.'.join(str(version_as_digits) for version_as_digits in version_as_digits))
