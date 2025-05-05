import requests
from collections import Counter
import matplotlib.pyplot as plt
import datetime

GITHUB_API = "https://api.github.com"


def get_user_repos(username):
    url = f"{GITHUB_API}/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching repos: {response.status_code}")
    return response.json()


def analyze_languages(repos):
    languages = [repo['language'] for repo in repos if repo['language']]
    return Counter(languages)


def analyze_activity(repos):
    activity = []
    for repo in repos:
        pushed_at = repo['pushed_at']
        if pushed_at:
            dt = datetime.datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ")
            activity.append(dt.hour)
    return Counter(activity)


def plot_language_stats(language_counter):
    labels, values = zip(*language_counter.items())
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='skyblue')
    plt.title('Languages Used')
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('language_usage.png')
    plt.close()


def plot_activity_stats(activity_counter):
    hours = list(range(24))
    values = [activity_counter.get(hour, 0) for hour in hours]
    plt.figure(figsize=(8, 5))
    plt.plot(hours, values, marker='o')
    plt.title('Push Activity by Hour (UTC)')
    plt.xlabel('Hour of Day')
    plt.ylabel('Push Count')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('push_activity.png')
    plt.close()


def main():
    username = input("Enter GitHub username: ")
    repos = get_user_repos(username)
    lang_stats = analyze_languages(repos)
    activity_stats = analyze_activity(repos)

    print("\nLanguage Stats:", lang_stats)
    print("\nActivity Stats:", activity_stats)

    plot_language_stats(lang_stats)
    plot_activity_stats(activity_stats)
    print("\nGraphs saved as 'language_usage.png' and 'push_activity.png'")


if __name__ == '__main__':
    main()
