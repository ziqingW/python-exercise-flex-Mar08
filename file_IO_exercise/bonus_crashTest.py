import io
file_handle = io.StringIO()
while True:
    file_handle.write("B" * 1024 * 1024)
    size_contents = len(file_handle.getvalue())
    print("Characters count: {}".format(size_contents))

# crash happens at counting of 208666624
# MemoryError
# I use 1mb as one time write, so totally it reached to 200mb
# it's later than I thought, I never expect cloud9 has memory as much as 200mb