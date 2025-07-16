# -------------------------------
# DFS Web Crawler with Graph Visualization
# -------------------------------

import networkx as nx
import matplotlib.pyplot as plt

# Simulated web structure (editable by user)
web = {
    "home": ["about", "blog"],
    "about": ["contact"],
    "blog": ["post1", "post2"],
    "post1": [],
    "post2": [],
    "contact": []
}

# DFS with tree-style output
def dfs_crawl(page, visited, depth=0, is_last=False):
    if page in visited:
        return

    prefix = "│   " * (depth - 1) + ("└── " if is_last else "├── ") if depth > 0 else ""
    print(f"{prefix}📄 Visiting: {page} (Depth {depth})")
    visited.add(page)

    links = web.get(page, [])
    for i, link in enumerate(links):
        last = (i == len(links) - 1)
        dfs_crawl(link, visited, depth + 1, is_last=last)

# Visual graph output using matplotlib and networkx
def visualize_graph(web):
    G = nx.DiGraph()

    for page, links in web.items():
        for link in links:
            G.add_edge(page, link)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color='skyblue',
        node_size=2000,
        edge_color='gray',
        font_size=10,
        font_weight='bold',
        arrows=True,
        arrowsize=20,
        arrowstyle='-|>'
    )
    plt.title("Web Crawler Graph Visualization")
    plt.axis('off')
    plt.show()

# Display current web structure
def display_web_structure():
    print("\n🌐 Web Structure (Simulated):")
    for page, links in web.items():
        print(f"  {page} ➡ {', '.join(links) if links else 'No links'}")

# Menu-driven interface
def main():
    print("\n🔍 Welcome to the DFS Web Crawler Simulation")

    while True:
        display_web_structure()

        print("\n📘 Menu:")
        print("1. Start crawling from 'home'")
        print("2. Start crawling from custom page")
        print("3. Add a new page with links")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            start = "home"
        elif choice == "2":
            start = input("Enter start page name: ").strip().lower()
            if start not in web:
                print("❌ Invalid page. Try again.")
                continue
        elif choice == "3":
            new_page = input("Enter new page name: ").strip().lower()
            links_input = input("Enter linked pages (comma-separated): ").strip()
            links = [link.strip().lower() for link in links_input.split(",") if link.strip()]

            if new_page in web:
                print(f"⚠️ Page '{new_page}' already exists. Updating its links...")
            else:
                print(f"✅ Page '{new_page}' added.")

            web[new_page] = links
            for link in links:
                if link not in web:
                    web[link] = []  # Automatically create empty pages if needed

            print("🔗 Links added successfully.")
            continue
        elif choice == "4":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.")
            continue

        visited_pages = set()
        print(f"\n🧭 Crawling started at: [{start}]")
        dfs_crawl(start, visited_pages)

        print("\n✅ Crawl Complete!")
        print("📄 Visited Pages:", ", ".join(sorted(visited_pages)))

        # Show graph visualization
        visualize_graph(web)

# Run the program
if __name__ == "__main__":
    main()
