
web = {
    "home": ["about", "blog"],
    "about": ["contact"],
    "blog": ["post1", "post2"],
    "post1": [],
    "post2": [],
    "contact": []
}

# DFS function to crawl pages with depth tracking
def dfs_crawl(page, visited, depth=0):
    if page in visited:
        return
    print("  " * depth + f"📄 Visiting: {page} (Depth: {depth})")
    visited.add(page)

    # Visit all linked pages
    for link in web.get(page, []):
        dfs_crawl(link, visited, depth + 1)

# Display web structure (optional feature)
def display_web_structure():
    print("\n🌐 Web Structure (Simulated):")
    for page, links in web.items():
        print(f"  {page} ➡ {', '.join(links) if links else 'No links'}")

# Menu-driven program
def main():
    print("\n🔍 Welcome to the DFS Web Crawler Simulation")
    display_web_structure()

    while True:
        print("\n📘 Menu:")
        print("1. Start crawling from 'home'")
        print("2. Start crawling from custom page")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            start = "home"
        elif choice == "2":
            start = input("Enter start page name: ").strip().lower()
            if start not in web:
                print("❌ Invalid page. Try again.")
                continue
        elif choice == "3":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.")
            continue

        visited_pages = set()
        print(f"\n🚀 Starting DFS Crawl from: {start}")
        dfs_crawl(start, visited_pages)

        print("\n✅ Crawl Complete!")
        print("📄 Visited Pages:", ", ".join(visited_pages))

# Run the program
if __name__ == "__main__":
    main()
