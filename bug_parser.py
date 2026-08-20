def parse_file(filepath):

    if filepath.endswith(".txt") or filepath.endswith(".log"):

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:

            text = f.read()

            print("========== BUG TEXT ==========")
            print(text[:1000])
            print("==============================")

            return text