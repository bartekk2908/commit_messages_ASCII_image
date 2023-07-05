import git
import os


repo_name = "temporary_repo\\"


def get_ascii_addition(char):
    addition = 1
    if char == "." or char == "_":
        addition = 2
    elif char == "9":
        addition = 8
    elif char == "Z":
        addition = 7
    return addition


def next_string_in_order(string):
    string = list(string)

    addition = get_ascii_addition(string[-1])
    if string[-1] == "z":
        string.append("/")

    string[-1] = chr(ord(string[-1]) + addition)

    return "".join(string)


def new_string_in_order(string):
    index = 1
    while True:
        new_string = list(string[:index])

        addition = get_ascii_addition(new_string[-1])
        if new_string[-1] == "z":
            if len(string) == index:
                addition = 0
            else:
                index += 1
                continue
        break

    new_string[-1] = chr(ord(new_string[-1]) + addition)
    new_string.append("0")

    return "".join(new_string)


def create_aa_commits_messages(ascii_art, repo_url):

    # Deleting temporary repository
    if os.path.exists(repo_name):
        git.rmtree(repo_name)

    # Creating temporary cloned repository
    git.Repo.clone_from(repo_url, repo_name)

    repo = git.Repo(repo_name)

    # Getting list of directories and files
    folders = []
    for folder in repo.commit().tree.trees:
        folders.append(folder.path)
    files = []
    for file in repo.commit().tree.blobs:
        files.append(file.path)
    # print(folders)
    # print(files)

    n = ascii_art.count('\n')

    m = len(folders + files)

    # Creating missing files for ascii art
    if m < n:
        file_name = new_string_in_order(files[-1] if files else '/')
        for _ in range(n-m):
            file_name = next_string_in_order(file_name)
            open(repo_name + file_name, 'a').close()
            files.append(file_name)
            repo.index.add(file_name)

    # Changing names
    g = git.Git(repo_name)
    fnf = folders + files
    for i in range(n):
        g.execute(["git", "mv", fnf[i], fnf[i] + "_"])
    repo.git.commit('--allow-empty-message', '-m', '', author='')

    # Re-changing to previous names and committing with one line of ascii art
    lines = ascii_art.split('\n')
    for i in range(n):
        g.execute(["git", "mv", fnf[i] + "_", fnf[i]])
        repo.index.add(fnf[i])
        repo.git.commit('--allow-empty-message', '-m', f'{lines[i]}')

    # Pushing commits with ascii art
    origin = repo.remote(name='origin')
    origin.push()

    """
    # Deleting temporary repository
    if os.path.exists(repo_name):
        git.rmtree(repo_name)
    """


if __name__ == "__main__":

    with open("ascii_art.txt", "r") as file:
        art = file.read()
    print("Given ASCII art: ")
    print(art)

    url = "https://github.com/bartekk2908/commit_messages_ASCII_art.git"

    create_aa_commits_messages(art, url)
