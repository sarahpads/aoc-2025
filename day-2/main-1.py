from pathlib import Path

PATH = Path(__file__).with_name("input.txt")

invalid_ids = []

with open(PATH) as input:
  line = input.readline()
  for segment in line.split(","):
    start, end = segment.split("-")

    for id in range(int(start), int(end)+1):
      str_id = str(id)
      # Using divmod to get the quotient (q) and remainder (r) when dividing the string length by 2
      q, r = divmod(len(str_id), 2)

      # Slicing the string to get the first half, including the remainder if the length is odd
      first, second = str_id[:q + r], str_id[q + r:]

      if first == second:
        invalid_ids.append(id)

print(sum(invalid_ids))