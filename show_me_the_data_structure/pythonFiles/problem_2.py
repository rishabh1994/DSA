import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.exists(path):
        files = os.listdir(path)
        counter = 0
        for file in files:
            fullPath = path + "/" + file
            if os.path.isfile(fullPath):
                if fullPath.endswith(suffix):
                    counter += 1
            else:
                counter += find_files(suffix, fullPath)
        return counter
    else:
        return 0


def first_test_case():
    # Expected value is 0 as there is no File which ends with .ABCD extension.
    print(find_files(".ABCD", "/Users/rishabhsanklecha/Desktop"))


def second_test_case():
    # Expected value is 0 as there are no files at this path. The path is wrong.
    print(find_files(".txt", "/Users/rishabhsanklecha/random_wrong_path"))


def third_test_case():
    # Expected value is 39 as there are 39 pdf inside my Desktop folder.
    print(find_files(".pdf", "/Users/rishabhsanklecha/Desktop"))


first_test_case()
second_test_case()
third_test_case()
