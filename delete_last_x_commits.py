import git
import os


repo_name = "temporary_repo\\"


def delete_last_commits(repo_url, n):

    # Deleting temporary repository if exists
    if os.path.exists(repo_name):
        git.rmtree(repo_name)

    # Creating temporary cloned repository
    git.Repo.clone_from(repo_url, repo_name)

    repo = git.Repo(repo_name)

    try:
        # Deleting last commits
        g = git.Git(repo_name)
        g.execute(["git", "reset", "--soft", f"HEAD~{n}"])

        # Pushing changes
        origin = repo.remote(name='origin')
        origin.push(force=True)

        print(f"Last {n} commits deleted successfully.")

    except:
        print(f"Can't delete last {n} commits.")

    # Deleting temporary repository
    repo.git.clear_cache()
    if os.path.exists(repo_name):
        git.rmtree(repo_name)


if __name__ == "__main__":

    url = "https://github.com/bartekk2908/test_repo.git"
    x = 47

    delete_last_commits(url, x)
