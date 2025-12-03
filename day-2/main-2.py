from pathlib import Path

PATH = Path(__file__).with_name("input.txt")

invalid_ids = []

with open(PATH) as input:
  line = input.readline()
  for segment in line.split(","):
    start, end = segment.split("-")

    for id in range(int(start), int(end)+1):
      # https://www.geeksforgeeks.org/python/python-check-if-string-repeats-itself/
      s = str(id)
      res = s in (s + s)[1:-1]

      if (res):
        invalid_ids.append(id)

print(sum(invalid_ids))